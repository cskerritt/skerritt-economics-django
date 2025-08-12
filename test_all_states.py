#!/usr/bin/env python3
"""
Test that all state city pages are accessible
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from main.city_data import CITY_DATA, get_all_cities

def test_city_data():
    print("City Data Statistics:")
    print(f"Total states: {len(CITY_DATA)}")
    
    total_cities = 0
    for state, data in CITY_DATA.items():
        cities_count = len(data['cities'])
        total_cities += cities_count
        print(f"  {data['state_name']} ({data['state_abbr']}): {cities_count} cities")
    
    print(f"\nTotal cities across all states: {total_cities}")
    print(f"Total pages (4 services per city): {total_cities * 4}")
    
    # Test get_all_cities function
    all_cities = get_all_cities()
    print(f"\nget_all_cities() returned: {len(all_cities)} cities")
    
    # Sample some URLs that would be generated
    print("\nSample URLs that will be generated:")
    services = ['forensic-economist', 'business-valuation', 'vocational-expert', 'life-care-planner']
    
    sample_states = ['alabama', 'california', 'new-york', 'texas', 'florida']
    for state in sample_states:
        if state in CITY_DATA:
            state_data = CITY_DATA[state]
            first_city = state_data['cities'][0]
            for service in services:
                url = f"/{state}/{first_city['slug']}/{service}/"
                print(f"  {url}")
            print()

if __name__ == "__main__":
    test_city_data()