#!/usr/bin/env python3
"""
Generate comprehensive URL patterns for all services across all expanded cities
Creates URL patterns for forensic-economics, business-valuation, business-consulting, 
vocational-expert, and life-care-planning for maximum SEO coverage
"""

import sys
import os

# Add the main directory to Python path
sys.path.insert(0, '/home/bitnami/skerritt-economics-django/main')

def generate_expanded_city_urls():
    """Generate comprehensive URL patterns for expanded city coverage"""
    
    # The 5 main services we want to cover
    services = [
        {
            'slug': 'forensic-economics',
            'view_class': 'CityForensicEconomicsView',
            'name_prefix': 'city_forensic',
            'template_suffix': 'forensic_economics'
        },
        {
            'slug': 'business-valuation',
            'view_class': 'CityBusinessValuationView', 
            'name_prefix': 'city_valuation',
            'template_suffix': 'business_valuation'
        },
        {
            'slug': 'business-consulting',
            'view_class': 'CityBusinessConsultingView',
            'name_prefix': 'city_consulting', 
            'template_suffix': 'business_consulting'
        },
        {
            'slug': 'vocational-expert',
            'view_class': 'CityVocationalExpertView',
            'name_prefix': 'city_vocational',
            'template_suffix': 'vocational_expert'
        },
        {
            'slug': 'life-care-planning',
            'view_class': 'CityLifeCarePlanningView',
            'name_prefix': 'city_lifecare',
            'template_suffix': 'life_care_planning'
        }
    ]
    
    content = '''"""
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
'''
    
    # Generate URL patterns for each service
    for service in services:
        service_slug = service['slug']
        view_class = service['view_class']
        name_prefix = service['name_prefix']
        
        content += f'''
        # {service_slug.replace('-', ' ').title()} URLs
        urlpatterns.append(
            path(
                f'{{state_slug}}/{{city_slug}}/{service_slug}/',
                {view_class}.as_view(),
                name=f'{name_prefix}_{{state_slug}}_{{city_slug}}',
                kwargs={{'city_slug': city_slug, 'state_slug': state_slug, 'service': '{service_slug}'}}
            )
        )'''
    
    content += '''
    
    return urlpatterns

# Generate all URL patterns
expanded_city_urlpatterns = generate_expanded_city_urlpatterns()
'''
    
    return content

def generate_expanded_city_views():
    """Generate the view classes for expanded city coverage"""
    
    content = '''"""
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
        
        city_slug = kwargs.get('city_slug')
        state_slug = kwargs.get('state_slug') 
        service = kwargs.get('service', '')
        
        # Get city data
        city = get_city_by_slug(city_slug, state_slug)
        if not city:
            raise Http404("City not found")
        
        # Add context for all city service pages
        context.update({
            'city': city,
            'service_type': service,
            'page_title': self.get_page_title(city, service),
            'meta_description': self.get_meta_description(city, service),
            'canonical_url': self.get_canonical_url(city, service),
            'breadcrumbs': self.get_breadcrumbs(city, service),
            'schema_markup': self.get_schema_markup(city, service)
        })
        
        return context
    
    def get_page_title(self, city, service):
        """Generate SEO-optimized page title"""
        service_names = {
            'forensic-economics': 'Forensic Economist',
            'business-valuation': 'Business Valuation Expert', 
            'business-consulting': 'Business Consulting Services',
            'vocational-expert': 'Vocational Expert',
            'life-care-planning': 'Life Care Planning Services'
        }
        service_name = service_names.get(service, service.replace('-', ' ').title())
        return f"{service_name} in {city['name']}, {city['state_abbr']} | Expert Services"
    
    def get_meta_description(self, city, service):
        """Generate SEO-optimized meta description"""
        service_descriptions = {
            'forensic-economics': f"Expert forensic economist services in {city['name']}, {city['state_abbr']}. Professional economic damage analysis for litigation support.",
            'business-valuation': f"Professional business valuation services in {city['name']}, {city['state_abbr']}. Expert business appraisal for litigation and transactions.",
            'business-consulting': f"Strategic business consulting services in {city['name']}, {city['state_abbr']}. Expert analysis and advisory for business decisions.",
            'vocational-expert': f"Certified vocational expert services in {city['name']}, {city['state_abbr']}. Professional vocational assessment and testimony.",
            'life-care-planning': f"Expert life care planning services in {city['name']}, {city['state_abbr']}. Comprehensive medical and care cost analysis."
        }
        return service_descriptions.get(service, f"Expert {service.replace('-', ' ')} services in {city['name']}, {city['state_abbr']}.")
    
    def get_canonical_url(self, city, service):
        """Generate canonical URL for the page"""
        return f"/{city['state_slug']}/{city['slug']}/{service}/"
    
    def get_breadcrumbs(self, city, service):
        """Generate breadcrumb navigation"""
        return [
            {'name': 'Home', 'url': '/'},
            {'name': 'Locations', 'url': '/locations/'},
            {'name': city['state'], 'url': f"/locations/{city['state_slug']}/"},
            {'name': city['name'], 'url': f"/{city['state_slug']}/{city['slug']}/"},
            {'name': service.replace('-', ' ').title(), 'url': None}
        ]
    
    def get_schema_markup(self, city, service):
        """Generate JSON-LD schema markup"""
        return {
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "name": f"{service.replace('-', ' ').title()} in {city['name']}, {city['state_abbr']}",
            "description": self.get_meta_description(city, service),
            "areaServed": {
                "@type": "City",
                "name": city['name'],
                "containedInPlace": {
                    "@type": "State", 
                    "name": city['state']
                }
            },
            "provider": {
                "@type": "Organization",
                "name": "Skerritt Economic Consulting"
            }
        }

class CityForensicEconomicsView(BaseCityServiceView):
    """Forensic Economics services for specific cities"""
    template_name = 'main/cities/forensic_economics.html'

class CityBusinessValuationView(BaseCityServiceView):
    """Business Valuation services for specific cities"""
    template_name = 'main/cities/business_valuation.html'

class CityBusinessConsultingView(BaseCityServiceView):
    """Business Consulting services for specific cities"""
    template_name = 'main/cities/business_consulting.html'

class CityVocationalExpertView(BaseCityServiceView):
    """Vocational Expert services for specific cities"""
    template_name = 'main/cities/vocational_expert.html'

class CityLifeCarePlanningView(BaseCityServiceView):
    """Life Care Planning services for specific cities"""
    template_name = 'main/cities/life_care_planning.html'
'''
    
    return content

