#!/bin/bash

# Simplified deployment script for debugging
echo "🚀 Starting simplified deployment..."

# Navigate to project directory
cd /home/bitnami/skerritt-economics-django || exit 1

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cat > .env << EOF
DJANGO_SETTINGS_MODULE=skerritt_site.settings
DJANGO_SECRET_KEY=$(python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*
EOF
fi

# Use development settings for now to avoid SSL issues
export DJANGO_SETTINGS_MODULE=skerritt_site.settings
export $(cat .env | grep -v '^#' | xargs)

# Check if using venv
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    echo "Installing dependencies..."
    pip install -r requirements.txt
    
    echo "Running migrations..."
    python manage.py migrate --noinput
    
    echo "Collecting static files..."
    python manage.py collectstatic --noinput || true
    
    echo "Starting development server on port 8000..."
    # Kill any existing process on port 8000
    sudo lsof -ti:8000 | xargs -r sudo kill -9 || true
    
    # Start server in background
    nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
    
    echo "Server started. PID: $!"
    sleep 5
    
    # Check if it's running
    if curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000" | grep -q "200\|301\|302"; then
        echo "✅ Server is running on port 8000"
    else
        echo "❌ Server failed to start. Last 20 lines of log:"
        tail -n 20 server.log
    fi
else
    echo "❌ No virtual environment found!"
    exit 1
fi