#!/bin/bash

# Deployment script for AWS Lightsail
# This script pulls latest code from GitHub and redeploys the Django application with Docker

set -e

echo "🚀 Starting deployment to AWS Lightsail..."

# Pull latest code from GitHub
echo "📥 Pulling latest code from GitHub..."
git pull origin main

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Build Docker images with latest code
echo "📦 Building Docker images with latest code..."
docker build -t skerritt-django-local:latest .

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker compose down

# Start new containers with updated image
echo "🚀 Starting new containers..."
docker compose up -d

# Wait for containers to be ready
echo "⏳ Waiting for containers to be ready..."
sleep 10

# Run migrations (optional - already done in entrypoint)
echo "🔄 Checking database migrations..."
docker compose exec -T django python manage.py showmigrations --plan | head -5

# Note: Static files are collected automatically in the entrypoint script

# Create superuser if needed (optional)
# echo "👤 Checking for superuser..."
# docker compose exec -T django python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@skerritteconomics.com', 'change-this-password')
    print('Superuser created')
else:
    print('Superuser already exists')
"

# Check health
echo "🏥 Checking application health..."
if curl -f -s -o /dev/null -w "%{http_code}" -H "Host: skerritteconomics.com" http://localhost | grep -q "308"; then
    echo "✅ Site is responding correctly (redirecting to HTTPS)"
else
    echo "⚠️  Warning: Site may not be responding correctly"
fi

echo ""
echo "✅ Deployment complete!"
echo "🌐 Application running at https://skerritteconomics.com"
echo ""
echo "📊 Container status:"
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo "📝 To monitor logs: docker compose logs -f"
echo "🔄 To run this deployment again: ./deploy.sh"