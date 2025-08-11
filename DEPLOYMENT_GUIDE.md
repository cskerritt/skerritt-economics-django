# Deployment Guide - Skerritt Economics Website

## Quick Update Process

After SSHing into the AWS server, follow these steps to update the website with the latest code from GitHub:

```bash
# 1. Navigate to the project directory
cd /home/bitnami/skerritt-economics-django

# 2. Pull the latest changes from GitHub
git pull origin main

# 3. Rebuild and restart the Docker containers
sudo docker-compose down
sudo docker-compose build django
sudo docker-compose up -d

# 4. Run database migrations (if there are model changes)
sudo docker exec skerritt_django python manage.py migrate

# 5. Collect static files (if there are static file changes)
sudo docker exec skerritt_django python manage.py collectstatic --noinput

# 6. Verify the deployment
sudo docker-compose ps
curl -I http://localhost:80
```

## Detailed Step-by-Step Instructions

### Step 1: SSH into the AWS Server
```bash
ssh bitnami@54.243.84.130
# Or use your SSH key:
ssh -i your-key.pem bitnami@54.243.84.130
```

### Step 2: Navigate to Project Directory
```bash
cd /home/bitnami/skerritt-economics-django
```

### Step 3: Check Current Status
```bash
# Check git status
git status

# Check running containers
sudo docker-compose ps

# View recent logs
sudo docker-compose logs --tail=20
```

### Step 4: Pull Latest Code from GitHub
```bash
# Fetch and merge latest changes
git pull origin main

# If you have local changes that you want to keep:
git stash
git pull origin main
git stash pop

# If you want to discard local changes:
git fetch origin
git reset --hard origin/main
```

### Step 5: Update Docker Containers

#### Option A: Quick Restart (for small code changes)
```bash
sudo docker-compose restart django
```

#### Option B: Full Rebuild (for dependency or Dockerfile changes)
```bash
# Stop containers
sudo docker-compose down

# Rebuild the Django image
sudo docker-compose build django

# Start containers
sudo docker-compose up -d
```

### Step 6: Run Database Migrations
```bash
# Always run after pulling new code
sudo docker exec skerritt_django python manage.py migrate

# Check migration status
sudo docker exec skerritt_django python manage.py showmigrations
```

### Step 7: Update Static Files
```bash
# Collect static files
sudo docker exec skerritt_django python manage.py collectstatic --noinput
```

### Step 8: Verify Deployment
```bash
# Check container status
sudo docker-compose ps

# Test the health endpoint
sudo docker exec skerritt_django curl -f http://localhost:8000/health/

# Check the website
curl -I http://54.243.84.130

# View logs if there are issues
sudo docker-compose logs django --tail=50
sudo docker-compose logs caddy --tail=50
```

## Common Scenarios

### Scenario 1: Only Python Code Changed
```bash
cd /home/bitnami/skerritt-economics-django
git pull origin main
sudo docker-compose restart django
```

### Scenario 2: Requirements.txt Changed
```bash
cd /home/bitnami/skerritt-economics-django
git pull origin main
sudo docker-compose down
sudo docker-compose build django
sudo docker-compose up -d
sudo docker exec skerritt_django python manage.py migrate
```

### Scenario 3: Database Models Changed
```bash
cd /home/bitnami/skerritt-economics-django
git pull origin main
sudo docker-compose restart django
sudo docker exec skerritt_django python manage.py migrate
```

### Scenario 4: Static Files or Templates Changed
```bash
cd /home/bitnami/skerritt-economics-django
git pull origin main
sudo docker-compose restart django
sudo docker exec skerritt_django python manage.py collectstatic --noinput
```

### Scenario 5: Dockerfile or docker-compose.yml Changed
```bash
cd /home/bitnami/skerritt-economics-django
git pull origin main
sudo docker-compose down
sudo docker-compose build
sudo docker-compose up -d
sudo docker exec skerritt_django python manage.py migrate
sudo docker exec skerritt_django python manage.py collectstatic --noinput
```

## Troubleshooting

### Port 80 Already in Use
```bash
# Check what's using port 80
sudo netstat -tulpn | grep :80

# If Apache is running, stop it
sudo /opt/bitnami/apache/bin/httpd -k stop
```

### Container Won't Start
```bash
# Check logs
sudo docker-compose logs django
sudo docker-compose logs caddy

# Rebuild from scratch
sudo docker-compose down -v
sudo docker-compose build --no-cache
sudo docker-compose up -d
```

### Database Issues
```bash
# Create new migrations if needed
sudo docker exec skerritt_django python manage.py makemigrations

# Apply migrations
sudo docker exec skerritt_django python manage.py migrate

# Check database
sudo docker exec skerritt_django python manage.py dbshell
```

### Permission Issues
```bash
# Fix ownership if needed
sudo chown -R bitnami:bitnami /home/bitnami/skerritt-economics-django
```

## Environment Variables

The `.env` file contains sensitive configuration. Never commit this to git!

Key variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string

To update environment variables:
```bash
# Edit the .env file
nano .env

# Restart Django to apply changes
sudo docker-compose restart django
```

## Monitoring

### Check Container Health
```bash
sudo docker-compose ps
```

### View Real-time Logs
```bash
# All containers
sudo docker-compose logs -f

# Specific container
sudo docker-compose logs -f django
sudo docker-compose logs -f caddy
```

### Check Resource Usage
```bash
sudo docker stats
```

### Test Endpoints
```bash
# Health check
curl http://54.243.84.130/health/

# Homepage
curl -I http://54.243.84.130

# Admin panel
curl -I http://54.243.84.130/admin/
```

## Backup Procedures

### Database Backup
```bash
# Create backup
sudo docker exec skerritt_django python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Restore from backup
sudo docker exec skerritt_django python manage.py loaddata backup_20250811.json
```

### Full Project Backup
```bash
# Create tar archive
tar -czf skerritt_backup_$(date +%Y%m%d).tar.gz /home/bitnami/skerritt-economics-django
```

## Rollback Procedure

If an update causes issues:

```bash
# Check git log
git log --oneline -10

# Rollback to previous commit
git reset --hard HEAD~1
# Or to specific commit
git reset --hard <commit-hash>

# Rebuild and restart
sudo docker-compose down
sudo docker-compose build django
sudo docker-compose up -d
sudo docker exec skerritt_django python manage.py migrate
```

## Security Notes

1. Always use `sudo` for Docker commands
2. Keep the `.env` file secure and never commit it
3. Regularly update dependencies for security patches
4. Monitor logs for suspicious activity
5. Use HTTPS in production (configure domain DNS first)

## Contact & Support

For issues or questions about deployment:
1. Check the logs first: `sudo docker-compose logs`
2. Review this guide for common scenarios
3. Check GitHub issues for known problems

---

Last Updated: August 11, 2025