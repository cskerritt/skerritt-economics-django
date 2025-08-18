"""
Dynamic URL generator using data files to reduce code duplication
"""

from django.urls import path
from .utils import get_location_data, validate_unique_city_state_combinations

def generate_service_area_urls():
    """Generate service area URLs from data file"""
    from .service_area_views import (
        ServiceAreaVocationalExpertView,
        ServiceAreaForensicEconomistView,
        ServiceAreaLifeCarePlannerView,
        ServiceAreaBusinessValuationView
    )
    
    data = get_location_data()
    cities = data["cities"]
    
    # Validate for duplicates
    validate_unique_city_state_combinations(cities)
    
    urlpatterns = []
    view_map = {
        "vocational-expert": ServiceAreaVocationalExpertView,
        "forensic-economist": ServiceAreaForensicEconomistView,
        "life-care-planner": ServiceAreaLifeCarePlannerView,
        "business-valuation": ServiceAreaBusinessValuationView
    }
    
    for city_data in cities:
        for service_slug, view_class in view_map.items():
            urlpatterns.append(
                path(
                    f"{service_slug}/{city_data["city"]}-{city_data["state"]}/",
                    view_class.as_view(),
                    name=f"{service_slug.replace("-", "_")}_{city_data["city"]}_{city_data["state"]}",
                    kwargs={
                        "city": city_data["city"],
                        "state": city_data["state"],
                        "city_name": city_data["city_name"],
                        "state_name": city_data["state_name"]
                    }
                )
            )
    
    return urlpatterns

def generate_state_location_urls():
    """Generate state location URLs from data file"""
    from .location_hierarchy_views import StateLocationView
    
    data = get_location_data()
    states = data["states"]
    
    urlpatterns = []
    for state in states:
        urlpatterns.append(
            path(
                f"locations/states/{state["slug"]}/",
                StateLocationView.as_view(),
                name=f"location_state_{state["slug"]}",
                kwargs={
                    "state_slug": state["slug"],
                    "state_name": state["name"],
                    "state_abbr": state["abbr"]
                }
            )
        )
    
    return urlpatterns