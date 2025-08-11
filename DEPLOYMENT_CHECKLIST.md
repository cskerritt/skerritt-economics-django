# Deployment Checklist - Economic Damages Calculator

## ✅ Completed Updates

### 1. **Economic Damages Calculator Implementation**
- ✅ Full Tinari Method (AEF/AIF) calculator
- ✅ User authentication system (login/register)
- ✅ PostgreSQL-ready database models
- ✅ CSV/JSON import/export functionality
- ✅ Scenario management system
- ✅ Calculation history tracking

### 2. **UI/UX Improvements**
- ✅ Simplified navigation menu (consolidated options)
- ✅ Added Calculator link to main navigation
- ✅ Added "Calculator Login" link in footer
- ✅ Removed "Estimated Damages" field from referral form

### 3. **Technical Updates**
- ✅ Updated requirements.txt with all dependencies
- ✅ Configured for SQLite (dev) and PostgreSQL (production)
- ✅ Added HTTPS protocol to all sitemaps
- ✅ All changes committed and pushed to GitHub

## 🚀 Production Deployment Steps

### 1. **Environment Variables**
Set these in your production environment:
```bash
USE_POSTGRES=True
DB_NAME=economic_damages
DB_USER=your_postgres_user
DB_PASSWORD=your_secure_password
DB_HOST=your_db_host
DB_PORT=5432
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=skerritteconomics.com,www.skerritteconomics.com
```

### 2. **Database Setup**
```bash
# Create PostgreSQL database
createdb economic_damages

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Server Configuration**
For production with Gunicorn:
```bash
gunicorn skerritt_site.wsgi:application \
    --workers 3 \
    --bind 0.0.0.0:8000 \
    --access-logfile - \
    --error-logfile -
```

### 5. **Nginx Configuration** (if applicable)
```nginx
location /calculator/ {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}

location /static/ {
    alias /path/to/staticfiles/;
}

location /media/ {
    alias /path/to/media/;
}
```

## 📍 Access Points

### Public Pages
- **Home**: https://skerritteconomics.com/
- **Calculator Login**: https://skerritteconomics.com/calculator/login/
- **Calculator Register**: https://skerritteconomics.com/calculator/register/

### Protected Pages (require login)
- **Calculator Dashboard**: https://skerritteconomics.com/calculator/
- **New Scenario**: https://skerritteconomics.com/calculator/new/
- **Admin Panel**: https://skerritteconomics.com/admin/

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure proper `ALLOWED_HOSTS`
- [ ] Enable HTTPS/SSL certificate
- [ ] Set up database backups
- [ ] Configure secure headers (HSTS, CSP, etc.)
- [ ] Set up monitoring/logging
- [ ] Configure rate limiting for login attempts

## 📊 Database Considerations

### PostgreSQL Production Setup
1. Create database and user with limited permissions
2. Use connection pooling for better performance
3. Set up regular automated backups
4. Monitor database performance

### Migration from SQLite to PostgreSQL
```bash
# Export data from SQLite
python manage.py dumpdata > data.json

# Switch to PostgreSQL (set USE_POSTGRES=True)
# Run migrations on PostgreSQL
python manage.py migrate

# Load data into PostgreSQL
python manage.py loaddata data.json
```

## 🔄 Updates Since Last Deployment

1. **New App**: Calculator app with full economic damages functionality
2. **New URLs**: 
   - `/calculator/` - Main calculator interface
   - `/calculator/login/` - Login page
   - `/calculator/register/` - Registration page
3. **New Dependencies**:
   - `psycopg2-binary==2.9.10` - PostgreSQL adapter
   - `python-dateutil==2.9.0.post0` - Date calculations
4. **UI Changes**:
   - Simplified navigation menu
   - Added Calculator link to navbar
   - Added Calculator Login link to footer
   - Removed Estimated Damages field from referral form

## 📝 Post-Deployment Testing

1. [ ] Verify home page loads
2. [ ] Test calculator login/registration
3. [ ] Create a test scenario
4. [ ] Run calculations
5. [ ] Export CSV/JSON
6. [ ] Test navigation links
7. [ ] Verify footer login link
8. [ ] Check sitemap generation
9. [ ] Test referral form submission
10. [ ] Verify admin panel access

## 🆘 Troubleshooting

### Common Issues
1. **500 Error**: Check `DEBUG=False` and static files
2. **Database Connection**: Verify PostgreSQL credentials
3. **Missing Static Files**: Run `collectstatic`
4. **Import Errors**: Install all requirements
5. **Permission Denied**: Check file/folder permissions

### Logs to Check
- Application logs
- Nginx/Apache error logs
- PostgreSQL logs
- Gunicorn logs

## 📞 Support

For deployment assistance or issues:
- Review code in `/calculator/` directory
- Check `CALCULATOR_README.md` for detailed documentation
- Database models in `/calculator/models.py`
- Calculation engine in `/calculator/calculations.py`

---

**Last Updated**: August 11, 2025
**Status**: Ready for Production Deployment
**GitHub**: All changes pushed to main branch