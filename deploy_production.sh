#!/bin/bash
# Production Deployment Script for Skerritt Economics Django Website

echo "🚀 Skerritt Economics - Production Deployment Setup"
echo "=================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   print_error "This script should not be run as root"
   exit 1
fi

# Check if .env.production exists
if [ ! -f ".env.production" ]; then
    print_error ".env.production file not found!"
    echo "Please create .env.production with your production settings"
    echo "See SMTP_SETUP_GUIDE.md for configuration instructions"
    exit 1
fi

print_status "Found .env.production file"

# Backup existing .env if it exists
if [ -f ".env" ]; then
    cp .env .env.backup
    print_status "Backed up existing .env to .env.backup"
fi

# Copy production settings
cp .env.production .env
print_status "Copied production settings to .env"

# Install/update Python dependencies
print_status "Installing Python dependencies..."
pip install -r requirements.txt

# Run database migrations
print_status "Running database migrations..."
python manage.py migrate

# Collect static files
print_status "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if needed (optional)
echo ""
read -p "Do you want to create a Django superuser? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python manage.py createsuperuser
fi

# Test email configuration
echo ""
print_status "Testing email configuration..."
python test_email.py

echo ""
print_status "Production deployment setup complete!"
echo ""
print_warning "Important Next Steps:"
echo "1. Configure your web server (nginx/Apache) to serve the application"
echo "2. Set up SSL certificates for HTTPS"
echo "3. Configure your process manager (systemd/supervisor)"
echo "4. Update DNS records if needed"
echo "5. Test the contact form on your live site"
echo ""
echo "📄 See SMTP_SETUP_GUIDE.md for detailed email setup instructions"
echo "🌐 Your Django application is ready for production!"