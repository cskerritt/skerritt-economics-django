"""
URL patterns for city-specific SEO landing pages
"""
from django.urls import path
from .city_views import (
    ForensicEconomistCityView,
    BusinessValuationCityView,
    VocationalExpertCityView,
    LifeCarePlannerCityView,
)
from .city_views import CityForensicEconomistView, StateForensicEconomistIndexView, AllCitiesForensicEconomistView

# Generate URL patterns for all cities
city_seo_urlpatterns = [
    # Main city index pages
    path('forensic-economist/', 
         AllCitiesForensicEconomistView.as_view(), 
         name='all_cities_forensic_economist'),
    
    path('business-valuation-expert/', 
         AllCitiesForensicEconomistView.as_view(), 
         name='all_cities_business_valuation'),
    
    path('vocational-expert/', 
         AllCitiesForensicEconomistView.as_view(), 
         name='all_cities_vocational_expert'),
    
    path('life-care-planner/', 
         AllCitiesForensicEconomistView.as_view(), 
         name='all_cities_life_care_planner'),
    
    # State index pages
    path('forensic-economist/<str:state_abbr>/', 
         StateForensicEconomistIndexView.as_view(), 
         name='state_forensic_economist_index'),
    
    # City-specific pages for each service
    path('forensic-economist/<str:state_abbr>/<slug:city_slug>/', 
         CityForensicEconomistView.as_view(), 
         name='city_forensic_economist'),
    
    path('business-valuation/<str:state_abbr>/<slug:city_slug>/', 
         BusinessValuationCityView.as_view(), 
         name='city_business_valuation'),
    
    path('vocational-expert/<str:state_abbr>/<slug:city_slug>/', 
         VocationalExpertCityView.as_view(), 
         name='city_vocational_expert'),
    
    path('life-care-planner/<str:state_abbr>/<slug:city_slug>/', 
         LifeCarePlannerCityView.as_view(), 
         name='city_life_care_planner'),
    
    # Alternative URL patterns for better SEO
    path('<slug:city_slug>-forensic-economist/', 
         ForensicEconomistCityView.as_view(), 
         name='city_forensic_economist_alt'),
    
    path('<slug:city_slug>-business-valuation/', 
         BusinessValuationCityView.as_view(), 
         name='city_business_valuation_alt'),
    
    path('<slug:city_slug>-vocational-expert/', 
         VocationalExpertCityView.as_view(), 
         name='city_vocational_expert_alt'),
    
    path('<slug:city_slug>-life-care-planner/', 
         LifeCarePlannerCityView.as_view(), 
         name='city_life_care_planner_alt'),
]