#!/bin/bash

# Docker-specific update script for Django app on AWS Lightsail
# Run this whenever GitHub repository is updated

set -e

echo "🐳 Starting Docker-based update process from GitHub..."
echo "================================================"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Step 1: Navigate to project directory
print_status "Navigating to project directory..."
cd /home/bitnami/skerritt-economics-django

# Step 2: Create backup of current state
print_status "Creating backup of current state..."
BACKUP_DIR="/home/bitnami/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
docker-compose down || print_warning "No existing containers to stop"
cp -r /home/bitnami/skerritt-economics-django "$BACKUP_DIR/" 2>/dev/null || print_warning "Backup skipped"

# Step 3: Stash any local changes
print_status "Stashing any local changes..."
git stash

# Step 4: Pull latest changes from GitHub
print_status "Pulling latest changes from GitHub..."
git pull origin main || git pull origin master

# Step 5: Apply stashed changes if needed
if git stash list | grep -q 'stash@{0}'; then
    print_warning "Attempting to apply stashed changes..."
    git stash pop || print_warning "Could not apply stashed changes automatically"
fi

# Step 6: Check for environment variables
if [ ! -f ".env" ]; then
    print_warning ".env file not found. Creating from template..."
    cat > .env << 'EOF'
# Django settings
DEBUG=False
SECRET_KEY=your-secret-key-here-change-this-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database settings (SQLite by default)
DATABASE_URL=sqlite:///db/db.sqlite3

# Static files
STATIC_ROOT=/app/staticfiles
MEDIA_ROOT=/app/media
EOF
    print_warning "Basic .env file created. Please update with production values!"
fi

# Step 7: Load environment variables
print_status "Loading environment variables..."
export $(cat .env | grep -v '^#' | xargs)

# Step 8: Stop existing containers
print_status "Stopping existing Docker containers..."
docker-compose down || print_warning "No existing containers to stop"

# Step 9: Remove old images (optional - saves space)
print_status "Cleaning up old Docker images..."
docker system prune -f || print_warning "Docker cleanup skipped"

# Step 10: Build new images
print_status "Building Docker images..."
docker-compose build --no-cache

# Step 11: Start new containers
print_status "Starting Docker containers..."
docker-compose up -d

# Step 12: Wait for containers to be healthy
print_status "Waiting for containers to start..."
sleep 30

# Step 13: Run database migrations inside container
print_status "Running database migrations..."
docker-compose exec -T django python manage.py migrate --noinput

# Step 14: Collect static files inside container
print_status "Collecting static files..."
docker-compose exec -T django python manage.py collectstatic --noinput

# Step 15: Create superuser if needed (optional)
print_status "Checking for superuser..."
docker-compose exec -T django python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@skerritteconomics.com', 'change-this-password')
    print('Superuser created')
else:
    print('Superuser already exists')
" || print_warning "Could not create superuser"

# Step 16: Check container health
print_status "Checking container health..."
docker-compose ps

# Step 17: Test application health
print_status "Testing application health..."
sleep 10
if curl -f http://localhost/health/ 2>/dev/null; then
    print_status "Health check passed!"
elif curl -f http://localhost:80/ 2>/dev/null; then
    print_status "Application is responding on port 80!"
else
    print_warning "Health check failed - check container logs"
fi

# Step 18: Show container logs (last 50 lines)
echo ""
echo "🔍 Recent container logs:"
echo "========================"
docker-compose logs --tail=50

# Step 19: Display status
echo ""
echo "================================================"
print_status "Docker update complete!"
echo ""
echo "📊 Deployment Summary:"
echo "  - Latest code: pulled from GitHub"
echo "  - Docker images: rebuilt"
echo "  - Containers: restarted"
echo "  - Database: migrated"
echo "  - Static files: collected"
echo ""
echo "🔍 Useful commands:"
echo "  - Check status: docker-compose ps"
echo "  - View logs: docker-compose logs -f"
echo "  - Access Django shell: docker-compose exec django python manage.py shell"
echo "  - Stop containers: docker-compose down"
echo ""
echo "🌐 Access your application at:"
echo "  - http://$(hostname -I | awk '{print $1}')"
echo "  - http://localhost"
echo ""

# Create a log entry
mkdir -p logs
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Docker update completed successfully" >> logs/updates.log

exit 0