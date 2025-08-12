#!/bin/bash
# Auto-deployment script for Lightsail instance
# Place this on your Lightsail instance at /opt/skerritt-economics/deploy.sh

set -e

DEPLOY_PATH="/opt/skerritt-economics"
LOG_FILE="/var/log/deploy.log"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a $LOG_FILE
}

log "🚀 Starting deployment..."

# Navigate to project directory
cd $DEPLOY_PATH

# Pull latest changes from GitHub
log "📦 Pulling latest code from GitHub..."
git fetch origin main
git reset --hard origin/main

# Check if using Docker or traditional deployment
if [ -f "docker-compose.yml" ]; then
    log "🐳 Deploying with Docker Compose..."
    
    # Pull latest images
    docker-compose pull
    
    # Stop current containers
    docker-compose down
    
    # Build and start new containers
    docker-compose up -d --build
    
    # Wait for containers to be ready
    sleep 5
    
    # Run migrations
    docker-compose exec -T web python manage.py migrate --noinput
    
    # Collect static files
    docker-compose exec -T web python manage.py collectstatic --noinput
    
    # Show container status
    docker-compose ps
    
else
    log "🐍 Deploying with Python/Gunicorn..."
    
    # Activate virtual environment
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    fi
    
    # Install/update dependencies
    pip install -r requirements.txt
    
    # Run migrations
    python manage.py migrate --noinput
    
    # Collect static files
    python manage.py collectstatic --noinput
    
    # Restart Gunicorn
    sudo systemctl restart gunicorn
    
    # Restart Nginx
    sudo systemctl restart nginx
    
    # Check status
    sudo systemctl status gunicorn --no-pager
fi

log "✅ Deployment complete!"

# Optional: Send notification (replace with your notification method)
# curl -X POST https://your-webhook-url -d "Deployment successful"