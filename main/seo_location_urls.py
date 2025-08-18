"""
SEO Location URLs Configuration
Generates comprehensive location-based URL patterns
"""

from django.urls import path, include
from . import seo_location_views
from .seo_location_system import (
    SEO_LOCATION_DATA,
    CORE_SERVICES,
    METRO_AREAS,
    US_STATES,
    MAJOR_COUNTIES
)
from .expanded_city_data import EXPANDED_CITY_DATA
from .missing_states_data import MISSING_STATES_DATA

def generate_all_location_urls():
    """Generate all location-based URL patterns"""
    urlpatterns = []
    
    # State-level pages
    for state_slug, state_data in US_STATES.items():
        urlpatterns.append(
            path(f'forensic-economist-{state_slug}/', 
                 seo_location_views.state_page, 
                 {'state_slug': state_slug},
                 name=f'state-{state_slug}')
        )
        
        # State + Service combinations
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f"{service['slug']}-{state_slug}/", 
                     seo_location_views.state_service_page,
                     {'state_slug': state_slug, 'service_slug': service['slug']},
                     name=f"{service['slug']}-{state_slug}")
            )
    
    # Metro area pages
    for metro in METRO_AREAS:
        urlpatterns.append(
            path(f"{metro['slug']}-economist/", 
                 seo_location_views.metro_area_page,
                 {'metro_slug': metro['slug']},
                 name=f"metro-{metro['slug']}")
        )
        
        # Metro + Service combinations
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f"{metro['slug']}-{service['slug']}/", 
                     seo_location_views.metro_service_page,
                     {'metro_slug': metro['slug'], 'service_slug': service['slug']},
                     name=f"{metro['slug']}-{service['slug']}")
            )
    
    # County pages
    for county in MAJOR_COUNTIES:
        urlpatterns.append(
            path(f"{county['slug']}-economist/", 
                 seo_location_views.county_page,
                 {'county_slug': county['slug']},
                 name=f"county-{county['slug']}")
        )
        
        # County + Service combinations  
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f"{county['slug']}-{service['slug']}/", 
                     seo_location_views.county_service_page,
                     {'county_slug': county['slug'], 'service_slug': service['slug']},
                     name=f"{county['slug']}-{service['slug']}")
            )
    
    return urlpatterns

def generate_city_service_urls():
    """Generate city + service combination URLs"""
    urlpatterns = []
    
    # Combine all city data
    all_cities = []
    
    # Add cities from expanded data
    for state_slug, state_data in EXPANDED_CITY_DATA.items():
        for city in state_data.get('cities', []):
            city['state_slug'] = state_slug
            city['state_abbr'] = state_data.get('state_abbr', '')
            all_cities.append(city)
    
    # Add cities from missing states
    for state_slug, state_data in MISSING_STATES_DATA.items():
        for city in state_data.get('cities', []):
            city['state_slug'] = state_slug
            city['state_abbr'] = state_data.get('state_abbr', '')
            all_cities.append(city)
    
    # Limit to top 200 cities for initial implementation
    top_cities = sorted(all_cities, key=lambda x: int(x.get('population', '0')), reverse=True)[:200]
    
    # Generate city-service URLs
    for city in top_cities:
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(
                    f"{service['slug']}-{city['slug']}/",
                    seo_location_views.city_service_page,
                    {'city_slug': city['slug'], 'service_slug': service['slug']},
                    name=f"{service['slug']}-{city['slug']}"
                )
            )
    
    return urlpatterns

# Main URL patterns
urlpatterns = []

# Add generated location URLs
urlpatterns += generate_all_location_urls()

# Add city-service combination URLs  
urlpatterns += generate_city_service_urls()

# Add aggregate pages
urlpatterns += [
    # All locations index
    path('locations/', seo_location_views.metro_area_page, 
         {'metro_slug': 'greater-boston-area'}, name='all-locations'),
    
    # Regional aggregation pages
    path('northeast-forensic-economist/', seo_location_views.metro_area_page,
         {'metro_slug': 'new-york-metro'}, name='northeast-region'),
    
    path('southeast-forensic-economist/', seo_location_views.metro_area_page,
         {'metro_slug': 'atlanta-metro'}, name='southeast-region'),
    
    path('midwest-forensic-economist/', seo_location_views.metro_area_page,
         {'metro_slug': 'chicago-metro'}, name='midwest-region'),
    
    path('west-coast-forensic-economist/', seo_location_views.metro_area_page,
         {'metro_slug': 'san-francisco-bay-area'}, name='west-coast-region'),
    
    path('southwest-forensic-economist/', seo_location_views.metro_area_page,
         {'metro_slug': 'dallas-fort-worth'}, name='southwest-region'),
]

# Export URL count for monitoring
def get_total_seo_urls():
    """Calculate total number of SEO location URLs"""
    counts = {
        'state_pages': len(US_STATES),
        'state_service_combos': len(US_STATES) * len(CORE_SERVICES),
        'metro_pages': len(METRO_AREAS),
        'metro_service_combos': len(METRO_AREAS) * len(CORE_SERVICES),
        'county_pages': len(MAJOR_COUNTIES),
        'county_service_combos': len(MAJOR_COUNTIES) * len(CORE_SERVICES),
        'city_service_combos': 200 * len(CORE_SERVICES),  # Top 200 cities
        'regional_pages': 6
    }
    
    counts['total'] = sum(counts.values())
    return counts

# Print URL statistics when module loads
if __name__ == '__main__':
    stats = get_total_seo_urls()
    print(f"SEO Location URL Statistics:")
    print(f"  State pages: {stats['state_pages']}")
    print(f"  State-service combos: {stats['state_service_combos']}")
    print(f"  Metro pages: {stats['metro_pages']}")
    print(f"  Metro-service combos: {stats['metro_service_combos']}")
    print(f"  County pages: {stats['county_pages']}")
    print(f"  County-service combos: {stats['county_service_combos']}")
    print(f"  City-service combos: {stats['city_service_combos']}")
    print(f"  Regional pages: {stats['regional_pages']}")
    print(f"  TOTAL URLs: {stats['total']}")