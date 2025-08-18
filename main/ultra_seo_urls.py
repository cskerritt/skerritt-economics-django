"""
Ultra SEO URL Generator
Massive expansion of location-based URLs for maximum coverage
"""

from django.urls import path
from . import ultra_seo_views
from .expanded_seo_services import (
    EXPANDED_SERVICES,
    PRACTICE_AREAS,
    INDUSTRIES,
    COURT_SYSTEMS,
    get_priority_services
)
from .additional_cities_data import (
    ADDITIONAL_CITIES,
    CITY_NEIGHBORHOODS,
    CROSS_BORDER_REGIONS
)
from .seo_location_system import US_STATES, METRO_AREAS, MAJOR_COUNTIES
from .expanded_city_data import EXPANDED_CITY_DATA
from .missing_states_data import MISSING_STATES_DATA

def generate_ultra_seo_urls():
    """Generate massive set of SEO URLs"""
    urlpatterns = []
    
    # Get priority services
    priority_services = get_priority_services()
    high_priority = priority_services['high']
    medium_priority = priority_services['medium']
    
    # 1. Neighborhood + Service URLs for major cities
    for city_slug, neighborhoods in CITY_NEIGHBORHOODS.items():
        for neighborhood in neighborhoods[:10]:  # Top 10 neighborhoods per city
            for service in high_priority[:5]:  # Top 5 high priority services
                urlpatterns.append(
                    path(
                        f"{service['slug']}-{neighborhood['slug']}-{city_slug}/",
                        ultra_seo_views.neighborhood_service_page,
                        {
                            'neighborhood_slug': neighborhood['slug'],
                            'city_slug': city_slug,
                            'service_slug': service['slug']
                        },
                        name=f"{service['slug']}-{neighborhood['slug']}"
                    )
                )
    
    # 2. Practice Area + State combinations
    for state_slug in list(US_STATES.keys())[:30]:  # Top 30 states by population
        for practice_area in PRACTICE_AREAS[:10]:  # Top 10 practice areas
            urlpatterns.append(
                path(
                    f'{practice_area}-expert-{state_slug}/',
                    ultra_seo_views.practice_state_page,
                    {
                        'practice_slug': practice_area,
                        'state_slug': state_slug
                    },
                    name=f'{practice_area}-{state_slug}'
                )
            )
    
    # 3. Industry + Metro combinations
    for metro in METRO_AREAS:
        for industry in INDUSTRIES[:8]:  # Top 8 industries
            urlpatterns.append(
                path(
                    f'{industry}-economist-{metro["slug"]}/',
                    ultra_seo_views.industry_metro_page,
                    {
                        'industry_slug': industry,
                        'metro_slug': metro['slug']
                    },
                    name=f'{industry}-{metro["slug"]}'
                )
            )
    
    # 4. Court System + County combinations
    for county in MAJOR_COUNTIES[:25]:  # Top 25 counties
        for court in COURT_SYSTEMS[:5]:  # Top 5 court types
            urlpatterns.append(
                path(
                    f'{court}-expert-{county["slug"]}/',
                    ultra_seo_views.court_county_page,
                    {
                        'court_slug': court,
                        'county_slug': county['slug']
                    },
                    name=f'{court}-{county["slug"]}'
                )
            )
    
    # 5. Cross-border region pages
    for region in CROSS_BORDER_REGIONS:
        urlpatterns.append(
            path(
                f'{region["slug"]}-forensic-economist/',
                ultra_seo_views.cross_border_page,
                {'region_slug': region['slug']},
                name=f'region-{region["slug"]}'
            )
        )
        
        # Region + Service combinations
        for service in high_priority[:5]:
            urlpatterns.append(
                path(
                    f"{region['slug']}-{service['slug']}/",
                    ultra_seo_views.region_service_page,
                    {
                        'region_slug': region['slug'],
                        'service_slug': service['slug']
                    },
                    name=f"{region['slug']}-{service['slug']}"
                )
            )
    
    # 6. Additional city + service combinations
    for state, cities in ADDITIONAL_CITIES.items():
        for city in cities[:20]:  # Top 20 cities per state
            for service in high_priority[:5]:  # Top 5 services
                urlpatterns.append(
                    path(
                        f"{service['slug']}-{city['slug']}/",
                        ultra_seo_views.city_service_page,
                        {
                            'city_slug': city['slug'],
                            'service_slug': service['slug']
                        },
                        name=f"{service['slug']}-{city['slug']}"
                    )
                )
    
    # 7. Specialized service + major city combinations
    all_cities = []
    for state_data in {**EXPANDED_CITY_DATA, **MISSING_STATES_DATA}.values():
        all_cities.extend(state_data.get('cities', []))
    
    # Sort by population and get top 100
    top_cities = sorted(
        [c for c in all_cities if 'population' in c],
        key=lambda x: int(x.get('population', '0')),
        reverse=True
    )[:100]
    
    for city in top_cities:
        for service in medium_priority[:10]:  # Medium priority services
            urlpatterns.append(
                path(
                    f"{service['slug']}-{city['slug']}/",
                    ultra_seo_views.city_service_page,
                    {
                        'city_slug': city['slug'],
                        'service_slug': service['slug']
                    },
                    name=f"{service['slug']}-{city['slug']}-med"
                )
            )
    
    # 8. Practice area + major city combinations
    for city in top_cities[:50]:  # Top 50 cities
        for practice in PRACTICE_AREAS[:8]:  # Top 8 practice areas
            urlpatterns.append(
                path(
                    f'{practice}-lawyer-{city["slug"]}/',
                    ultra_seo_views.practice_city_page,
                    {
                        'practice_slug': practice,
                        'city_slug': city['slug']
                    },
                    name=f'{practice}-{city["slug"]}'
                )
            )
    
    # 9. Industry-specific state pages
    for state_slug in list(US_STATES.keys())[:25]:  # Top 25 states
        for industry in INDUSTRIES[:5]:  # Top 5 industries
            urlpatterns.append(
                path(
                    f'{industry}-expert-witness-{state_slug}/',
                    ultra_seo_views.industry_state_page,
                    {
                        'industry_slug': industry,
                        'state_slug': state_slug
                    },
                    name=f'{industry}-witness-{state_slug}'
                )
            )
    
    # 10. Dual service combinations for metros
    for metro in METRO_AREAS[:8]:  # Top 8 metros
        urlpatterns.append(
            path(
                f'business-valuation-forensic-economist-{metro["slug"]}/',
                ultra_seo_views.dual_service_metro,
                {'metro_slug': metro['slug']},
                name=f'dual-service-{metro["slug"]}'
            )
        )
    
    return urlpatterns

# Generate all URLs
ultra_seo_urlpatterns = generate_ultra_seo_urls()

def calculate_ultra_seo_stats():
    """Calculate statistics for ultra SEO expansion"""
    stats = {
        'neighborhoods': len(CITY_NEIGHBORHOODS) * 10 * 5,  # cities * neighborhoods * services
        'practice_states': 30 * 10,  # states * practice areas
        'industry_metros': len(METRO_AREAS) * 8,  # metros * industries
        'court_counties': 25 * 5,  # counties * court types
        'cross_border': len(CROSS_BORDER_REGIONS) * 6,  # regions * (1 + 5 services)
        'additional_cities': sum(len(cities[:20]) for cities in ADDITIONAL_CITIES.values()) * 5,
        'specialized_cities': 100 * 10,  # top cities * medium priority services
        'practice_cities': 50 * 8,  # top cities * practice areas
        'industry_states': 25 * 5,  # states * industries
        'dual_service_metros': 8,  # top metros
    }
    
    stats['total'] = sum(stats.values())
    return stats

# Export for use in other modules
ULTRA_SEO_STATS = calculate_ultra_seo_stats()