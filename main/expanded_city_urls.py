"""
Comprehensive URL patterns for expanded city coverage across all services
Auto-generated for maximum SEO impact - covers all 888+ unique cities
"""

from django.urls import path
from .expanded_city_views import (
    CityForensicEconomicsView,
    CityBusinessValuationView,
    CityBusinessConsultingView,
    CityVocationalExpertView,
    CityLifeCarePlanningView
)
from .expanded_city_data import get_all_expanded_cities

def generate_expanded_city_urlpatterns():
    """Generate URL patterns for all cities and all services"""
    urlpatterns = []
    
    # Get all cities from expanded data
    cities = get_all_expanded_cities()
    
    for city in cities:
        state_slug = city['state_slug']
        city_slug = city['slug']
        
        # Generate URLs for all 5 services

        # Forensic Economics URLs
        urlpatterns.append(
            path(
                f'{state_slug}/{city_slug}/forensic-economics/',
                CityForensicEconomicsView.as_view(),
                name=f'city_forensic_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug, 'service': 'forensic-economics'}
            )
        )
        # Business Valuation URLs
        urlpatterns.append(
            path(
                f'{state_slug}/{city_slug}/business-valuation/',
                CityBusinessValuationView.as_view(),
                name=f'city_valuation_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug, 'service': 'business-valuation'}
            )
        )
        # Business Consulting URLs
        urlpatterns.append(
            path(
                f'{state_slug}/{city_slug}/business-consulting/',
                CityBusinessConsultingView.as_view(),
                name=f'city_consulting_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug, 'service': 'business-consulting'}
            )
        )
        # Vocational Expert URLs
        urlpatterns.append(
            path(
                f'{state_slug}/{city_slug}/vocational-expert/',
                CityVocationalExpertView.as_view(),
                name=f'city_vocational_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug, 'service': 'vocational-expert'}
            )
        )
        # Life Care Planning URLs
        urlpatterns.append(
            path(
                f'{state_slug}/{city_slug}/life-care-planning/',
                CityLifeCarePlanningView.as_view(),
                name=f'city_lifecare_{state_slug}_{city_slug}',
                kwargs={'city_slug': city_slug, 'state_slug': state_slug, 'service': 'life-care-planning'}
            )
        )
    
    return urlpatterns

# Generate all URL patterns
expanded_city_urlpatterns = generate_expanded_city_urlpatterns()
