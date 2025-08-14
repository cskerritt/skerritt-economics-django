#!/usr/bin/env python3
"""
SEO Location Coverage Summary
Shows the complete SEO location coverage statistics
"""

from main.seo_location_system import (
    CORE_SERVICES,
    METRO_AREAS,
    US_STATES,
    MAJOR_COUNTIES
)
from main.expanded_city_data import EXPANDED_CITY_DATA
from main.missing_states_data import MISSING_STATES_DATA

def calculate_seo_coverage():
    """Calculate complete SEO coverage statistics"""
    
    # Count cities
    total_cities = 0
    cities_by_state = {}
    
    # From expanded data
    for state_slug, state_data in EXPANDED_CITY_DATA.items():
        city_count = len(state_data.get('cities', []))
        total_cities += city_count
        cities_by_state[state_slug] = city_count
    
    # From missing states
    for state_slug, state_data in MISSING_STATES_DATA.items():
        city_count = len(state_data.get('cities', []))
        total_cities += city_count
        cities_by_state[state_slug] = city_count
    
    # Calculate URLs
    url_counts = {
        'State Pages': len(US_STATES),
        'State + Service Combos': len(US_STATES) * len(CORE_SERVICES),
        'Metro Area Pages': len(METRO_AREAS),
        'Metro + Service Combos': len(METRO_AREAS) * len(CORE_SERVICES),
        'County Pages': len(MAJOR_COUNTIES),
        'County + Service Combos': len(MAJOR_COUNTIES) * len(CORE_SERVICES),
        'City + Service Combos (Top 200)': 200 * len(CORE_SERVICES),
    }
    
    total_urls = sum(url_counts.values())
    
    print("=" * 60)
    print("SEO LOCATION COVERAGE SUMMARY")
    print("=" * 60)
    print()
    
    print("GEOGRAPHIC COVERAGE:")
    print(f"  States: {len(US_STATES)} (all 50 states)")
    print(f"  Metro Areas: {len(METRO_AREAS)}")
    print(f"  Major Counties: {len(MAJOR_COUNTIES)}")
    print(f"  Total Cities: {total_cities}")
    print()
    
    print("SERVICE TYPES:")
    print(f"  Core Services: {len(CORE_SERVICES)}")
    for service in CORE_SERVICES:
        print(f"    - {service['title']}")
    print()
    
    print("URL GENERATION:")
    for category, count in url_counts.items():
        print(f"  {category}: {count:,}")
    print(f"  {'='*40}")
    print(f"  TOTAL URLS: {total_urls:,}")
    print()
    
    print("TOP STATES BY CITY COUNT:")
    sorted_states = sorted(cities_by_state.items(), key=lambda x: x[1], reverse=True)[:10]
    for state, count in sorted_states:
        state_name = US_STATES.get(state, {}).get('name', state.title())
        print(f"  {state_name}: {count} cities")
    print()
    
    print("COVERAGE BENEFITS:")
    print("  ✓ Complete US state coverage")
    print("  ✓ Major metropolitan areas covered")
    print("  ✓ Top counties by population included")
    print("  ✓ Service-location combinations for targeting")
    print("  ✓ Regional aggregation pages")
    print("  ✓ Scalable URL structure")
    print()
    
    print("SITEMAP INCLUSION:")
    sitemap_urls = (
        len(US_STATES) +  # State pages
        len(US_STATES) * 4 +  # State + top 4 services
        len(METRO_AREAS) +  # Metro pages
        len(METRO_AREAS) * 4 +  # Metro + top 4 services
        20 +  # Top 20 counties
        100 * 4  # Top 100 cities + top 4 services
    )
    print(f"  URLs in sitemap.xml: {sitemap_urls:,}")
    print(f"  (Limited to prevent sitemap bloat)")
    print()

if __name__ == '__main__':
    calculate_seo_coverage()