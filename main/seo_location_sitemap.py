"""
SEO Location Sitemap Generator
Generates sitemap entries for all location-based pages
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .seo_location_system import (
    SEO_LOCATION_DATA,
    CORE_SERVICES,
    METRO_AREAS,
    US_STATES,
    MAJOR_COUNTIES
)
from .expanded_city_data import EXPANDED_CITY_DATA
from .missing_states_data import MISSING_STATES_DATA
from datetime import datetime

class StateSitemap(Sitemap):
    """Sitemap for state-level pages"""
    changefreq = "monthly"
    priority = 0.8
    
    def items(self):
        return list(US_STATES.keys())
    
    def location(self, state_slug):
        return f"/forensic-economist-{state_slug}/"
    
    def lastmod(self, obj):
        return datetime.now()

class StateServiceSitemap(Sitemap):
    """Sitemap for state + service combination pages"""
    changefreq = "monthly"
    priority = 0.7
    
    def items(self):
        combos = []
        for state_slug in US_STATES.keys():
            for service in CORE_SERVICES:
                combos.append({
                    "state": state_slug,
                    "service": service["slug"]
                })
        return combos
    
    def location(self, item):
        return f"/{item["service"]}-{item["state"]}/"
    
    def lastmod(self, obj):
        return datetime.now()

class MetroAreaSitemap(Sitemap):
    """Sitemap for metro area pages"""
    changefreq = "monthly"
    priority = 0.8
    
    def items(self):
        return METRO_AREAS
    
    def location(self, metro):
        return f"/{metro["slug"]}-economist/"
    
    def lastmod(self, obj):
        return datetime.now()

class MetroServiceSitemap(Sitemap):
    """Sitemap for metro + service combination pages"""
    changefreq = "monthly"
    priority = 0.7
    
    def items(self):
        combos = []
        for metro in METRO_AREAS:
            for service in CORE_SERVICES:
                combos.append({
                    "metro": metro["slug"],
                    "service": service["slug"]
                })
        return combos
    
    def location(self, item):
        return f"/{item["metro"]}-{item["service"]}/"
    
    def lastmod(self, obj):
        return datetime.now()

class CountySitemap(Sitemap):
    """Sitemap for county pages"""
    changefreq = "monthly"
    priority = 0.7
    
    def items(self):
        return MAJOR_COUNTIES
    
    def location(self, county):
        return f"/{county["slug"]}-economist/"
    
    def lastmod(self, obj):
        return datetime.now()

class CountyServiceSitemap(Sitemap):
    """Sitemap for county + service combination pages"""
    changefreq = "monthly"
    priority = 0.6
    
    def items(self):
        combos = []
        for county in MAJOR_COUNTIES:
            for service in CORE_SERVICES:
                combos.append({
                    "county": county["slug"],
                    "service": service["slug"]
                })
        return combos
    
    def location(self, item):
        return f"/{item["county"]}-{item["service"]}/"
    
    def lastmod(self, obj):
        return datetime.now()

class CityServiceSitemap(Sitemap):
    """Sitemap for city + service combination pages"""
    changefreq = "monthly"
    priority = 0.6
    
    def items(self):
        combos = []
        all_cities = []
        
        # Collect cities from expanded data
        for state_slug, state_data in EXPANDED_CITY_DATA.items():
            for city in state_data.get("cities", []):
                city["population"] = int(city.get("population", "0"))
                all_cities.append(city)
        
        # Collect cities from missing states
        for state_slug, state_data in MISSING_STATES_DATA.items():
            for city in state_data.get("cities", []):
                city["population"] = int(city.get("population", "0"))
                all_cities.append(city)
        
        # Get top 200 cities by population
        top_cities = sorted(all_cities, key=lambda x: x["population"], reverse=True)[:200]
        
        # Generate combinations
        for city in top_cities:
            for service in CORE_SERVICES:
                combos.append({
                    "city": city["slug"],
                    "service": service["slug"]
                })
        
        return combos
    
    def location(self, item):
        return f"/{item["service"]}-{item["city"]}/"
    
    def lastmod(self, obj):
        return datetime.now()

# Dictionary of all SEO location sitemaps
seo_location_sitemaps = {
    "states": StateSitemap,
    "state_services": StateServiceSitemap,
    "metro_areas": MetroAreaSitemap,
    "metro_services": MetroServiceSitemap,
    "counties": CountySitemap,
    "county_services": CountyServiceSitemap,
    "city_services": CityServiceSitemap,
}

def get_total_sitemap_urls():
    """Calculate total URLs in sitemaps"""
    counts = {
        "states": len(US_STATES),
        "state_services": len(US_STATES) * len(CORE_SERVICES),
        "metro_areas": len(METRO_AREAS),
        "metro_services": len(METRO_AREAS) * len(CORE_SERVICES),
        "counties": len(MAJOR_COUNTIES),
        "county_services": len(MAJOR_COUNTIES) * len(CORE_SERVICES),
        "city_services": 200 * len(CORE_SERVICES),
    }
    
    counts["total"] = sum(counts.values())
    return counts