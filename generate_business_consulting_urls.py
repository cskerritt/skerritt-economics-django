#!/usr/bin/env python
"""
Generate business consulting URLs for all cities in the database
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from main.city_data import CITY_DATA

def generate_business_consulting_urls():
    """Generate URLs for business consulting service for all cities"""
    
    urls = []
    total_cities = 0
    
    for state_slug, state_data in CITY_DATA.items():
        state_name = state_data['state_name']
        state_abbr = state_data['state_abbr'].lower()
        
        for city in state_data['cities']:
            city_slug = f"{city['slug']}-{state_abbr}"
            url_path = f"path('locations/business-consulting/{city_slug}.html', views.CityBusinessConsultingView.as_view(), name='business_consulting_{city_slug.replace('-', '_')}'),"
            urls.append(url_path)
            total_cities += 1
    
    print(f"Generated {total_cities} business consulting city URLs")
    
    # Write to a file
    with open('business_consulting_urls.py', 'w') as f:
        f.write("# Auto-generated business consulting city URLs\n")
        f.write("from django.urls import path\n")
        f.write("from . import views\n\n")
        f.write("business_consulting_city_urls = [\n")
        for url in urls:
            f.write(f"    {url}\n")
        f.write("]\n")
    
    print("URLs written to business_consulting_urls.py")
    
    # Also generate a list of all city URLs for testing
    test_urls = []
    for state_slug, state_data in CITY_DATA.items():
        state_abbr = state_data['state_abbr'].lower()
        for city in state_data['cities']:
            city_slug = f"{city['slug']}-{state_abbr}"
            test_urls.append(f"/locations/business-consulting/{city_slug}.html")
    
    return test_urls

if __name__ == "__main__":
    test_urls = generate_business_consulting_urls()
    
    # Print sample URLs for testing
    print("\nSample URLs for testing:")
    for url in test_urls[:5]:
        print(f"  https://skerritteconomics.com{url}")