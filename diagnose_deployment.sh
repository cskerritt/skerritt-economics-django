#!/bin/bash

# Diagnostic script to identify deployment issues
echo "🔍 Running deployment diagnostics..."
echo "================================="

# Check current directory
echo "📁 Current directory:"
pwd
echo ""

# Check if .env file exists and has required variables
echo "🔐 Environment file check:"
if [ -f ".env" ]; then
    echo "✅ .env file exists"
    # Check for critical variables
    if grep -q "DJANGO_SECRET_KEY=" .env; then
        echo "✅ DJANGO_SECRET_KEY is set"
    else
        echo "❌ DJANGO_SECRET_KEY is missing!"
    fi
    if grep -q "DJANGO_SETTINGS_MODULE=" .env; then
        echo "✅ DJANGO_SETTINGS_MODULE is set"
        grep "DJANGO_SETTINGS_MODULE=" .env
    else
        echo "❌ DJANGO_SETTINGS_MODULE is missing!"
    fi
else
    echo "❌ .env file not found!"
fi
echo ""

# Check Python and Django
echo "🐍 Python/Django check:"
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "✅ Virtual environment activated"
    python --version
    
    # Try to check Django settings
    echo "Testing Django configuration..."
    python manage.py check --deploy 2>&1 | head -20 || echo "Django check failed"
    
    # Check if database is accessible
    echo ""
    echo "Testing database connection..."
    python manage.py showmigrations --plan | head -5 2>&1 || echo "Database connection failed"
else
    echo "⚠️ No virtual environment found"
fi
echo ""

# Check for running services
echo "🔧 Service status:"
if systemctl is-active --quiet skerritt-economics; then
    echo "✅ skerritt-economics service is running"
    sudo journalctl -u skerritt-economics -n 10 --no-pager
elif systemctl is-active --quiet gunicorn; then
    echo "✅ gunicorn service is running"
    sudo journalctl -u gunicorn -n 10 --no-pager
else
    echo "⚠️ No application service found running"
fi
echo ""

# Check nginx
if systemctl is-active --quiet nginx; then
    echo "✅ nginx is running"
    # Check nginx error log
    echo "Recent nginx errors:"
    sudo tail -n 10 /var/log/nginx/error.log 2>/dev/null || echo "No nginx error log found"
else
    echo "⚠️ nginx is not running"
fi
echo ""

# Check Docker if available
if command -v docker &> /dev/null && [ -f "docker-compose.yml" ]; then
    echo "🐳 Docker status:"
    docker compose ps || docker-compose ps
    echo ""
    
    # Check Django container specifically
    echo "Django container status:"
    docker compose ps django || docker-compose ps django
    echo ""
    
    echo "Recent Django container logs:"
    docker compose logs --tail=30 django 2>&1 || docker-compose logs --tail=30 django 2>&1
    echo ""
    
    echo "Recent Caddy container logs:"
    docker compose logs --tail=20 caddy 2>&1 || docker-compose logs --tail=20 caddy 2>&1
    echo ""
    
    # Check if containers are healthy
    echo "Container health status:"
    docker ps --format "table {{.Names}}\t{{.Status}}" | grep skerritt || echo "No skerritt containers found"
fi
echo ""

# Check if application is responding
echo "🌐 Application response check:"
for PORT in 8000 80 3000; do
    response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:$PORT" 2>/dev/null || echo "000")
    echo "Port $PORT: HTTP $response"
    if [ "$response" = "500" ]; then
        echo "Attempting to get error details from port $PORT:"
        curl -s "http://localhost:$PORT" 2>&1 | head -20 || echo "Could not retrieve error page"
    fi
done
echo ""

echo "🔍 Diagnostics complete!"
echo "================================="