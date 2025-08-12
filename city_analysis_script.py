#!/usr/bin/env python3
"""
Script to analyze and merge city data files for comprehensive SEO expansion
"""

import sys
import os
import json
import re
from collections import defaultdict

# Add the main directory to Python path
sys.path.insert(0, '/home/bitnami/skerritt-economics-django/main')

def load_us_cities_seo_data():
    """Load cities from us_cities_seo_data.py"""
    try:
        from us_cities_seo_data import US_MAJOR_CITIES
        cities = []
        for slug, data in US_MAJOR_CITIES.items():
            # Create standardized format
            city = {
                'name': data['name'],
                'slug': slug,
                'state': data['state'],
                'state_abbr': data['state_abbr'],
                'county': data.get('county', ''),
                'population': str(data.get('population', '')),
                'lat': data.get('lat', 0.0),
                'lng': data.get('lng', 0.0),
                'metro_area': data.get('metro_area', ''),
                'region': data.get('region', ''),
                'source': 'us_cities_seo_data'
            }
            cities.append(city)
        print(f"Loaded {len(cities)} cities from us_cities_seo_data.py")
        return cities
    except Exception as e:
        print(f"Error loading us_cities_seo_data.py: {e}")
        return []

def load_city_data():
    """Load cities from city_data.py"""
    try:
        from city_data import CITY_DATA
        cities = []
        for state_slug, state_data in CITY_DATA.items():
            state_name = state_data['state_name']
            state_abbr = state_data['state_abbr']
            
            for city_info in state_data['cities']:
                city = {
                    'name': city_info['name'],
                    'slug': city_info['slug'],
                    'state': state_name,
                    'state_abbr': state_abbr,
                    'state_slug': state_slug,
                    'county': city_info.get('county', ''),
                    'population': str(city_info.get('population', '')),
                    'lat': city_info.get('lat', 0.0),
                    'lng': city_info.get('lng', 0.0),
                    'source': 'city_data'
                }
                cities.append(city)
        print(f"Loaded {len(cities)} cities from city_data.py")
        return cities
    except Exception as e:
        print(f"Error loading city_data.py: {e}")
        return []

def create_state_slug(state_name):
    """Create URL-friendly state slug"""
    return state_name.lower().replace(' ', '-')

def merge_cities(us_cities, city_data_cities):
    """Merge cities from both sources, avoiding duplicates"""
    merged = {}
    stats = {'duplicates': 0, 'new_from_us_cities': 0, 'existing_from_city_data': 0, 'enhanced': 0}
    
    # Add all cities from city_data first (existing coverage)
    for city in city_data_cities:
        key = f"{city['name']}_{city['state_abbr']}".lower()
        merged[key] = city
        stats['existing_from_city_data'] += 1
    
    # Add cities from us_cities_seo_data that aren't already included
    for city in us_cities:
        key = f"{city['name']}_{city['state_abbr']}".lower()
        if key not in merged:
            # Need to add state_slug for consistency
            city['state_slug'] = create_state_slug(city['state'])
            merged[key] = city
            stats['new_from_us_cities'] += 1
        else:
            # City exists, but enhance with additional data if available
            existing = merged[key]
            if city.get('metro_area') and not existing.get('metro_area'):
                existing['metro_area'] = city['metro_area']
            if city.get('region') and not existing.get('region'):
                existing['region'] = city['region']
            stats['duplicates'] += 1
            stats['enhanced'] += 1
    
    print(f"Merge Statistics:")
    print(f"  - Existing cities from city_data.py: {stats['existing_from_city_data']}")
    print(f"  - New cities from us_cities_seo_data.py: {stats['new_from_us_cities']}")
    print(f"  - Duplicates found and enhanced: {stats['duplicates']}")
    print(f"  - Total unique cities: {len(merged)}")
    
    return list(merged.values()), stats

def organize_by_state(cities):
    """Organize cities by state for the final data structure"""
    states = defaultdict(list)
    
    for city in cities:
        state_slug = city['state_slug']
        states[state_slug].append(city)
    
    # Sort cities within each state by name
    for state_cities in states.values():
        state_cities.sort(key=lambda x: x['name'])
    
    return dict(states)

