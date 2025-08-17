"""
Cached data loader for location and service configurations
"""

import json
import os
from functools import lru_cache
from django.conf import settings

@lru_cache(maxsize=1)
def get_location_data():
    """
    Load and cache location data from JSON file.
    Uses LRU cache to avoid repeated file reads.
    
    Returns:
        dict: Location data including states, cities, and services
    """
    data_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 
        'data', 
        'locations.json'
    )
    with open(data_file, 'r') as f:
        return json.load(f)

@lru_cache(maxsize=1)
def get_services_config():
    """
    Get cached services configuration.
    
    Returns:
        list: List of service configurations
    """
    return [
        {
            'slug': 'forensic-economics',
            'name': 'Forensic Economics',
            'description': 'Economic damage calculations, lost earnings analysis, and expert testimony',
            'template_key': 'forensic_economics'
        },
        {
            'slug': 'business-valuation',
            'name': 'Business Valuation',
            'description': 'Professional business valuations for litigation, divorce, and partnership disputes',
            'template_key': 'business_valuation'
        },
        {
            'slug': 'life-care-planning',
            'name': 'Life Care Planning',
            'description': 'Comprehensive life care plans and future medical cost projections',
            'template_key': 'life_care_planning'
        },
        {
            'slug': 'vocational-expert',
            'name': 'Vocational Assessment',
            'description': 'Earning capacity evaluations and employability determinations',
            'template_key': 'vocational_assessment'
        }
    ]

def clear_cache():
    """
    Clear the cached data (useful for testing or data updates).
    """
    get_location_data.cache_clear()
    get_services_config.cache_clear()