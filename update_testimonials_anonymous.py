#!/usr/bin/env python
"""
Update existing testimonials to be anonymous
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from main.models import Testimonial

def update_testimonials():
    """Update testimonials to be anonymous"""
    
    updates = [
        {
            'old_author': 'Sarah Mitchell',
            'new_author': 'Attorney',
            'new_title': 'Personal Injury Law Firm'
        },
        {
            'old_author': 'Robert Chen', 
            'new_author': 'Senior Attorney',
            'new_title': 'Commercial Litigation Practice'
        },
        {
            'old_author': 'Jennifer Walsh',
            'new_author': 'Law Firm Partner',
            'new_title': 'Medical Malpractice Firm'
        },
        {
            'old_author': 'John Davis',
            'new_author': 'Senior Attorney',
            'new_title': 'Commercial Litigation Firm'
        },
        {
            'old_author': 'Michael Chen',
            'new_author': 'Managing Partner',
            'new_title': 'Employment Law Practice'
        }
    ]
    
    for update in updates:
        try:
            testimonial = Testimonial.objects.get(author=update['old_author'])
            testimonial.author = update['new_author']
            testimonial.title = update['new_title']
            testimonial.save()
            print(f"Updated testimonial: {update['old_author']} -> {update['new_author']}")
        except Testimonial.DoesNotExist:
            print(f"Testimonial not found for: {update['old_author']}")
        except Exception as e:
            print(f"Error updating {update['old_author']}: {e}")

if __name__ == '__main__':
    print("Updating testimonials to be anonymous...")
    update_testimonials()
    print("Update complete!")