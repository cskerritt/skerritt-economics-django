#!/usr/bin/env python3
"""
Generate comprehensive city data for all 50 US states
"""

import json
from main.us_cities_data import US_STATES

# Population estimates and county data for major cities
CITY_METADATA = {
    'AL': {
        'Birmingham': {'pop': '209403', 'county': 'Jefferson County', 'lat': 33.5186, 'lng': -86.8104},
        'Montgomery': {'pop': '198525', 'county': 'Montgomery County', 'lat': 32.3668, 'lng': -86.3000},
        'Huntsville': {'pop': '215006', 'county': 'Madison County', 'lat': 34.7304, 'lng': -86.5861},
        'Mobile': {'pop': '187041', 'county': 'Mobile County', 'lat': 30.6954, 'lng': -88.0399},
        'Tuscaloosa': {'pop': '101129', 'county': 'Tuscaloosa County', 'lat': 33.2098, 'lng': -87.5692},
        'Hoover': {'pop': '92606', 'county': 'Jefferson County', 'lat': 33.4054, 'lng': -86.8114},
        'Dothan': {'pop': '71072', 'county': 'Houston County', 'lat': 31.2232, 'lng': -85.3905},
        'Auburn': {'pop': '76143', 'county': 'Lee County', 'lat': 32.6099, 'lng': -85.4808},
        'Decatur': {'pop': '57938', 'county': 'Morgan County', 'lat': 34.6059, 'lng': -86.9833},
        'Madison': {'pop': '56933', 'county': 'Madison County', 'lat': 34.6993, 'lng': -86.7483},
        'Florence': {'pop': '40184', 'county': 'Lauderdale County', 'lat': 34.7998, 'lng': -87.6773},
        'Gadsden': {'pop': '33945', 'county': 'Etowah County', 'lat': 34.0143, 'lng': -86.0066},
        'Prattville': {'pop': '37781', 'county': 'Autauga County', 'lat': 32.4640, 'lng': -86.4597},
        'Vestavia Hills': {'pop': '39102', 'county': 'Jefferson County', 'lat': 33.4488, 'lng': -86.7877},
        'Phenix City': {'pop': '38816', 'county': 'Russell County', 'lat': 32.4710, 'lng': -85.0008},
    },
    # Add more states as needed - for now focusing on structure
}

def generate_slug(city_name):
    """Generate URL-friendly slug from city name"""
    return city_name.lower().replace(' ', '-').replace("'", '').replace('.', '')

def generate_state_data():
    """Generate comprehensive city data for all states"""
    all_states_data = {}
    
    for state_abbr, state_info in US_STATES.items():
        state_name = state_info['name']
        state_slug = state_name.lower().replace(' ', '-')
        
        cities_data = []
        for city_name in state_info['cities']:
            city_slug = generate_slug(city_name)
            
            # Get metadata if available, otherwise use defaults
            metadata = CITY_METADATA.get(state_abbr, {}).get(city_name, {})
            
            city_data = {
                'name': city_name,
                'slug': city_slug,
                'population': metadata.get('pop', '50000'),  # Default population
                'county': metadata.get('county', f'{city_name} County'),  # Default county
                'lat': metadata.get('lat', 40.0),  # Default latitude
                'lng': metadata.get('lng', -95.0),  # Default longitude
            }
            cities_data.append(city_data)
        
        all_states_data[state_slug] = {
            'state_name': state_name,
            'state_abbr': state_abbr,
            'cities': cities_data
        }
    
    return all_states_data

def write_city_data_file(data):
    """Write the complete city data to a Python file"""
    output = '''"""
Comprehensive city data for all 50 US states
Auto-generated for SEO-optimized location pages
"""

CITY_DATA = '''
    
    output += json.dumps(data, indent=4)
    output = output.replace('true', 'True').replace('false', 'False').replace('null', 'None')
    
    # Add helper functions
    output += '''

def get_all_cities():
    """Get all cities across all states"""
    all_cities = []
    for state, data in CITY_DATA.items():
        for city in data['cities']:
            city_info = city.copy()
            city_info['state'] = state
            city_info['state_name'] = data['state_name']
            city_info['state_abbr'] = data['state_abbr']
            all_cities.append(city_info)
    return all_cities

def get_city_by_slug(city_slug, state_slug=None):
    """Get city data by slug"""
    for state, data in CITY_DATA.items():
        if state_slug and state != state_slug:
            continue
        for city in data['cities']:
            if city['slug'] == city_slug:
                city_info = city.copy()
                city_info['state'] = state
                city_info['state_name'] = data['state_name']
                city_info['state_abbr'] = data['state_abbr']
                return city_info
    return None

def get_state_cities(state_slug):
    """Get all cities for a specific state"""
    if state_slug in CITY_DATA:
        data = CITY_DATA[state_slug]
        cities = []
        for city in data['cities']:
            city_info = city.copy()
            city_info['state'] = state_slug
            city_info['state_name'] = data['state_name']
            city_info['state_abbr'] = data['state_abbr']
            cities.append(city_info)
        return cities
    return []

def get_total_pages():
    """Calculate total number of pages that will be generated"""
    services = ['forensic-economist', 'business-valuation', 'vocational-expert', 'life-care-planner']
    total_cities = sum(len(data['cities']) for data in CITY_DATA.values())
    return total_cities * len(services)
'''
    
    with open('main/city_data_all_states.py', 'w') as f:
        f.write(output)
    
    print(f"Generated city data file with {len(data)} states")
    total_cities = sum(len(state['cities']) for state in data.values())
    print(f"Total cities: {total_cities}")
    print(f"Total potential pages (4 services per city): {total_cities * 4}")

if __name__ == "__main__":
    data = generate_state_data()
    write_city_data_file(data)
    
    # Show sample data
    print("\nSample data for first 3 states:")
    for i, (state, info) in enumerate(data.items()):
        if i >= 3:
            break
        print(f"\n{info['state_name']} ({info['state_abbr']}):")
        for j, city in enumerate(info['cities'][:3]):
            print(f"  - {city['name']} ({city['slug']})")