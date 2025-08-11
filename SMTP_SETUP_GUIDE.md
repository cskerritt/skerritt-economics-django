# SMTP Email Setup Guide for Production

This guide covers setting up email functionality for the Skerritt Economics Django website in production.

## Quick Setup Summary

1. Choose an email provider (Gmail, SendGrid, or Amazon SES)
2. Update `.env.production` with your credentials
3. Copy `.env.production` to your production server as `.env`
4. Restart your Django application

---

## Option 1: Gmail SMTP (Recommended for Small Volume)

**Best for:** Small to medium websites (< 500 emails/day)
**Cost:** Free for personal use, limited sending

### Setup Steps:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Create App Password:**
   - Go to Google Account settings → Security
   - Under "2-Step Verification" → App passwords
   - Generate password for "Mail"
   - Copy the 16-character password

3. **Update `.env.production`:**
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
DEFAULT_FROM_EMAIL=noreply@skerritteconomics.com
ADMIN_EMAIL=chris@skerritteconomics.com
```

4. **Gmail Limitations:**
   - 500 emails per day for free accounts
   - 2000 emails per day for Google Workspace accounts

---

## Option 2: SendGrid (Recommended for High Volume)

**Best for:** Professional websites with high email volume
**Cost:** Free tier (100 emails/day), paid plans available

### Setup Steps:

1. **Create SendGrid Account:**
   - Sign up at https://sendgrid.com/
   - Verify your domain (skerritteconomics.com)
   - Complete sender authentication

2. **Create API Key:**
   - Go to Settings → API Keys
   - Create new API key with "Mail Send" permissions
   - Copy the API key

3. **Update `.env.production`:**
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
DEFAULT_FROM_EMAIL=noreply@skerritteconomics.com
ADMIN_EMAIL=chris@skerritteconomics.com
```

4. **SendGrid Benefits:**
   - Professional deliverability
   - Detailed analytics
   - Template management
   - Unsubscribe handling

---

## Option 3: Amazon SES (Recommended for AWS)

**Best for:** Websites hosted on AWS
**Cost:** $0.10 per 1,000 emails

### Setup Steps:

1. **AWS SES Setup:**
   - Enable Amazon SES in AWS Console
   - Verify skerritteconomics.com domain
   - Request production access (removes sandbox limits)

2. **Create SMTP Credentials:**
   - Go to SES → SMTP Settings
   - Create SMTP credentials
   - Download credentials

3. **Update `.env.production`:**
```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-ses-smtp-username
EMAIL_HOST_PASSWORD=your-ses-smtp-password
DEFAULT_FROM_EMAIL=noreply@skerritteconomics.com
ADMIN_EMAIL=chris@skerritteconomics.com
```

---

## Production Deployment Steps

1. **Copy environment file to production server:**
```bash
cp .env.production .env
```

2. **Install required packages:**
```bash
pip install python-decouple
```

3. **Test email sending:**
```bash
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Test message', 'noreply@skerritteconomics.com', ['chris@skerritteconomics.com'])
```

4. **Restart your Django application**

---

## Email Templates Enhancement

The contact form will automatically send emails with this format:

**Subject:** "New Case Consultation Request - [Case Type]"

**Body:**
```
New consultation request received:

Name: [User Name]
Email: [User Email]
Phone: [User Phone]
Organization: [User Organization]

Case Type: [Case Type]
Jurisdiction: [Jurisdiction]
Timeline: [Timeline]

Case Details:
[User Message]

---
This inquiry was submitted on [Date/Time]
```

---

## Security Best Practices

1. **Never commit email credentials to Git**
2. **Use environment variables for all sensitive data**
3. **Enable HTTPS in production (SSL/TLS)**
4. **Set up SPF, DKIM, and DMARC records for your domain**
5. **Monitor email deliverability and bounce rates**

---

## Troubleshooting

### Common Issues:

1. **"Authentication failed" errors:**
   - Verify credentials are correct
   - Check if 2FA is enabled (Gmail)
   - Ensure app password is used (not regular password)

2. **Emails going to spam:**
   - Set up SPF record: `v=spf1 include:_spf.google.com ~all`
   - Configure DKIM signing
   - Use proper From address

3. **Rate limiting:**
   - Gmail: 500 emails/day limit
   - SendGrid: Check your plan limits
   - Add delays between bulk emails

### Testing Email Delivery:

```python
# Django shell test
python manage.py shell

from django.core.mail import send_mail
from django.conf import settings

# Test basic email
send_mail(
    'Test Email',
    'This is a test email from Skerritt Economics.',
    settings.DEFAULT_FROM_EMAIL,
    [settings.ADMIN_EMAIL],
    fail_silently=False,
)
```

---

## Recommended Setup for Skerritt Economics

**For immediate deployment:** Use **Gmail SMTP** (Option 1)
- Quick setup
- No additional costs
- Suitable for consultation requests

**For long-term/growth:** Use **SendGrid** (Option 2)
- Professional appearance
- Better deliverability
- Detailed analytics
- Can handle growth

Choose the option that best fits your current needs and budget!