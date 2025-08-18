#!/bin/bash

# Deployment script for AWS Lightsail
# This script builds and deploys the Django application with Docker

set -e

echo "🚀 Starting deployment to AWS Lightsail..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Build Docker images
echo "📦 Building Docker images..."
docker-compose build

# Stop existing containers
echo "🛑 Stopping existing containers..."
docker-compose down

# Start new containers
echo "🚀 Starting new containers..."
docker-compose up -d

# Run migrations
echo "🔄 Running database migrations..."
docker-compose exec django python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
docker-compose exec django python manage.py collectstatic --noinput

# Create superuser if needed
echo "👤 Checking for superuser..."
docker-compose exec django python manage.py shell -c "
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
sleep 5
curl -f http://localhost/health/ || echo "Health check endpoint not configured"

echo "✅ Deployment complete!"
echo "🌐 Application running at http://localhost"
echo ""
echo "📝 Next steps:"
echo "1. Configure your domain DNS to point to this server"
echo "2. Update .env file with production values"
echo "3. Change the default admin password"
echo "4. Monitor logs with: docker-compose logs -f"