# Quick Update Commands for Django App on AWS Lightsail

## Complete Update Process (Automated)
```bash
cd /home/bitnami/skerritt-economics-django
./update_from_github.sh
```

## Manual Step-by-Step Commands

### 1. Initial Boot/Login
```bash
ssh -i your-key.pem bitnami@your-lightsail-ip
```

### 2. Navigate to Project
```bash
cd /home/bitnami/skerritt-economics-django
```

### 3. Pull Latest Code from GitHub
```bash
git stash                    # Save any local changes
git pull origin main         # Pull latest changes
git stash pop                # Reapply local changes (if any)
```

### 4. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 5. Update Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run Database Migrations
```bash
python manage.py migrate
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Restart Application

#### If using Docker:
```bash
docker-compose down
docker-compose build
docker-compose up -d
```

#### If using Gunicorn directly:
```bash
sudo pkill gunicorn
gunicorn skerritt_site.wsgi:application --bind 0.0.0.0:8000 --workers 3 --daemon
```

#### If using systemd service:
```bash
sudo systemctl restart skerritt-economics
```

### 9. Restart Web Server (if applicable)
```bash
sudo systemctl restart apache2   # For Apache
# OR
sudo systemctl restart nginx     # For Nginx
```

### 10. Check Status
```bash
# Check if app is running
curl http://localhost:8000/health/

# Check logs
tail -f logs/error.log

# Check Docker logs (if using Docker)
docker-compose logs -f

# Check system service status
systemctl status skerritt-economics
```

## Quick One-Liner for Updates
```bash
cd /home/bitnami/skerritt-economics-django && git pull && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput && sudo systemctl restart skerritt-economics
```

## Setting Up Auto-Update with Cron (Optional)
```bash
# Edit crontab
crontab -e

# Add this line to auto-update daily at 2 AM
0 2 * * * /home/bitnami/skerritt-economics-django/update_from_github.sh >> /home/bitnami/update.log 2>&1
```

## Troubleshooting Commands

### Check Python/Django Version
```bash
python --version
python manage.py --version
```

### Check Running Processes
```bash
ps aux | grep gunicorn
ps aux | grep python
```

### Check Port Usage
```bash
sudo netstat -tlnp | grep :8000
sudo lsof -i :8000
```

### View Error Logs
```bash
# Django logs
tail -f /home/bitnami/skerritt-economics-django/logs/error.log

# System logs
sudo journalctl -u skerritt-economics -f

# Apache logs (if using)
sudo tail -f /opt/bitnami/apache2/logs/error_log
```

### Database Commands
```bash
# Create superuser
python manage.py createsuperuser

# Database shell
python manage.py dbshell

# Check migrations
python manage.py showmigrations
```

## Environment Variables
```bash
# Edit environment variables
nano .env

# Reload environment
source .env
```

## Rollback to Previous Version
```bash
# View commit history
git log --oneline -10

# Rollback to specific commit
git checkout <commit-hash>

# Or restore from backup
cp -r /home/bitnami/backups/<timestamp>/* /home/bitnami/skerritt-economics-django/
```