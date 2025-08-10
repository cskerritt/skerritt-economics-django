"""
URL patterns for city-specific pages
"""
from django.urls import path
from .city_views import (
    ForensicEconomistCityView,
    BusinessValuationCityView,
    VocationalExpertCityView,
    LifeCarePlannerCityView
)
from .city_data import get_all_cities

def generate_city_urls():
    """Generate URL patterns for all cities"""
    urlpatterns = []
    
    # Get all cities
    cities = get_all_cities()
    
    for city in cities:
        state_slug = city['state']
        city_slug = city['slug']
        
        # Create URL patterns for each service type
        urlpatterns.extend([
            # Forensic Economist
            path(
                f'{state_slug}/{city_slug}/forensic-economist/',
                ForensicEconomistCityView.as_view(),
                name=f'city_forensic_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug}
            ),
            # Business Valuation
            path(
                f'{state_slug}/{city_slug}/business-valuation/',
                BusinessValuationCityView.as_view(),
                name=f'city_valuation_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug}
            ),
            # Vocational Expert
            path(
                f'{state_slug}/{city_slug}/vocational-expert/',
                VocationalExpertCityView.as_view(),
                name=f'city_vocational_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug}
            ),
            # Life Care Planner
            path(
                f'{state_slug}/{city_slug}/life-care-planner/',
                LifeCarePlannerCityView.as_view(),
                name=f'city_lifecare_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug}
            ),
        ])
    
    return urlpatterns

# Generate all city URLs
city_urlpatterns = generate_city_urls()