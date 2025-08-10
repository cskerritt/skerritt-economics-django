"""
Improved URL patterns for state-by-service pages
Clean, SEO-friendly URL structure: /locations/{service}/{state}/{city}/
"""
from django.urls import path
from .improved_views import (
    ImprovedCityServiceView,
    StateServiceIndexView, 
    ServiceIndexView,
    CityServiceSitemapView
)

# New improved URL patterns
improved_urlpatterns = [
    # Service index pages (national level)
    path('locations/<slug:service_slug>/', ServiceIndexView.as_view(), name='service_locations_index'),
    
    # State-service index pages  
    path('locations/<slug:service_slug>/<slug:state_slug>/', StateServiceIndexView.as_view(), name='state_service_index'),
    
    # City-service pages (the main landing pages)
    path('locations/<slug:service_slug>/<slug:state_slug>/<slug:city_slug>/', ImprovedCityServiceView.as_view(), name='city_service_page'),
    
    # Sitemap for city-service pages
    path('sitemaps/city-services.xml', CityServiceSitemapView.as_view(), name='city_services_sitemap'),
]

# URL patterns with specific service slugs for better SEO
forensic_economics_urls = [
    path('locations/forensic-economics/<slug:state_slug>/<slug:city_slug>/', 
         ImprovedCityServiceView.as_view(), 
         {'service_slug': 'forensic-economics'}, 
         name='forensic_economics_city'),
]

business_valuation_urls = [
    path('locations/business-valuation/<slug:state_slug>/<slug:city_slug>/', 
         ImprovedCityServiceView.as_view(),
         {'service_slug': 'business-valuation'},
         name='business_valuation_city'),
]

vocational_expert_urls = [
    path('locations/vocational-expert/<slug:state_slug>/<slug:city_slug>/', 
         ImprovedCityServiceView.as_view(),
         {'service_slug': 'vocational-expert'}, 
         name='vocational_expert_city'),
]

life_care_planning_urls = [
    path('locations/life-care-planning/<slug:state_slug>/<slug:city_slug>/', 
         ImprovedCityServiceView.as_view(),
         {'service_slug': 'life-care-planning'},
         name='life_care_planning_city'),
]

# All improved URL patterns combined
all_improved_urls = (
    improved_urlpatterns + 
    forensic_economics_urls +
    business_valuation_urls + 
    vocational_expert_urls +
    life_care_planning_urls
)