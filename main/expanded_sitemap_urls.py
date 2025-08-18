"""
Generate sitemap URLs for all expanded city service pages
For use in sitemaps.py to ensure all pages are indexed
"""

from .expanded_city_data import get_all_expanded_cities

def get_all_city_service_urls():
    """Get all city service URL patterns for sitemap generation"""
    
    services = [
        "forensic-economics",
        "business-valuation", 
        "business-consulting",
        "vocational-expert",
        "life-care-planning"
    ]
    
    urls = []
    cities = get_all_expanded_cities()
    
    for city in cities:
        state_slug = city["state_slug"]
        city_slug = city["slug"]
        
        for service in services:
            url = f"/{state_slug}/{city_slug}/{service}/"
            urls.append({
                "url": url,
                "city": city["name"],
                "state": city["state"],
                "service": service,
                "priority": 0.7,
                "changefreq": "monthly"
            })
    
    return urls

def get_city_service_count():
    """Get total count of city service pages"""
    cities = get_all_expanded_cities()
    services_count = 5  # forensic-economics, business-valuation, business-consulting, vocational-expert, life-care-planning
    return len(cities) * services_count
