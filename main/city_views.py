"""
City-specific views for local SEO
"""
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .city_data import get_city_by_slug, get_all_cities, CITY_DATA

class CityLandingView(TemplateView):
    """Base view for city landing pages"""
    template_name = 'main/locations/city_landing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_slug = kwargs.get('city_slug')
        state_slug = kwargs.get('state_slug')
        
        # Get city data
        city = get_city_by_slug(city_slug, state_slug)
        if not city:
            # Handle 404
            city = {'name': 'Unknown', 'state_name': 'Unknown'}
        
        context.update({
            'city': city,
            'service_type': self.service_type if hasattr(self, 'service_type') else 'all',
            'page_title': self.get_page_title(city),
            'meta_description': self.get_meta_description(city),
            'nearby_cities': self.get_nearby_cities(city),
        })
        return context
    
    def get_page_title(self, city):
        """Generate SEO-optimized title"""
        return f"Forensic Economist {city['name']}, {city['state_abbr']} | Economic Expert Witness | Skerritt Economics"
    
    def get_meta_description(self, city):
        """Generate SEO-optimized meta description"""
        return f"Expert forensic economist serving {city['name']}, {city['state_name']}. Economic damage calculations, business valuation, life care planning. Free consultation: (203) 605-2814"
    
    def get_nearby_cities(self, city):
        """Get nearby cities for internal linking"""
        if not city or 'state' not in city:
            return []
        
        state_data = CITY_DATA.get(city['state'], {})
        cities = state_data.get('cities', [])
        
        # Return up to 5 other cities from the same state
        nearby = [c for c in cities if c['slug'] != city.get('slug', '')][:5]
        return nearby


class ForensicEconomistCityView(CityLandingView):
    """Forensic economist city-specific pages"""
    service_type = 'forensic-economist'
    template_name = 'main/locations/city_forensic.html'
    
    def get_page_title(self, city):
        return f"Forensic Economist {city['name']}, {city['state_abbr']} | Economic Damages Expert | Christopher Skerritt"
    
    def get_meta_description(self, city):
        return f"Top forensic economist in {city['name']}, {city['state_abbr']}. Lost earnings, wrongful death, personal injury economic analysis. Court-qualified expert. Call (203) 605-2814"


class BusinessValuationCityView(CityLandingView):
    """Business valuation city-specific pages"""
    service_type = 'business-valuation'
    template_name = 'main/locations/city_valuation.html'
    
    def get_page_title(self, city):
        return f"Business Valuation Expert {city['name']}, {city['state_abbr']} | Fair Market Value Analysis"
    
    def get_meta_description(self, city):
        return f"Certified business valuation expert in {city['name']}, {city['state_abbr']}. Business damages, lost profits, partnership disputes. MBA economist. Free consultation: (203) 605-2814"


class VocationalExpertCityView(CityLandingView):
    """Vocational expert city-specific pages"""
    service_type = 'vocational-expert'
    template_name = 'main/locations/city_vocational.html'
    
    def get_page_title(self, city):
        return f"Vocational Expert {city['name']}, {city['state_abbr']} | CVE ABVE/F | Earning Capacity"
    
    def get_meta_description(self, city):
        return f"Certified vocational expert CVE ABVE/F serving {city['name']}, {city['state_abbr']}. Employability assessments, earning capacity analysis. Call (203) 605-2814"


class LifeCarePlannerCityView(CityLandingView):
    """Life care planner city-specific pages"""
    service_type = 'life-care-planner'
    template_name = 'main/locations/city_lifecare.html'
    
    def get_page_title(self, city):
        return f"Life Care Planner CLCP {city['name']}, {city['state_abbr']} | Future Medical Costs"
    
    def get_meta_description(self, city):
        return f"Certified Life Care Planner CLCP in {city['name']}, {city['state_abbr']}. Catastrophic injury, future medical costs, Medicare Set-Aside. Free consultation: (203) 605-2814"