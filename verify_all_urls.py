#!/usr/bin/env python3
"""
Verify that all city-service combination URLs are being generated
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from main.city_data import CITY_DATA, get_all_cities
from main.city_urls import city_urlpatterns

def verify_urls():
    print("=" * 80)
    print("URL VERIFICATION REPORT")
    print("=" * 80)
    
    # Calculate expected URLs
    services = ['forensic-economist', 'business-valuation', 'vocational-expert', 'life-care-planner']
    
    total_cities = sum(len(data['cities']) for data in CITY_DATA.values())
    expected_urls = total_cities * len(services)
    
    print(f"\n📊 EXPECTED COUNTS:")
    print(f"   States: {len(CITY_DATA)}")
    print(f"   Total Cities: {total_cities}")
    print(f"   Services per City: {len(services)}")
    print(f"   Expected Total URLs: {expected_urls}")
    
    # Count actual URLs generated
    actual_urls = len(city_urlpatterns)
    print(f"\n✅ ACTUAL URLS GENERATED: {actual_urls}")
    
    if actual_urls == expected_urls:
        print(f"   ✓ SUCCESS: All {expected_urls} URLs have been generated!")
    else:
        print(f"   ✗ ERROR: Missing {expected_urls - actual_urls} URLs")
    
    # Verify URL patterns by state
    print(f"\n📍 URL PATTERNS BY STATE:")
    print("-" * 40)
    
    for state_slug, state_data in CITY_DATA.items():
        state_name = state_data['state_name']
        state_abbr = state_data['state_abbr']
        cities_count = len(state_data['cities'])
        
        # Count URLs for this state
        state_urls = [p for p in city_urlpatterns if f'{state_slug}/' in str(p.pattern)]
        urls_count = len(state_urls)
        expected_state_urls = cities_count * len(services)
        
        status = "✓" if urls_count == expected_state_urls else "✗"
        print(f"{status} {state_name:20} ({state_abbr}): {urls_count:4} URLs ({cities_count} cities × 4 services)")
        
        if urls_count != expected_state_urls:
            print(f"   WARNING: Expected {expected_state_urls}, got {urls_count}")
    
    # Sample some specific URLs to verify format
    print(f"\n🔍 SAMPLE URL PATTERNS:")
    print("-" * 40)
    
    sample_states = ['alabama', 'california', 'new-york', 'texas', 'florida']
    for state in sample_states:
        if state in CITY_DATA:
            first_city = CITY_DATA[state]['cities'][0]
            print(f"\n{CITY_DATA[state]['state_name']}:")
            
            # Find URLs for this city
            city_patterns = [p for p in city_urlpatterns 
                           if f"{state}/{first_city['slug']}/" in str(p.pattern)]
            
            for pattern in city_patterns[:4]:  # Show all 4 services
                print(f"  /{pattern.pattern}")
    
    # Verify specific important cities
    print(f"\n🏙️ MAJOR CITIES VERIFICATION:")
    print("-" * 40)
    
    major_cities = [
        ('new-york', 'new-york-city', 'New York City'),
        ('california', 'los-angeles', 'Los Angeles'),
        ('illinois', 'chicago', 'Chicago'),
        ('texas', 'houston', 'Houston'),
        ('arizona', 'phoenix', 'Phoenix'),
        ('pennsylvania', 'philadelphia', 'Philadelphia'),
        ('texas', 'san-antonio', 'San Antonio'),
        ('california', 'san-diego', 'San Diego'),
        ('texas', 'dallas', 'Dallas'),
        ('california', 'san-jose', 'San Jose'),
    ]
    
    for state_slug, city_slug, city_name in major_cities:
        city_urls = [p for p in city_urlpatterns 
                    if f"{state_slug}/{city_slug}/" in str(p.pattern)]
        
        if len(city_urls) == 4:
            print(f"✓ {city_name:20} - All 4 service pages found")
        else:
            print(f"✗ {city_name:20} - Only {len(city_urls)} pages found")
    
    # List all unique URL patterns
    print(f"\n📋 UNIQUE URL PATTERN STRUCTURE:")
    print("-" * 40)
    
    # Get a sample URL for each service type
    sample_patterns = set()
    for pattern in city_urlpatterns[:20]:
        pattern_str = str(pattern.pattern)
        for service in services:
            if service in pattern_str:
                # Replace specific city/state with placeholders
                generic = pattern_str
                for state in CITY_DATA.keys():
                    generic = generic.replace(f"{state}/", "{state}/")
                generic = generic.split('/')[2:]  # Remove state/city part
                generic = "/{state}/{city}/" + "/".join(generic)
                sample_patterns.add(generic)
                break
    
    for pattern in sorted(sample_patterns):
        print(f"  {pattern}")
    
    print(f"\n{'=' * 80}")
    print(f"VERIFICATION COMPLETE")
    print(f"{'=' * 80}")
    
    return actual_urls == expected_urls

if __name__ == "__main__":
    success = verify_urls()
    sys.exit(0 if success else 1)