def generate_expanded_city_data(organized_cities):
    """Generate the expanded_city_data.py file content"""
    content = '''"""
Comprehensive expanded city data for maximum SEO coverage
Merged from us_cities_seo_data.py (396 cities) and city_data.py (750 cities)
Total unique cities for complete US coverage
Auto-generated for SEO-optimized location pages
"""

EXPANDED_CITY_DATA = {
'''
    
    # Generate state sections
    for state_slug in sorted(organized_cities.keys()):
        cities = organized_cities[state_slug]
        if not cities:
            continue
            
        # Get state info from first city
        state_name = cities[0]['state']
        state_abbr = cities[0]['state_abbr']
        
        content += f'    "{state_slug}": {{\n'
        content += f'        "state_name": "{state_name}",\n'
        content += f'        "state_abbr": "{state_abbr}",\n'
        content += f'        "cities": [\n'
        
        # Add all cities for this state
        for i, city in enumerate(cities):
            content += '            {\n'
            content += f'                "name": "{city["name"]}",\n'
            content += f'                "slug": "{city["slug"]}",\n'
            content += f'                "population": "{city["population"]}",\n'
            content += f'                "county": "{city["county"]}",\n'
            content += f'                "lat": {city["lat"]},\n'
            content += f'                "lng": {city["lng"]}'
            
            # Add source and additional fields if available
            if city.get('metro_area'):
                content += f',\n                "metro_area": "{city["metro_area"]}"'
            if city.get('region'):
                content += f',\n                "region": "{city["region"]}"'
            
            content += '\n            }'
            if i < len(cities) - 1:
                content += ','
            content += '\n'
        
        content += '        ]\n'
        content += '    },\n'
    
    content += '''}

def get_all_expanded_cities():
    """Get all cities in a flat list for URL generation"""
    cities = []
    for state_slug, state_data in EXPANDED_CITY_DATA.items():
        for city_info in state_data['cities']:
            city = {
                'name': city_info['name'],
                'slug': city_info['slug'],
                'state': state_data['state_name'],
                'state_abbr': state_data['state_abbr'],
                'state_slug': state_slug,
                'county': city_info.get('county', ''),
                'population': city_info.get('population', ''),
                'lat': city_info.get('lat', 0.0),
                'lng': city_info.get('lng', 0.0),
                'metro_area': city_info.get('metro_area', ''),
                'region': city_info.get('region', '')
            }
            cities.append(city)
    return cities

def get_cities_by_state(state_slug):
    """Get all cities for a specific state"""
    if state_slug in EXPANDED_CITY_DATA:
        return EXPANDED_CITY_DATA[state_slug]['cities']
    return []

def get_city_by_slug(city_slug, state_slug):
    """Get specific city data by slug and state"""
    cities = get_cities_by_state(state_slug)
    for city in cities:
        if city['slug'] == city_slug:
            return city
    return None

def get_states_list():
    """Get list of all states with city data"""
    return [
        {
            'slug': state_slug,
            'name': state_data['state_name'],
            'abbr': state_data['state_abbr'],
            'city_count': len(state_data['cities'])
        }
        for state_slug, state_data in EXPANDED_CITY_DATA.items()
    ]
'''
    
    return content

def main():
    print("Starting comprehensive city data analysis and expansion...")
    print("=" * 60)
    
    # Load both city data sources
    us_cities = load_us_cities_seo_data()
    city_data_cities = load_city_data()
    
    if not us_cities and not city_data_cities:
        print("ERROR: Could not load any city data!")
        return
    
    # Merge cities avoiding duplicates
    all_cities, stats = merge_cities(us_cities, city_data_cities)
    
    # Organize by state
    organized_cities = organize_by_state(all_cities)
    
    # Generate expanded city data file
    expanded_content = generate_expanded_city_data(organized_cities)
    
    # Write the expanded city data file
    output_file = '/home/bitnami/skerritt-economics-django/main/expanded_city_data.py'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(expanded_content)
    
    print(f"\n✓ Created {output_file}")
    print(f"✓ Total states covered: {len(organized_cities)}")
    print(f"✓ Total unique cities: {len(all_cities)}")
    
    # Show breakdown by state
    print(f"\nState breakdown (top 10 by city count):")
    state_counts = [(state, len(cities)) for state, cities in organized_cities.items()]
    state_counts.sort(key=lambda x: x[1], reverse=True)
    
    for state, count in state_counts[:10]:
        print(f"  {state}: {count} cities")
    
    print(f"\nExpanded city data generation complete!")
    return all_cities, organized_cities

if __name__ == "__main__":
    main()