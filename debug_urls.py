#!/usr/bin/env python3
"""
Debug URL patterns
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from django.urls import get_resolver
from main.city_urls import city_urlpatterns

def debug_urls():
    print(f"Total city URL patterns: {len(city_urlpatterns)}")
    
    # Check for NYC specifically
    nyc_patterns = [p for p in city_urlpatterns if 'new-york-city' in str(p.pattern)]
    print(f"\nNYC patterns found: {len(nyc_patterns)}")
    for p in nyc_patterns[:3]:
        print(f"  Pattern: {p.pattern}")
        print(f"  Name: {p.name}")
        print(f"  Kwargs: {p.default_args}")
    
    # Check routing
    from django.urls import resolve, reverse
    from django.urls.exceptions import Resolver404
    
    test_url = '/new-york/new-york-city/forensic-economist/'
    try:
        match = resolve(test_url)
        print(f"\nURL {test_url} resolved to:")
        print(f"  View: {match.func}")
        print(f"  Kwargs: {match.kwargs}")
    except Resolver404 as e:
        print(f"\nURL {test_url} NOT FOUND")
        print(f"  Error: {e}")
        
        # Try to find similar patterns
        print("\nSimilar patterns:")
        for p in city_urlpatterns[:10]:
            if 'new-york' in str(p.pattern):
                print(f"  {p.pattern}")

if __name__ == "__main__":
    debug_urls()