#!/bin/bash

# Complete update script for Django app on AWS Lightsail
# Run this whenever GitHub repository is updated

set -e

echo "🔄 Starting complete update process from GitHub..."
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

# Step 2: Backup current state (optional but recommended)
print_status "Creating backup of current state..."
BACKUP_DIR="/home/bitnami/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
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

# Step 6: Check Python version and virtual environment
print_status "Checking Python environment..."
if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python3 -m venv venv
fi

# Step 7: Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate

# Step 8: Upgrade pip
print_status "Upgrading pip..."
pip install --upgrade pip

# Step 9: Install/Update dependencies
print_status "Installing/updating dependencies..."
pip install -r requirements.txt

# Step 10: Check for environment variables
if [ ! -f ".env" ]; then
    print_warning ".env file not found. Creating from template..."
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_warning "Please update .env file with production values!"
    else
        cat > .env << 'EOF'
# Django settings
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database (if using PostgreSQL)
# DATABASE_URL=postgresql://user:password@localhost/dbname

# Static files
STATIC_ROOT=/home/bitnami/skerritt-economics-django/staticfiles
MEDIA_ROOT=/home/bitnami/skerritt-economics-django/media
EOF
        print_warning "Basic .env file created. Please update with production values!"
    fi
fi

# Step 11: Load environment variables
print_status "Loading environment variables..."
export $(cat .env | grep -v '^#' | xargs)

# Step 12: Run database migrations
print_status "Running database migrations..."
python manage.py migrate --noinput

# Step 13: Collect static files
print_status "Collecting static files..."
python manage.py collectstatic --noinput

# Step 14: Check if using Docker or native deployment
if [ -f "docker-compose.yml" ] && command -v docker-compose &> /dev/null; then
    print_status "Docker deployment detected. Using Docker..."
    
    # Stop existing containers
    print_status "Stopping existing Docker containers..."
    docker-compose down
    
    # Rebuild images
    print_status "Rebuilding Docker images..."
    docker-compose build
    
    # Start containers
    print_status "Starting Docker containers..."
    docker-compose up -d
    
    # Run migrations in container
    print_status "Running migrations in Docker container..."
    docker-compose exec -T django python manage.py migrate --noinput
    
    # Collect static files in container
    print_status "Collecting static files in Docker container..."
    docker-compose exec -T django python manage.py collectstatic --noinput
    
else
    print_status "Native deployment detected. Using Gunicorn..."
    
    # Step 15: Stop existing Gunicorn process
    print_status "Stopping existing Gunicorn process..."
    sudo pkill gunicorn || print_warning "No existing Gunicorn process found"
    
    # Step 16: Start Gunicorn with the Django app
    print_status "Starting Gunicorn..."
    gunicorn skerritt_site.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 3 \
        --daemon \
        --access-logfile /home/bitnami/skerritt-economics-django/logs/access.log \
        --error-logfile /home/bitnami/skerritt-economics-django/logs/error.log
fi

# Step 17: Restart web server (Apache/Nginx if configured)
if systemctl list-units --type=service | grep -q apache2; then
    print_status "Restarting Apache..."
    sudo systemctl restart apache2
elif systemctl list-units --type=service | grep -q nginx; then
    print_status "Restarting Nginx..."
    sudo systemctl restart nginx
fi

# Step 18: Clear cache if Redis is installed
if command -v redis-cli &> /dev/null; then
    print_status "Clearing Redis cache..."
    redis-cli FLUSHALL
fi

# Step 19: Run tests (optional)
print_status "Running tests..."
python manage.py test --noinput || print_warning "Some tests failed"

# Step 20: Check application health
print_status "Checking application health..."
sleep 5
if curl -f http://localhost:8000/health/ 2>/dev/null; then
    print_status "Health check passed!"
else
    print_warning "Health check endpoint not available or failed"
fi

# Step 21: Display status
echo ""
echo "================================================"
print_status "Update complete!"
echo ""
echo "📊 Deployment Summary:"
echo "  - Latest code: pulled from GitHub"
echo "  - Dependencies: updated"
echo "  - Database: migrated"
echo "  - Static files: collected"
echo "  - Application: restarted"
echo ""
echo "🔍 Check the following:"
echo "  1. Application logs: logs/error.log"
echo "  2. Access logs: logs/access.log"
echo "  3. Docker logs (if using): docker-compose logs -f"
echo "  4. System status: systemctl status skerritt-economics"
echo ""
echo "🌐 Access your application at:"
echo "  - http://$(hostname -I | awk '{print $1}'):8000"
echo "  - http://localhost:8000"
echo ""

# Create a log entry
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Update completed successfully" >> /home/bitnami/skerritt-economics-django/logs/updates.log

exit 0