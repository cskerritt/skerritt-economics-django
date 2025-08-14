"""
Custom sitemap generator that creates a complete sitemap with HTTPS URLs
"""
from datetime import datetime
from xml.etree import ElementTree as ET
from django.http import HttpResponse
from django.urls import reverse
from blog.models import Post, CaseStudy
from .us_cities_data import US_STATES, PRACTICE_AREAS
from .us_cities_seo_data import US_MAJOR_CITIES
from .seo_location_system import (
    CORE_SERVICES,
    METRO_AREAS,
    US_STATES as ALL_US_STATES,
    MAJOR_COUNTIES
)
from .expanded_city_data import EXPANDED_CITY_DATA
from .missing_states_data import MISSING_STATES_DATA


def generate_sitemap_xml(request):
    """Generate a complete sitemap with all HTTPS URLs"""
    
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    urlset.set('xmlns:xhtml', 'http://www.w3.org/1999/xhtml')
    
    base_url = 'https://skerritteconomics.com'
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Helper function to add URL
    def add_url(path, changefreq='weekly', priority='0.8'):
        url = ET.SubElement(urlset, 'url')
        loc = ET.SubElement(url, 'loc')
        loc.text = f"{base_url}{path}"
        lastmod = ET.SubElement(url, 'lastmod')
        lastmod.text = current_date
        cf = ET.SubElement(url, 'changefreq')
        cf.text = changefreq
        pr = ET.SubElement(url, 'priority')
        pr.text = str(priority)
    
    # Add static pages
    static_pages = [
        ('/', 'weekly', 0.9),
        ('/about/', 'weekly', 0.9),
        ('/contact/', 'weekly', 0.9),
        ('/referral/', 'weekly', 0.9),
        ('/services/', 'weekly', 0.9),
        ('/practice-areas/', 'weekly', 0.9),
        ('/locations/', 'weekly', 0.9),
        ('/resources/', 'weekly', 0.9),
        ('/case-studies/', 'weekly', 0.9),
        ('/services/forensic-economics/', 'weekly', 0.9),
        ('/services/business-valuation/', 'weekly', 0.9),
        ('/services/vocational-expert/', 'weekly', 0.9),
        ('/services/life-care-planning/', 'weekly', 0.9),
        ('/vocational-expert/', 'weekly', 0.9),
        ('/life-care-planning/', 'weekly', 0.9),
        ('/locations/massachusetts-forensic-economist/', 'weekly', 0.9),
        ('/locations/rhode-island-forensic-economist/', 'weekly', 0.9),
        ('/locations/new-england-economic-expert/', 'weekly', 0.9),
        ('/practice-areas/personal-injury/', 'weekly', 0.9),
        ('/practice-areas/medical-malpractice/', 'weekly', 0.9),
        ('/practice-areas/employment-litigation/', 'weekly', 0.9),
        ('/practice-areas/commercial-disputes/', 'weekly', 0.9),
        ('/tools/', 'weekly', 0.9),
        ('/tools/life-expectancy/', 'weekly', 0.9),
        ('/tools/present-value/', 'weekly', 0.9),
        ('/tools/wage-growth/', 'weekly', 0.9),
        ('/tools/household-services/', 'weekly', 0.9),
        ('/tools/business-valuation/', 'weekly', 0.9),
        ('/tools/medical-costs/', 'weekly', 0.9),
    ]
    
    for path, freq, priority in static_pages:
        add_url(path, freq, priority)
    
    # Add location pages
    locations = ['massachusetts', 'rhode-island', 'connecticut', 'new-hampshire', 'vermont', 'maine']
    for state in locations:
        add_url(f'/locations/{state}/', 'monthly', 0.8)
    
    # Add blog posts
    try:
        posts = Post.objects.filter(status='published')
        for post in posts:
            add_url(post.get_absolute_url(), 'weekly', 0.7)
    except:
        pass
    
    # Add case studies
    try:
        cases = CaseStudy.objects.filter(published=True)
        for case in cases:
            add_url(case.get_absolute_url(), 'monthly', 0.6)
    except:
        pass
    
    # Add practice area pages
    for area in PRACTICE_AREAS:
        add_url(f"/practice-areas/{area['slug']}/", 'monthly', 0.7)
    
    # Add city pages
    services = ['forensic-economist', 'business-valuation', 'vocational-expert', 'life-care-planner']
    
    # Priority cities
    priority_cities = ['boston', 'providence', 'hartford', 'new-york', 'los-angeles', 'chicago']
    
    for city_slug, city_data in US_MAJOR_CITIES.items():
        for service in services:
            priority = 0.9 if city_slug in priority_cities else 0.8
            add_url(f'/{service}/{city_slug}/', 'weekly', priority)
    
    # Add new SEO location pages
    
    # State pages
    for state_slug in ALL_US_STATES.keys():
        add_url(f'/forensic-economist-{state_slug}/', 'monthly', 0.8)
        
        # State + Service combinations (limited to avoid huge sitemap)
        for service in CORE_SERVICES[:4]:  # Top 4 services
            add_url(f'/{service["slug"]}-{state_slug}/', 'monthly', 0.7)
    
    # Metro area pages
    for metro in METRO_AREAS:
        add_url(f'/{metro["slug"]}-economist/', 'monthly', 0.8)
        
        # Metro + Service combinations
        for service in CORE_SERVICES[:4]:
            add_url(f'/{metro["slug"]}-{service["slug"]}/', 'monthly', 0.7)
    
    # Major county pages
    for county in MAJOR_COUNTIES[:20]:  # Top 20 counties
        add_url(f'/{county["slug"]}-economist/', 'monthly', 0.7)
    
    # Top cities with service combinations
    all_cities = []
    for state_slug, state_data in {**EXPANDED_CITY_DATA, **MISSING_STATES_DATA}.items():
        for city in state_data.get('cities', []):
            city['population'] = int(city.get('population', '0'))
            all_cities.append(city)
    
    # Sort by population and take top 100
    top_cities = sorted(all_cities, key=lambda x: x['population'], reverse=True)[:100]
    
    for city in top_cities:
        for service in CORE_SERVICES[:4]:  # Top 4 services
            add_url(f'/{service["slug"]}-{city["slug"]}/', 'monthly', 0.7)
    
    # Convert to string
    tree = ET.ElementTree(urlset)
    xml_str = ET.tostring(urlset, encoding='unicode', method='xml')
    
    # Add XML declaration
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str
    
    # Return HTTP response
    return HttpResponse(xml_str, content_type='application/xml')