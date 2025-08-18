"""
Comprehensive city views for expanded SEO coverage
Handles all 5 services across 888+ cities for maximum SEO impact
"""

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import Http404
from .expanded_city_data import get_city_by_slug, get_all_expanded_cities

class BaseCityServiceView(TemplateView):
    """Base view for city-specific service pages"""
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        city_slug = kwargs.get("city_slug")
        state_slug = kwargs.get("state_slug") 
        service = kwargs.get("service", "")
        
        # Get city data
        city = get_city_by_slug(city_slug, state_slug)
        if not city:
            raise Http404("City not found")
        
        # Add context for all city service pages
        context.update({
            "city": city,
            "service_type": service,
            "page_title": self.get_page_title(city, service),
            "meta_description": self.get_meta_description(city, service),
            "canonical_url": self.get_canonical_url(city, service),
            "breadcrumbs": self.get_breadcrumbs(city, service),
            "schema_markup": self.get_schema_markup(city, service)
        })
        
        return context
    
    def get_page_title(self, city, service):
        """Generate SEO-optimized page title"""
        service_names = {
            "forensic-economics": "Forensic Economist",
            "business-valuation": "Business Valuation Expert", 
            "business-consulting": "Business Consulting Services",
            "vocational-expert": "Vocational Expert",
            "life-care-planning": "Life Care Planning Services"
        }
        service_name = service_names.get(service, service.replace("-", " ").title())
        return f"{service_name} in {city['name']}, {city['state_abbr']} | Expert Services"
    
    def get_meta_description(self, city, service):
        """Generate SEO-optimized meta description"""
        service_descriptions = {
            "forensic-economics": f"Expert forensic economist services in {city['name']}, {city['state_abbr']}. Professional economic damage analysis for litigation support.",
            "business-valuation": f"Professional business valuation services in {city['name']}, {city['state_abbr']}. Expert business appraisal for litigation and transactions.",
            "business-consulting": f"Strategic business consulting services in {city['name']}, {city['state_abbr']}. Expert analysis and advisory for business decisions.",
            "vocational-expert": f"Certified vocational expert services in {city['name']}, {city['state_abbr']}. Professional vocational assessment and testimony.",
            "life-care-planning": f"Expert life care planning services in {city['name']}, {city['state_abbr']}. Comprehensive medical and care cost analysis."
        }
        return service_descriptions.get(service, f"Expert {service.replace('-', ' ')} services in {city['name']}, {city['state_abbr']}.")
    
    def get_canonical_url(self, city, service):
        """Generate canonical URL for the page"""
        return f"/{city['state_slug']}/{city["slug"]}/{service}/"
    
    def get_breadcrumbs(self, city, service):
        """Generate breadcrumb navigation"""
        return [
            {"name": "Home", "url": "/"},
            {"name": "Locations", "url": "/locations/"},
            {"name": city["state"], "url": f"/locations/{city['state_slug']}/"},
            {"name": city["name"], "url": f"/{city['state_slug']}/{city["slug"]}/"},
            {"name": service.replace("-", " ").title(), "url": None}
        ]
    
    def get_schema_markup(self, city, service):
        """Generate JSON-LD schema markup"""
        return {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "name": f"{service.replace("-", " ").title()} in {city["name"]}, {city["state_abbr"]}",
            "description": self.get_meta_description(city, service),
            "areaServed": {
                "@type": "City",
                "name": city["name"],
                "containedInPlace": {
                    "@type": "State", 
                    "name": city["state"]
                }
            },
            "provider": {
                "@type": "Organization",
                "name": "Skerritt Economic Consulting"
            }
        }

class CityForensicEconomicsView(BaseCityServiceView):
    """Forensic Economics services for specific cities"""
    template_name = "main/cities/forensic_economics.html"

class CityBusinessValuationView(BaseCityServiceView):
    """Business Valuation services for specific cities"""
    template_name = "main/cities/business_valuation.html"

class CityBusinessConsultingView(BaseCityServiceView):
    """Business Consulting services for specific cities"""
    template_name = "main/cities/business_consulting.html"

class CityVocationalExpertView(BaseCityServiceView):
    """Vocational Expert services for specific cities"""
    template_name = "main/cities/vocational_expert.html"

class CityLifeCarePlanningView(BaseCityServiceView):
    """Life Care Planning services for specific cities"""
    template_name = "main/cities/life_care_planning.html"
