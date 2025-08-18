"""
SEO Location Views
Handles all location-based pages for maximum SEO coverage
"""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .seo_location_system import SEO_LOCATION_DATA
from .expanded_city_data import EXPANDED_CITY_DATA
from .missing_states_data import MISSING_STATES_DATA
import json

def state_page(request, state_slug):
    """State-level overview page"""
    state_data = SEO_LOCATION_DATA["states"].get(state_slug)
    if not state_data:
        raise Http404("State not found")
    
    # Get cities for this state
    cities = []
    if state_slug in EXPANDED_CITY_DATA:
        cities = EXPANDED_CITY_DATA[state_slug].get("cities", [])[:10]  # Top 10 cities
    elif state_slug in MISSING_STATES_DATA:
        cities = MISSING_STATES_DATA[state_slug].get("cities", [])
    
    context = {
        "state": state_data,
        "state_slug": state_slug,
        "cities": cities,
        "page_title": f"{state_data['name']} Forensic Economist | Expert Witness & Business Valuation",
        "page_description": f"Leading forensic economist serving {state_data['name']}. Expert economic analysis, business valuation, and damage calculations for all {state_data["abbr"]} courts.",
        "services": SEO_LOCATION_DATA["services"][:4],  # Top services
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": "Locations", "url": "/locations/"},
            {"name": state_data["name"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/state_page.html", context)

def state_service_page(request, state_slug, service_slug):
    """State + Service combination page"""
    state_data = SEO_LOCATION_DATA["states"].get(state_slug)
    service_data = next((s for s in SEO_LOCATION_DATA["services"] if s["slug"] == service_slug), None)
    
    if not state_data or not service_data:
        raise Http404("Page not found")
    
    # Get cities for this state
    cities = []
    if state_slug in EXPANDED_CITY_DATA:
        cities = EXPANDED_CITY_DATA[state_slug].get("cities", [])[:5]
    elif state_slug in MISSING_STATES_DATA:
        cities = MISSING_STATES_DATA[state_slug].get("cities", [])[:5]
    
    context = {
        "state": state_data,
        "service": service_data,
        "cities": cities,
        "page_title": f"{service_data['title']} in {state_data["name"]} | Skerritt Economics",
        "page_description": f"{service_data['description']} throughout {state_data["name"]}. Serving all {state_data["abbr"]} courts and jurisdictions. Free consultation: (203) 605-2814",
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": state_data["name"], "url": f"/forensic-economist-{state_slug}/"},
            {"name": service_data["title"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/state_service_page.html", context)

def metro_area_page(request, metro_slug):
    """Metro area overview page"""
    metro_data = next((m for m in SEO_LOCATION_DATA["metro_areas"] if m["slug"] == metro_slug), None)
    
    if not metro_data:
        raise Http404("Metro area not found")
    
    context = {
        "metro": metro_data,
        "page_title": f"{metro_data['name']} Forensic Economist | Regional Expert Witness",
        "page_description": f"{metro_data['description']}. Expert forensic economics and business valuation services. Call (203) 605-2814",
        "services": SEO_LOCATION_DATA["services"][:4],
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": "Metro Areas", "url": "/locations/"},
            {"name": metro_data["name"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/metro_page.html", context)

def metro_service_page(request, metro_slug, service_slug):
    """Metro area + Service combination page"""
    metro_data = next((m for m in SEO_LOCATION_DATA["metro_areas"] if m["slug"] == metro_slug), None)
    service_data = next((s for s in SEO_LOCATION_DATA["services"] if s["slug"] == service_slug), None)
    
    if not metro_data or not service_data:
        raise Http404("Page not found")
    
    context = {
        "metro": metro_data,
        "service": service_data,
        "page_title": f"{service_data['title']} - {metro_data["name"]} | Expert Services",
        "page_description": f"{service_data['description']} in the {metro_data["name"]} region. Experienced expert witness. Contact: (203) 605-2814",
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": metro_data["name"], "url": f"/{metro_slug}-economist/"},
            {"name": service_data["title"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/metro_service_page.html", context)

def county_page(request, county_slug):
    """County-level page"""
    county_data = next((c for c in SEO_LOCATION_DATA["counties"] if c["slug"] == county_slug), None)
    
    if not county_data:
        raise Http404("County not found")
    
    state_name = SEO_LOCATION_DATA["states"].get(county_data["state"].lower(), {}).get("name", county_data["state"])
    
    context = {
        "county": county_data,
        "state_name": state_name,
        "page_title": f"{county_data['name']} {county_data["state"]} Forensic Economist | Local Expert",
        "page_description": f"Expert forensic economist serving {county_data['name']}, {county_data["state"]}. Economic damages and business valuation. Call (203) 605-2814",
        "services": SEO_LOCATION_DATA["services"][:4],
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": "Counties", "url": "/locations/"},
            {"name": f"{county_data['name']}, {county_data["state"]}", "url": request.path}
        ]
    }
    
    return render(request, "main/seo/county_page.html", context)

def county_service_page(request, county_slug, service_slug):
    """County + Service combination page"""
    county_data = next((c for c in SEO_LOCATION_DATA["counties"] if c["slug"] == county_slug), None)
    service_data = next((s for s in SEO_LOCATION_DATA["services"] if s["slug"] == service_slug), None)
    
    if not county_data or not service_data:
        raise Http404("Page not found")
    
    context = {
        "county": county_data,
        "service": service_data,
        "page_title": f"{service_data['title']} in {county_data["name"]}, {county_data["state"]}",
        "page_description": f"{service_data['description']} for {county_data["name"]} attorneys and businesses. Free consultation: (203) 605-2814",
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": f"{county_data['name']}, {county_data["state"]}", "url": f"/{county_slug}-economist/"},
            {"name": service_data["title"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/county_service_page.html", context)

def city_service_page(request, city_slug, service_slug):
    """City + Service combination page"""
    # Find city data across all states
    city_data = None
    state_data = None
    
    for state_slug, state_info in {**EXPANDED_CITY_DATA, **MISSING_STATES_DATA}.items():
        for city in state_info.get("cities", []):
            if city["slug"] == city_slug:
                city_data = city
                state_data = state_info
                break
        if city_data:
            break
    
    service_data = next((s for s in SEO_LOCATION_DATA["services"] if s["slug"] == service_slug), None)
    
    if not city_data or not service_data:
        raise Http404("Page not found")
    
    context = {
        "city": city_data,
        "state": state_data,
        "service": service_data,
        "page_title": f"{service_data['title']} in {city_data["name"]}, {state_data["state_abbr"]}",
        "page_description": f"{service_data['description']} for {city_data["name"]} area. Expert witness testimony and economic analysis. Call (203) 605-2814",
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": f"{city_data['name']}, {state_data["state_abbr"]}", "url": f"/locations/{city_slug}/"},
            {"name": service_data["title"], "url": request.path}
        ]
    }
    
    return render(request, "main/seo/city_service_page.html", context)