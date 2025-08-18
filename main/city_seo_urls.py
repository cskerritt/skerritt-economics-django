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

# Generate URL patterns for all cities
city_seo_urlpatterns = [
    # City-specific pages for forensic economist
    path("forensic-economist/<slug:city_slug>/", 
         ForensicEconomistCityView.as_view(), 
         name="city_forensic_economist"),
    
    path("business-valuation/<slug:city_slug>/", 
         BusinessValuationCityView.as_view(), 
         name="city_business_valuation"),
    
    path("vocational-expert/<slug:city_slug>/", 
         VocationalExpertCityView.as_view(), 
         name="city_vocational_expert"),
    
    path("life-care-planner/<slug:city_slug>/", 
         LifeCarePlannerCityView.as_view(), 
         name="city_life_care_planner"),
    
    # Alternative URL patterns for better SEO
    path("<slug:city_slug>-forensic-economist/", 
         ForensicEconomistCityView.as_view(), 
         name="city_forensic_economist_alt"),
    
    path("<slug:city_slug>-business-valuation/", 
         BusinessValuationCityView.as_view(), 
         name="city_business_valuation_alt"),
    
    path("<slug:city_slug>-vocational-expert/", 
         VocationalExpertCityView.as_view(), 
         name="city_vocational_expert_alt"),
    
    path("<slug:city_slug>-life-care-planner/", 
         LifeCarePlannerCityView.as_view(), 
         name="city_life_care_planner_alt"),
]