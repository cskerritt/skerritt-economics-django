"""
Improved views for state-by-service pages with better data structure and SEO
"""
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404
from .us_complete_data import US_STATES_COMPLETE, SERVICES, get_state_by_slug, get_city_by_slug, get_nearby_cities

class ImprovedCityServiceView(TemplateView):
    """
    Improved city-service view with better data structure and SEO
    URL pattern: /locations/{service}/{state}/{city}/
    """
    
    def get_template_names(self):
        service_slug = self.kwargs.get("service_slug")
        # Use service-specific template
        return [f"main/locations/city_{service_slug.replace('-', '_')}.html"]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Extract URL parameters
        service_slug = self.kwargs.get("service_slug")
        state_slug = self.kwargs.get("state_slug") 
        city_slug = self.kwargs.get("city_slug")
        
        # Validate service
        if service_slug not in SERVICES:
            raise Http404("Service not found")
            
        service_info = SERVICES[service_slug]
        
        # Get state data
        state_abbr, state_data = get_state_by_slug(state_slug)
        if not state_data:
            raise Http404("State not found")
            
        # Get city data
        city_data = get_city_by_slug(state_abbr, city_slug)
        if not city_data:
            raise Http404("City not found")
            
        # Get nearby cities for "also serving" section
        nearby_cities = get_nearby_cities(state_abbr, city_slug, 6)
        
        # Build context
        context.update({
            # Service info
            "service": service_info,
            "service_slug": service_slug,
            "service_type": service_slug.replace('-', '_'),
            "service_name": service_info["name"],
            "service_title": service_info["title"],
            "service_description": service_info["description"],
            
            # Location info
            "state_abbr": state_abbr,
            "state_name": state_data["name"],
            "state_slug": state_slug,
            "city": {
                "name": city_data["name"],
                "slug": city_data["slug"],
                "county": city_data["county"],
                "lat": city_data["lat"],
                "lng": city_data["lng"],
                "population": city_data.get("population", 0),
                "state_abbr": state_abbr,
                "state_name": state_data["name"],
                "state": state_slug
            },
            "nearby_cities": nearby_cities,
            
            # SEO data
            "meta_title": f"{service_info['title']} in {city_data['name']}, {state_abbr} | Christopher Skerritt",
            "meta_description": f"Expert {service_info['title'].lower()} services in {city_data['name']}, {state_data['name']}. Christopher Skerritt provides {service_info['description'].lower()} for legal professionals. Call (203) 605-2814.",
            
            # Structured data
            "structured_data": {
                "service_name": f"{service_info['name']} Services in {city_data['name']}",
                "city_name": city_data['name'],
                "state_name": state_data['name'],
                "county": city_data["county"],
                "latitude": city_data["lat"],
                "longitude": city_data["lng"]
            }
        })
        
        return context

class StateServiceIndexView(TemplateView):
    """
    State-level service index page
    URL pattern: /locations/{service}/{state}/
    """
    template_name = "main/locations/state_service_index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        service_slug = self.kwargs.get("service_slug")
        state_slug = self.kwargs.get("state_slug")
        
        # Validate service
        if service_slug not in SERVICES:
            raise Http404("Service not found")
            
        service_info = SERVICES[service_slug]
        
        # Get state data
        state_abbr, state_data = get_state_by_slug(state_slug)
        if not state_data:
            raise Http404("State not found")
            
        context.update({
            "service": service_info,
            "service_slug": service_slug,
            "state_abbr": state_abbr,
            "state_name": state_data["name"], 
            "state_slug": state_slug,
            "cities": state_data["cities"][:20],  # Top 20 cities
            "total_cities": len(state_data["cities"]),
            "meta_title": f"{service_info['title']} Services in {state_data['name']} | Christopher Skerritt",
            "meta_description": f"Expert {service_info['title'].lower()} services throughout {state_data['name']}. Serving all major cities with {service_info['description'].lower()}. Call (203) 605-2814."
        })
        
        return context

class ServiceIndexView(TemplateView):
    """
    National service index page  
    URL pattern: /locations/{service}/
    """
    template_name = "main/locations/service_index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        service_slug = self.kwargs.get("service_slug")
        
        # Validate service
        if service_slug not in SERVICES:
            raise Http404("Service not found")
            
        service_info = SERVICES[service_slug]
        
        # Get featured states (major ones)
        featured_states = ["CA", "TX", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI"]
        states_data = []
        
        for state_abbr in featured_states:
            if state_abbr in US_STATES_COMPLETE:
                state_data = US_STATES_COMPLETE[state_abbr]
                states_data.append({
                    "abbr": state_abbr,
                    "name": state_data["name"],
                    "slug": state_data["slug"],
                    "top_cities": state_data["cities"][:5]
                })
        
        context.update({
            "service": service_info,
            "service_slug": service_slug,
            "featured_states": states_data,
            "total_states": len(US_STATES_COMPLETE),
            "meta_title": f"{service_info['title']} Services Nationwide | Christopher Skerritt", 
            "meta_description": f"Expert {service_info['title'].lower()} services available in all 50 states. {service_info['description']} for legal professionals nationwide. Call (203) 605-2814."
        })
        
        return context

# Utility view for generating sitemaps
class CityServiceSitemapView(TemplateView):
    """Generate sitemap data for all city-service combinations"""
    template_name = "main/sitemaps/city_services.xml"
    content_type = "application/xml"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        urls = []
        for state_abbr, state_data in US_STATES_COMPLETE.items():
            for city in state_data["cities"]:
                for service_slug in SERVICES.keys():
                    urls.append({
                        "url": f"/locations/{service_slug}/{state_data['slug']}/{city['slug']}/",
                        "priority": 0.8,
                        "changefreq": "monthly"
                    })
        
        context["urls"] = urls
        return context