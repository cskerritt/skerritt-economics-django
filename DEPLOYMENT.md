# AWS Lightsail Deployment Guide

## Overview
This guide covers deploying the Skerritt Economics Django website to AWS Lightsail using Docker, Gunicorn, and Caddy.

## Architecture
- **Django**: Python web framework
- **Gunicorn**: WSGI HTTP Server
- **Caddy**: Reverse proxy with automatic HTTPS
- **Docker**: Containerization
- **AWS Lightsail**: $5/month hosting

## Prerequisites
- AWS account with Lightsail access
- Domain name (skerritteconomics.com)
- Basic Linux knowledge

## Step 1: Create Lightsail Instance

1. Log into AWS Lightsail Console
2. Create new instance:
   - Platform: Linux/Unix
   - Blueprint: Ubuntu 22.04 LTS
   - Instance Plan: $5/month (1 GB RAM, 1 vCPU, 40 GB SSD)
   - Name: skerritt-economics
3. Download SSH key for access

## Step 2: Configure DNS

1. In Lightsail, create static IP
2. Attach static IP to instance
3. Update domain DNS:
   - A record: @ -> Static IP
   - A record: www -> Static IP

## Step 3: Connect to Instance

```bash
# Using SSH
ssh -i your-key.pem ubuntu@your-static-ip

# Or use Lightsail browser-based SSH
```

## Step 4: Run Setup Script

```bash
# Download and run setup script
wget https://raw.githubusercontent.com/your-repo/lightsail-setup.sh
chmod +x lightsail-setup.sh
./lightsail-setup.sh
```

## Step 5: Deploy Application

### Option A: Git Clone
```bash
cd /opt/skerritt-economics
git clone https://github.com/your-username/skerritt-economics.git .
```

### Option B: Manual Upload
```bash
# From local machine
scp -r -i your-key.pem ./* ubuntu@your-ip:/opt/skerritt-economics/
```

## Step 6: Configure Environment

```bash
# Copy and edit environment file
cp .env.example .env
nano .env
```

Update these values:
```env
DJANGO_SECRET_KEY=generate-strong-key-here
DJANGO_ALLOWED_HOSTS=skerritteconomics.com,www.skerritteconomics.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Generate secret key:
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Step 7: Deploy

```bash
cd /opt/skerritt-economics
chmod +x deploy.sh
./deploy.sh
```

## Step 8: SSL Configuration

Caddy automatically handles SSL certificates via Let's Encrypt. Ensure:
1. DNS is properly configured
2. Ports 80 and 443 are open
3. Domain is accessible

## Monitoring

### View Logs
```bash
# All containers
docker-compose logs -f

# Django only
docker-compose logs -f django

# Caddy only
docker-compose logs -f caddy
```

### Check Status
```bash
docker-compose ps
```

### Resource Usage
```bash
htop
docker stats
```

## Maintenance

### Update Application
```bash
cd /opt/skerritt-economics
git pull origin main
./deploy.sh
```

### Backup Database
```bash
docker-compose exec django python manage.py dumpdata > backup.json
```

### Restore Database
```bash
docker-compose exec django python manage.py loaddata backup.json
```

### Clear Cache
```bash
docker-compose exec django python manage.py clear_cache
```

## Troubleshooting

### Container Won't Start
```bash
docker-compose logs django
docker-compose down
docker-compose up -d
```

### Static Files Not Loading
```bash
docker-compose exec django python manage.py collectstatic --noinput
docker-compose restart caddy
```

### Database Issues
```bash
docker-compose exec django python manage.py migrate
docker-compose exec django python manage.py makemigrations
```

### Permission Issues
```bash
sudo chown -R ubuntu:ubuntu /opt/skerritt-economics
sudo chmod -R 755 /opt/skerritt-economics
```

## Performance Optimization

### Enable Swap (for $5 instance)
```bash
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### Optimize Docker
```bash
# Prune unused images
docker system prune -a

# Limit container memory
# Edit docker-compose.yml and add memory limits
```

## Security

### Firewall Rules
```bash
sudo ufw status
sudo ufw allow 22/tcp   # SSH
sudo ufw allow 80/tcp   # HTTP
sudo ufw allow 443/tcp  # HTTPS
```

### Regular Updates
```bash
sudo apt update && sudo apt upgrade -y
docker-compose pull
```

### Change Default Passwords
1. Django admin password
2. Database password (if using PostgreSQL)
3. SSH keys

## Costs

- **Lightsail Instance**: $5/month
- **Static IP**: Free (1 per account)
- **Data Transfer**: 2TB included
- **Total**: ~$5/month

## Support

For issues or questions:
- Email: chris@skerritteconomics.com
- Documentation: /docs
- Logs: /opt/skerritt-economics/logs

## Quick Commands Reference

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View logs
docker-compose logs -f

# Django shell
docker-compose exec django python manage.py shell

# Run migrations
docker-compose exec django python manage.py migrate

# Create superuser
docker-compose exec django python manage.py createsuperuser

# Collect static files
docker-compose exec django python manage.py collectstatic --noinput
```