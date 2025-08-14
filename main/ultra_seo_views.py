"""
Ultra SEO Views
Handle all expanded location and service combination pages
"""

from django.shortcuts import render
from django.http import Http404
from .expanded_seo_services import (
    EXPANDED_SERVICES,
    PRACTICE_AREAS,
    INDUSTRIES,
    COURT_SYSTEMS
)
from .additional_cities_data import (
    ADDITIONAL_CITIES,
    CITY_NEIGHBORHOODS,
    CROSS_BORDER_REGIONS
)
from .seo_location_system import US_STATES, METRO_AREAS, MAJOR_COUNTIES

def neighborhood_service_page(request, neighborhood_slug, city_slug, service_slug):
    """Neighborhood + Service page"""
    # Find neighborhood data
    neighborhoods = CITY_NEIGHBORHOODS.get(city_slug, [])
    neighborhood = next((n for n in neighborhoods if n['slug'] == neighborhood_slug), None)
    service = next((s for s in EXPANDED_SERVICES if s['slug'] == service_slug), None)
    
    if not neighborhood or not service:
        raise Http404("Page not found")
    
    context = {
        'neighborhood': neighborhood,
        'city': city_slug.replace('-', ' ').title(),
        'service': service,
        'page_title': f'{service["title"]} in {neighborhood["name"]}, {city_slug.replace("-", " ").title()}',
        'page_description': f'{service["description"]} serving {neighborhood["name"]} area. Local expert witness. Call (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': city_slug.replace('-', ' ').title(), 'url': f'/locations/{city_slug}/'},
            {'name': neighborhood['name'], 'url': f'/{neighborhood_slug}/'},
            {'name': service['title'], 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/neighborhood_service.html', context)

def practice_state_page(request, practice_slug, state_slug):
    """Practice Area + State page"""
    state = US_STATES.get(state_slug)
    
    if not state or practice_slug not in PRACTICE_AREAS:
        raise Http404("Page not found")
    
    practice_name = practice_slug.replace('-', ' ').title()
    
    context = {
        'practice': practice_name,
        'practice_slug': practice_slug,
        'state': state,
        'page_title': f'{practice_name} Expert Witness in {state["name"]} | Skerritt Economics',
        'page_description': f'Expert {practice_name.lower()} economic analysis throughout {state["name"]}. Experienced expert witness. Contact (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': 'Practice Areas', 'url': '/practice-areas/'},
            {'name': state['name'], 'url': f'/forensic-economist-{state_slug}/'},
            {'name': practice_name, 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/practice_state.html', context)

def industry_metro_page(request, industry_slug, metro_slug):
    """Industry + Metro page"""
    metro = next((m for m in METRO_AREAS if m['slug'] == metro_slug), None)
    
    if not metro or industry_slug not in INDUSTRIES:
        raise Http404("Page not found")
    
    industry_name = industry_slug.replace('-', ' ').title()
    
    context = {
        'industry': industry_name,
        'metro': metro,
        'page_title': f'{industry_name} Economist - {metro["name"]} | Industry Expert',
        'page_description': f'Specialized {industry_name.lower()} economic expert serving the {metro["name"]} region. Call (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': metro['name'], 'url': f'/{metro_slug}-economist/'},
            {'name': f'{industry_name} Industry', 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/industry_metro.html', context)

def court_county_page(request, court_slug, county_slug):
    """Court System + County page"""
    county = next((c for c in MAJOR_COUNTIES if c['slug'] == county_slug), None)
    
    if not county or court_slug not in COURT_SYSTEMS:
        raise Http404("Page not found")
    
    court_name = court_slug.replace('-', ' ').title()
    
    context = {
        'court': court_name,
        'county': county,
        'page_title': f'{court_name} Expert - {county["name"]}, {county["state"]}',
        'page_description': f'Expert witness for {court_name.lower()} in {county["name"]}. Economic damages and valuations. (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': f'{county["name"]}, {county["state"]}', 'url': f'/{county_slug}-economist/'},
            {'name': court_name, 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/court_county.html', context)

def cross_border_page(request, region_slug):
    """Cross-border region page"""
    region = next((r for r in CROSS_BORDER_REGIONS if r['slug'] == region_slug), None)
    
    if not region:
        raise Http404("Region not found")
    
    context = {
        'region': region,
        'page_title': f'{region["name"]} Forensic Economist | Regional Expert',
        'page_description': f'Expert forensic economics serving the {region["name"]} region. {region["description"]}. Call (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': 'Regions', 'url': '/locations/'},
            {'name': region['name'], 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/cross_border.html', context)

def region_service_page(request, region_slug, service_slug):
    """Cross-border region + Service page"""
    region = next((r for r in CROSS_BORDER_REGIONS if r['slug'] == region_slug), None)
    service = next((s for s in EXPANDED_SERVICES if s['slug'] == service_slug), None)
    
    if not region or not service:
        raise Http404("Page not found")
    
    context = {
        'region': region,
        'service': service,
        'page_title': f'{service["title"]} - {region["name"]} | Cross-Border Expert',
        'page_description': f'{service["description"]} in the {region["name"]} area. {region["description"]}. (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': region['name'], 'url': f'/{region_slug}-forensic-economist/'},
            {'name': service['title'], 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/region_service.html', context)

def city_service_page(request, city_slug, service_slug):
    """Enhanced city + service page"""
    # Find city across all data sources
    city = None
    state_name = None
    
    # Check additional cities
    for state, cities in ADDITIONAL_CITIES.items():
        for c in cities:
            if c['slug'] == city_slug:
                city = c
                state_name = state.title()
                break
        if city:
            break
    
    service = next((s for s in EXPANDED_SERVICES if s['slug'] == service_slug), None)
    
    if not city or not service:
        raise Http404("Page not found")
    
    context = {
        'city': city,
        'state': state_name,
        'service': service,
        'page_title': f'{service["title"]} in {city["name"]}, {state_name}',
        'page_description': f'{service["description"]} for {city["name"]} attorneys and businesses. Expert witness services. (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': f'{city["name"]}, {state_name}', 'url': f'/locations/{city_slug}/'},
            {'name': service['title'], 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/city_service_enhanced.html', context)

def practice_city_page(request, practice_slug, city_slug):
    """Practice area + City page"""
    # Find city
    city = None
    state_name = None
    
    for state, cities in ADDITIONAL_CITIES.items():
        for c in cities:
            if c['slug'] == city_slug:
                city = c
                state_name = state.title()
                break
        if city:
            break
    
    if not city or practice_slug not in PRACTICE_AREAS:
        raise Http404("Page not found")
    
    practice_name = practice_slug.replace('-', ' ').title()
    
    context = {
        'practice': practice_name,
        'city': city,
        'state': state_name,
        'page_title': f'{practice_name} Economic Expert in {city["name"]}, {state_name}',
        'page_description': f'Expert {practice_name.lower()} economist serving {city["name"]}. Economic damage calculations. Call (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': f'{city["name"]}, {state_name}', 'url': f'/locations/{city_slug}/'},
            {'name': practice_name, 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/practice_city.html', context)

def industry_state_page(request, industry_slug, state_slug):
    """Industry + State page"""
    state = US_STATES.get(state_slug)
    
    if not state or industry_slug not in INDUSTRIES:
        raise Http404("Page not found")
    
    industry_name = industry_slug.replace('-', ' ').title()
    
    context = {
        'industry': industry_name,
        'state': state,
        'page_title': f'{industry_name} Expert Witness in {state["name"]} | Industry Specialist',
        'page_description': f'{industry_name} industry economic expert serving all {state["name"]} courts. Specialized expertise. (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': state['name'], 'url': f'/forensic-economist-{state_slug}/'},
            {'name': f'{industry_name} Industry', 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/industry_state.html', context)

def dual_service_metro(request, metro_slug):
    """Dual service combination for metro areas"""
    metro = next((m for m in METRO_AREAS if m['slug'] == metro_slug), None)
    
    if not metro:
        raise Http404("Metro not found")
    
    context = {
        'metro': metro,
        'page_title': f'Business Valuation & Forensic Economics - {metro["name"]}',
        'page_description': f'Combined business valuation and forensic economics expertise in {metro["name"]}. Complete economic analysis. (203) 605-2814',
        'breadcrumb_items': [
            {'name': 'Home', 'url': '/'},
            {'name': metro['name'], 'url': f'/{metro_slug}-economist/'},
            {'name': 'Business Valuation & Forensic Economics', 'url': request.path}
        ]
    }
    
    return render(request, 'main/seo/dual_service.html', context)