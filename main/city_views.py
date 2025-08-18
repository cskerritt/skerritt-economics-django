"""
City-specific views for local SEO
"""
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from .city_data import get_city_by_slug, get_state_cities

class CityLandingView(TemplateView):
    """Base view for city landing pages"""
    template_name = "main/locations/city_landing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_slug = kwargs.get("city_slug")
        state_slug = kwargs.get("state_slug")
        
        # Get city data using the new city_data module
        city = get_city_by_slug(city_slug, state_slug)
        if not city:
            raise Http404(f"City {city_slug} not found")
        
        context.update({
            "city": city,
            "city_slug": city_slug,
            "service_type": self.service_type if hasattr(self, "service_type") else "all",
            "page_title": self.get_page_title(city),
            "meta_description": self.get_meta_description(city),
            "nearby_cities": self.get_nearby_cities(city),
        })
        return context
    
    def get_page_title(self, city):
        """Generate SEO-optimized title"""
        return f"Forensic Economist {city["name"]}, {city["state_abbr"]} | Economic Expert Witness | Skerritt Economics"
    
    def get_meta_description(self, city):
        """Generate SEO-optimized meta description"""
        return f"Expert forensic economist serving {city["name"]}, {city["state"]}. Economic damage calculations, business valuation, life care planning. Free consultation: (203) 605-2814"
    
    def get_nearby_cities(self, city):
        """Get nearby cities for internal linking"""
        if not city or "state" not in city:
            return []
        
        # Get cities from the same state
        nearby = []
        current_state = city.get("state")
        current_slug = city.get("slug")
        
        state_cities = get_state_cities(current_state)
        for city_data in state_cities:
            if city_data.get("slug") != current_slug:
                nearby.append({
                    "slug": city_data["slug"],
                    "name": city_data["name"],
                    "state_abbr": city_data["state_abbr"]
                })
                if len(nearby) >= 5:
                    break
        
        return nearby


class ForensicEconomistCityView(CityLandingView):
    """Forensic economist city-specific pages"""
    service_type = "forensic-economist"
    template_name = "main/locations/city_forensic_economist.html"
    
    def get_page_title(self, city):
        return f"Forensic Economist {city["name"]}, {city["state_abbr"]} | Economic Damages Expert | Christopher Skerritt"
    
    def get_meta_description(self, city):
        return f"Top forensic economist in {city["name"]}, {city["state_abbr"]}. Lost earnings, wrongful death, personal injury economic analysis. Court-qualified expert. Call (203) 605-2814"


class BusinessValuationCityView(CityLandingView):
    """Business valuation city-specific pages"""
    service_type = "business-valuation"
    template_name = "main/locations/city_business_valuation.html"
    
    def get_page_title(self, city):
        return f"Business Valuation Expert {city["name"]}, {city["state_abbr"]} | Fair Market Value Analysis"
    
    def get_meta_description(self, city):
        return f"Certified business valuation expert in {city["name"]}, {city["state_abbr"]}. Business damages, lost profits, partnership disputes. MBA economist. Free consultation: (203) 605-2814"


class VocationalExpertCityView(CityLandingView):
    """Vocational expert city-specific pages"""
    service_type = "vocational-expert"
    template_name = "main/locations/city_vocational.html"
    
    def get_page_title(self, city):
        return f"Vocational Expert {city["name"]}, {city["state_abbr"]} | CVE ABVE/F | Earning Capacity"
    
    def get_meta_description(self, city):
        return f"Certified vocational expert CVE ABVE/F serving {city["name"]}, {city["state_abbr"]}. Employability assessments, earning capacity analysis. Call (203) 605-2814"


class LifeCarePlannerCityView(CityLandingView):
    """Life care planner city-specific pages"""
    service_type = "life-care-planner"
    template_name = "main/locations/city_lifecare.html"
    
    def get_page_title(self, city):
        return f"Life Care Planner CLCP {city["name"]}, {city["state_abbr"]} | Future Medical Costs"
    
    def get_meta_description(self, city):
        return f"Certified Life Care Planner CLCP in {city["name"]}, {city["state_abbr"]}. Catastrophic injury, future medical costs, Medicare Set-Aside. Free consultation: (203) 605-2814"