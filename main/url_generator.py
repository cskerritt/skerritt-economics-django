"""
Dynamic URL generator using data files to reduce code duplication
"""

import json
import os
from django.urls import path

def load_location_data():
    """Load location data from JSON file"""
    data_file = os.path.join(os.path.dirname(__file__), 'data', 'locations.json')
    with open(data_file, 'r') as f:
        return json.load(f)

def generate_service_area_urls():
    """Generate service area URLs from data file"""
    from .service_area_views import (
        ServiceAreaVocationalExpertView,
        ServiceAreaForensicEconomistView,
        ServiceAreaLifeCarePlannerView,
        ServiceAreaBusinessValuationView
    )
    
    data = load_location_data()
    cities = data['cities']
    
    # Validate for duplicates
    seen_combinations = set()
    for city_data in cities:
        combo_key = (city_data['city'], city_data['state'])
        if combo_key in seen_combinations:
            raise ValueError(f"Duplicate city-state combination: {combo_key}")
        seen_combinations.add(combo_key)
    
    urlpatterns = []
    view_map = {
        'vocational-expert': ServiceAreaVocationalExpertView,
        'forensic-economist': ServiceAreaForensicEconomistView,
        'life-care-planner': ServiceAreaLifeCarePlannerView,
        'business-valuation': ServiceAreaBusinessValuationView
    }
    
    for city_data in cities:
        for service_slug, view_class in view_map.items():
            urlpatterns.append(
                path(
                    f'{service_slug}/{city_data["city"]}-{city_data["state"]}/',
                    view_class.as_view(),
                    name=f'{service_slug.replace("-", "_")}_{city_data["city"]}_{city_data["state"]}',
                    kwargs={
                        'city': city_data['city'],
                        'state': city_data['state'],
                        'city_name': city_data['city_name'],
                        'state_name': city_data['state_name']
                    }
                )
            )
    
    return urlpatterns

def generate_state_location_urls():
    """Generate state location URLs from data file"""
    from .location_hierarchy_views import StateLocationView
    
    data = load_location_data()
    states = data['states']
    
    urlpatterns = []
    for state in states:
        urlpatterns.append(
            path(
                f'locations/states/{state["slug"]}/',
                StateLocationView.as_view(),
                name=f'location_state_{state["slug"]}',
                kwargs={
                    'state_slug': state['slug'],
                    'state_name': state['name'],
                    'state_abbr': state['abbr']
                }
            )
        )
    
    return urlpatterns