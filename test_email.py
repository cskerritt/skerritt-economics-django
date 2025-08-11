#!/usr/bin/env python3
"""
Email Testing Script for Skerritt Economics Django Website
Run this script to test email functionality after setting up SMTP credentials.
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from main.models import ContactInquiry

def test_basic_email():
    """Test basic email sending functionality"""
    print("🔧 Testing basic email functionality...")
    
    try:
        result = send_mail(
            subject='Test Email - Skerritt Economics',
            message='This is a test email to verify SMTP configuration is working properly.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        
        if result:
            print("✅ Basic email test: PASSED")
            return True
        else:
            print("❌ Basic email test: FAILED - No error but email not sent")
            return False
            
    except Exception as e:
        print(f"❌ Basic email test: FAILED - {str(e)}")
        return False

def test_contact_form_email():
    """Test contact form email format"""
    print("🔧 Testing contact form email format...")
    
    try:
        # Create a test inquiry
        test_inquiry = ContactInquiry(
            name="Test User",
            email="test@example.com",
            phone="(555) 123-4567", 
            organization="Test Law Firm",
            case_type="personal_injury",
            jurisdiction="state_court",
            timeline="soon",
            case_details="This is a test inquiry to verify email formatting."
        )
        
        # Prepare email (same format as in ContactView)
        subject = f"New Case Consultation Request - {test_inquiry.get_case_type_display()}"
        message = f"""
        New consultation request received:
        
        Name: {test_inquiry.name}
        Email: {test_inquiry.email}
        Phone: {test_inquiry.phone}
        Organization: {test_inquiry.organization or 'Not provided'}
        
        Case Type: {test_inquiry.get_case_type_display()}
        Jurisdiction: {test_inquiry.get_jurisdiction_display()}
        Timeline: {test_inquiry.get_timeline_display()}
        
        Case Details:
        {test_inquiry.case_details}
        
        ---
        This inquiry was submitted as a test email
        """
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
            reply_to=[test_inquiry.email]
        )
        
        result = email.send()
        
        if result:
            print("✅ Contact form email test: PASSED")
            return True
        else:
            print("❌ Contact form email test: FAILED - No error but email not sent")
            return False
            
    except Exception as e:
        print(f"❌ Contact form email test: FAILED - {str(e)}")
        return False

def show_email_settings():
    """Display current email configuration"""
    print("📧 Current Email Configuration:")
    print(f"   EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    print(f"   EMAIL_HOST: {settings.EMAIL_HOST}")
    print(f"   EMAIL_PORT: {settings.EMAIL_PORT}")
    print(f"   EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    print(f"   EMAIL_HOST_USER: {settings.EMAIL_HOST_USER or '(not set)'}")
    print(f"   EMAIL_HOST_PASSWORD: {'(set)' if settings.EMAIL_HOST_PASSWORD else '(not set)'}")
    print(f"   DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
    print(f"   ADMIN_EMAIL: {settings.ADMIN_EMAIL}")
    print()

def main():
    """Run all email tests"""
    print("🚀 Skerritt Economics - Email Configuration Test")
    print("=" * 50)
    
    # Show current configuration
    show_email_settings()
    
    # Check if using console backend
    if 'console' in settings.EMAIL_BACKEND.lower():
        print("⚠️  WARNING: Using console email backend")
        print("   Emails will be printed to console instead of sent")
        print("   Update EMAIL_BACKEND in .env for production")
        print()
    
    # Run tests
    basic_test = test_basic_email()
    form_test = test_contact_form_email()
    
    # Summary
    print()
    print("📊 Test Summary:")
    print(f"   Basic Email: {'✅ PASSED' if basic_test else '❌ FAILED'}")
    print(f"   Contact Form Email: {'✅ PASSED' if form_test else '❌ FAILED'}")
    
    if basic_test and form_test:
        print()
        print("🎉 All email tests passed! Your SMTP configuration is working correctly.")
        print("   Contact form submissions will now send email notifications.")
    else:
        print()
        print("❌ Some email tests failed. Please check your SMTP configuration.")
        print("   See SMTP_SETUP_GUIDE.md for detailed setup instructions.")

if __name__ == "__main__":
    main()