# Skerritt Economics & Consulting - Django Website

A professional Django web application for Skerritt Economics & Consulting, providing forensic economics and business valuation services.

## Features

- **Service Pages**: Detailed information about forensic economics, business valuation, vocational expert, and life care planning services
- **Practice Area Pages**: Specialized content for personal injury, medical malpractice, employment litigation, and commercial disputes
- **Blog System**: Articles & Insights section with categories and tags
- **Case Studies**: Detailed case study management and display
- **Contact Form**: Professional consultation request form with email notifications
- **Interactive Tools**: Six professional calculators for economic analysis
- **Location Pages**: SEO-optimized pages for New England states
- **Admin Panel**: Full content management system for easy updates

## Installation

1. Clone the repository:
```bash
cd skerritt_economics_django
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
- Copy `.env.example` to `.env` (if not already present)
- Update email settings and secret key for production

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Collect static files (for production):
```bash
python manage.py collectstatic
```

8. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
skerritt_economics_django/
├── skerritt_site/          # Main Django project settings
├── main/                   # Main app (home, services, contact)
├── blog/                   # Blog and case studies app
├── tools/                  # Interactive calculators app
├── templates/              # Base templates
├── static/                 # CSS, JavaScript, images
├── media/                  # User-uploaded files
└── manage.py              # Django management script
```

## Admin Access

Navigate to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

### Admin Features:
- **Blog Posts**: Create and manage articles with categories and tags
- **Case Studies**: Add detailed case study information
- **Contact Inquiries**: View and manage consultation requests
- **Testimonials**: Manage client testimonials
- **FAQs**: Update frequently asked questions

## Key URLs

- Home: `/`
- Services: `/services/<service-name>/`
- Practice Areas: `/practice-areas/<area-name>/`
- Blog: `/blog/`
- Tools: `/tools/`
- Contact: `/contact/`
- Admin: `/admin/`

## Interactive Tools

The site includes six professional calculators:
1. Life Expectancy Lookup Tool
2. Present Value Calculator
3. Wage Growth Projector
4. Household Services Valuation
5. Quick Business Valuation
6. Medical Cost Projector

These tools use client-side JavaScript for instant calculations.

## Deployment

For production deployment:

1. Set `DEBUG=False` in `.env`
2. Update `ALLOWED_HOSTS` with your domain
3. Configure proper email settings
4. Use a production-ready database (PostgreSQL recommended)
5. Serve with Gunicorn behind Nginx
6. Enable HTTPS with SSL certificates

### Gunicorn Example:
```bash
gunicorn skerritt_site.wsgi:application --bind 0.0.0.0:8000
```

## Content Migration

To migrate content from the static site:
1. Use Django admin to create blog posts
2. Add case studies through the admin panel
3. Configure testimonials and FAQs
4. Update service and practice area page templates with specific content

## Security Notes

- Keep `SECRET_KEY` secure and unique in production
- Enable CSRF protection (enabled by default)
- Configure secure headers in production
- Regular security updates for Django and dependencies

## Support

For questions or issues, contact the development team.

## License

Copyright © 2025 Skerritt Economics & Consulting. All rights reserved.