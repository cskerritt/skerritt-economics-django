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
    The data file path can be configured via the LOCATION_DATA_FILE setting or environment variable.
    
    Returns:
        dict: Location data including states, cities, and services
    """
    # Try Django settings first, then environment variable, then default
    data_file = getattr(settings, "LOCATION_DATA_FILE", None) or \
                os.environ.get("LOCATION_DATA_FILE") or \
                os.path.join(
                    os.path.dirname(os.path.dirname(__file__)), 
                    "data", 
                    "locations.json"
                )
    with open(data_file, "r") as f:
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
            "slug": "forensic-economics",
            "name": "Forensic Economics",
            "description": "Economic damage calculations, lost earnings analysis, and expert testimony",
            "suffix_template": "for {location_context}"
        },
        {
            "slug": "business-valuation",
            "name": "Business Valuation",
            "description": "Professional business valuations for litigation, divorce, and partnership disputes",
            "suffix_template": "{location_phrase}"
        },
        {
            "slug": "life-care-planning",
            "name": "Life Care Planning",
            "description": "Comprehensive life care plans and future medical cost projections",
            "suffix_template": "for {case_context}"
        },
        {
            "slug": "vocational-expert",
            "name": "Vocational Assessment",
            "description": "Earning capacity evaluations and employability determinations",
            "suffix_template": "for {disability_context}"
        }
    ]

def clear_cache():
    """
    Clear the cached data (useful for testing or data updates).
    
    WARNING: This should only be used in development/testing environments.
    In production, cache invalidation happens automatically when the process restarts.
    
    Raises:
        RuntimeError: If DEBUG is False (production mode)
    """
    if not getattr(settings, "DEBUG", False):
        raise RuntimeError(
            "Cache clearing is disabled in production. "
            "The cache will be automatically cleared on process restart."
        )
    
    get_location_data.cache_clear()
    get_services_config.cache_clear()