def generate_sitemap_urls():
    """Generate sitemap URLs for all city service combinations"""
    
    content = '''"""
Generate sitemap URLs for all expanded city service pages
For use in sitemaps.py to ensure all pages are indexed
"""

from .expanded_city_data import get_all_expanded_cities

def get_all_city_service_urls():
    """Get all city service URL patterns for sitemap generation"""
    
    services = [
        'forensic-economics',
        'business-valuation', 
        'business-consulting',
        'vocational-expert',
        'life-care-planning'
    ]
    
    urls = []
    cities = get_all_expanded_cities()
    
    for city in cities:
        state_slug = city['state_slug']
        city_slug = city['slug']
        
        for service in services:
            url = f"/{state_slug}/{city_slug}/{service}/"
            urls.append({
                'url': url,
                'city': city['name'],
                'state': city['state'],
                'service': service,
                'priority': 0.7,
                'changefreq': 'monthly'
            })
    
    return urls

def get_city_service_count():
    """Get total count of city service pages"""
    cities = get_all_expanded_cities()
    services_count = 5  # forensic-economics, business-valuation, business-consulting, vocational-expert, life-care-planning
    return len(cities) * services_count
'''
    
    return content

def main():
    print("Generating comprehensive URL patterns for expanded city coverage...")
    print("=" * 70)
    
    # Generate URL patterns file
    urls_content = generate_expanded_city_urls()
    urls_file = '/home/bitnami/skerritt-economics-django/main/expanded_city_urls.py'
    with open(urls_file, 'w', encoding='utf-8') as f:
        f.write(urls_content)
    print(f"✓ Created {urls_file}")
    
    # Generate views file
    views_content = generate_expanded_city_views()
    views_file = '/home/bitnami/skerritt-economics-django/main/expanded_city_views.py'
    with open(views_file, 'w', encoding='utf-8') as f:
        f.write(views_content)
    print(f"✓ Created {views_file}")
    
    # Generate sitemap URLs helper
    sitemap_content = generate_sitemap_urls()
    sitemap_file = '/home/bitnami/skerritt-economics-django/main/expanded_sitemap_urls.py'
    with open(sitemap_file, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    print(f"✓ Created {sitemap_file}")
    
    # Calculate total pages
    try:
        sys.path.insert(0, '/home/bitnami/skerritt-economics-django/main')
        from expanded_city_data import get_all_expanded_cities
        cities = get_all_expanded_cities()
        total_pages = len(cities) * 5  # 5 services per city
        print(f"\n📊 SEO Expansion Summary:")
        print(f"   - Total cities: {len(cities)}")
        print(f"   - Services per city: 5")
        print(f"   - Total new pages: {total_pages:,}")
        print(f"   - Services: forensic-economics, business-valuation, business-consulting, vocational-expert, life-care-planning")
    except Exception as e:
        print(f"Could not calculate totals: {e}")
    
    print(f"\n✅ Comprehensive URL generation complete!")
    print(f"Next steps:")
    print(f"1. Update main/urls.py to include expanded_city_urls")
    print(f"2. Create templates for the 5 service types")
    print(f"3. Update sitemap.py to include all new URLs")

if __name__ == "__main__":
    main()