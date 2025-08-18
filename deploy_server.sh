#!/bin/bash

# Server deployment script for skerritt-economics-django
# This script handles the complete deployment process on the server

set -e

echo "🚀 Starting server deployment..."

# Navigate to project directory
cd /home/bitnami/skerritt-economics-django || exit 1

# Load environment variables if .env exists
if [ -f .env ]; then
    echo "📋 Loading environment variables..."
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "⚠️ Warning: No .env file found. Creating from example..."
    if [ -f .env.example ]; then
        cp .env.example .env
        # Generate a secure secret key
        SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
        sed -i "s/MUST_BE_SET_IN_PRODUCTION/$SECRET_KEY/" .env
        echo "✅ Created .env file with secure secret key"
    else
        echo "❌ Error: No .env.example file found!"
        exit 1
    fi
fi

# Detect deployment method
if [ -f "docker-compose.yml" ] && command -v docker &> /dev/null; then
    echo "🐳 Using Docker deployment..."
    
    # Build and restart containers
    docker compose build
    docker compose down
    docker compose up -d
    
    # Wait for containers to start
    sleep 5
    
    # Run migrations
    docker compose exec -T django python manage.py migrate --noinput || echo "⚠️ Migration failed or no migrations to apply"
    
    # Collect static files
    docker compose exec -T django python manage.py collectstatic --noinput || echo "⚠️ Static collection failed"
    
    # Show container status
    docker compose ps
    
elif [ -f "venv/bin/activate" ]; then
    echo "🐍 Using Python virtual environment deployment..."
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Install/upgrade dependencies
    pip install --upgrade pip
    pip install -r requirements.txt
    
    # Run Django management commands
    python manage.py migrate --noinput || echo "⚠️ Migration failed or no migrations to apply"
    python manage.py collectstatic --noinput || echo "⚠️ Static collection failed"
    
    # Restart application service
    if systemctl is-active --quiet skerritt-economics; then
        echo "🔄 Restarting skerritt-economics service..."
        sudo systemctl restart skerritt-economics
    elif systemctl is-active --quiet gunicorn; then
        echo "🔄 Restarting gunicorn service..."
        sudo systemctl restart gunicorn
    else
        echo "⚠️ No known application service found to restart"
    fi
    
    # Reload nginx if it exists
    if systemctl is-active --quiet nginx; then
        echo "🔄 Reloading nginx..."
        sudo systemctl reload nginx
    fi
    
else
    echo "❌ No valid deployment method found (no Docker or venv)"
    exit 1
fi

# Health check
echo "🏥 Performing health check..."
sleep 5

# Try different possible URLs
for URL in "http://localhost" "http://localhost:8000" "http://127.0.0.1"; do
    response=$(curl -s -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null || echo "000")
    if [ "$response" = "200" ] || [ "$response" = "301" ] || [ "$response" = "302" ]; then
        echo "✅ Application is responding at $URL (HTTP $response)"
        break
    fi
done

if [ "$response" = "000" ] || [ "$response" = "500" ] || [ "$response" = "502" ] || [ "$response" = "503" ]; then
    echo "⚠️ Warning: Application may not be responding correctly (HTTP $response)"
    echo "Please check the logs:"
    echo "  - Docker: docker compose logs"
    echo "  - Systemd: sudo journalctl -u skerritt-economics -n 50"
    echo "  - Gunicorn: sudo journalctl -u gunicorn -n 50"
fi

echo "✅ Deployment script completed!"