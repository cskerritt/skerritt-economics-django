# Docker Commands for Django App Updates

## Quick Docker Update Commands (When GitHub Updates)

### 🚀 One-Command Update (Recommended)
```bash
cd /home/bitnami/skerritt-economics-django
./docker_update.sh
```

### 📋 Manual Step-by-Step Docker Commands

#### 1. Navigate to Project
```bash
cd /home/bitnami/skerritt-economics-django
```

#### 2. Pull Latest Code
```bash
git stash
git pull origin main
git stash pop  # if you have local changes
```

#### 3. Stop Current Containers
```bash
docker-compose down
```

#### 4. Rebuild Images (with latest code)
```bash
docker-compose build --no-cache
```

#### 5. Start New Containers
```bash
docker-compose up -d
```

#### 6. Run Database Migrations
```bash
docker-compose exec django python manage.py migrate
```

#### 7. Collect Static Files
```bash
docker-compose exec django python manage.py collectstatic --noinput
```

## Docker Management Commands

### Container Status
```bash
# Check running containers
docker-compose ps

# View all Docker containers
docker ps -a

# Check container health
docker-compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

### Logs and Debugging
```bash
# View all container logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f django
docker-compose logs -f caddy

# View last 50 lines of logs
docker-compose logs --tail=50

# Access Django container shell
docker-compose exec django bash

# Access Django management shell
docker-compose exec django python manage.py shell
```

### Database Operations
```bash
# Run migrations
docker-compose exec django python manage.py migrate

# Create superuser
docker-compose exec django python manage.py createsuperuser

# Access database shell
docker-compose exec django python manage.py dbshell

# Check migration status
docker-compose exec django python manage.py showmigrations
```

### Static Files and Media
```bash
# Collect static files
docker-compose exec django python manage.py collectstatic --noinput

# Force collect static files
docker-compose exec django python manage.py collectstatic --clear --noinput
```

### Container Maintenance
```bash
# Restart specific service
docker-compose restart django
docker-compose restart caddy

# Stop all containers
docker-compose down

# Stop and remove volumes (⚠️ DANGER: This removes database data)
docker-compose down -v

# Remove unused images and containers
docker system prune -f

# Remove all unused images
docker image prune -a -f
```

### Environment Variables
```bash
# Edit environment file
nano .env

# Restart containers after .env changes
docker-compose down && docker-compose up -d
```

### Health Checks
```bash
# Check if application is responding
curl http://localhost/
curl http://localhost/health/

# Check container health status
docker-compose exec django python manage.py check

# Test database connection
docker-compose exec django python manage.py check --database default
```

## Production Deployment Commands

### Initial Setup
```bash
# Build and start services for the first time
docker-compose up -d --build

# Create superuser
docker-compose exec django python manage.py createsuperuser

# Run initial data population (if you have fixtures)
docker-compose exec django python manage.py loaddata initial_data.json
```

### Backup and Restore
```bash
# Create backup directory
mkdir -p /home/bitnami/backups/$(date +%Y%m%d_%H%M%S)

# Backup database (if using PostgreSQL)
docker-compose exec postgres pg_dump -U username database_name > backup.sql

# Backup media files
docker-compose exec django tar -czf backup_media.tar.gz /app/media/

# Stop containers safely
docker-compose down --timeout 30
```

### Security Updates
```bash
# Update base images
docker-compose pull

# Rebuild with latest security patches
docker-compose build --pull --no-cache

# Restart with new images
docker-compose up -d
```

## Troubleshooting

### Common Issues
```bash
# If containers won't start
docker-compose logs

# If port conflicts
sudo netstat -tlnp | grep :80
sudo netstat -tlnp | grep :443

# If permission issues
docker-compose exec django ls -la /app/
docker-compose exec django whoami

# If database locked
docker-compose exec django python manage.py shell -c "
from django.db import connection
cursor = connection.cursor()
cursor.execute('SELECT 1')
print('Database connection OK')
"
```

### Reset Everything (Nuclear Option)
```bash
# ⚠️ WARNING: This removes all containers, images, and volumes
docker-compose down -v
docker system prune -a -f
docker volume prune -f

# Then rebuild everything
docker-compose up -d --build
```

## Monitoring and Performance

### Resource Usage
```bash
# Check Docker system usage
docker system df

# Monitor container resources
docker stats

# Check specific container resources
docker stats skerritt_django skerritt_caddy
```

### Performance Testing
```bash
# Test response time
time curl -s http://localhost/ > /dev/null

# Load testing (install apache2-utils first)
ab -n 100 -c 10 http://localhost/
```

## Cron Job for Auto-Updates

Add to crontab (`crontab -e`):
```bash
# Auto-update daily at 2 AM
0 2 * * * cd /home/bitnami/skerritt-economics-django && ./docker_update.sh >> /home/bitnami/update.log 2>&1

# Check container health every 5 minutes
*/5 * * * * cd /home/bitnami/skerritt-economics-django && docker-compose ps --quiet | wc -l | grep -q 2 || docker-compose up -d
```