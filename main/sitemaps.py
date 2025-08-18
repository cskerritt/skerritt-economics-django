from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post, CaseStudy
from datetime import datetime
from .us_cities_data import US_STATES, PRACTICE_AREAS
import os
import json

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"
    protocol = "https"
    
    def items(self):
        return [
            "home",
            "about",
            "contact",
            "referral",
            "services_index",
            "practice_areas_index",
            "locations_index",
            "resources",
            "case_studies",
            "service_forensic",
            "service_valuation",
            "service_vocational",
            "service_lifecare",
            "vocational_expert",
            "life_care_planning",
            "massachusetts_forensic_economist",
            "rhode_island_forensic_economist",
            "new_england_economic_expert",
            "practice_personal_injury",
            "practice_medical",
            "practice_employment",
            "practice_commercial",
            "tools:index",
            "tools:life_expectancy",
            "tools:present_value",
            "tools:wage_growth",
            "tools:household_services",
            "tools:business_valuation",
            "tools:medical_costs",
        ]
    
    def location(self, item):
        return reverse(item)
    
    def lastmod(self, item):
        return datetime.now()

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = "https"
    
    def items(self):
        return Post.objects.filter(status="published")
    
    def lastmod(self, obj):
        return obj.updated_date

class CaseStudySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    protocol = "https"
    
    def items(self):
        return CaseStudy.objects.filter(published=True)
    
    def lastmod(self, obj):
        return obj.created_date

class LocationSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = "https"
    
    def items(self):
        # Main state pages
        locations = [
            "massachusetts",
            "rhode-island",
            "connecticut",
            "new-hampshire",
            "vermont",
            "maine",
        ]
        
        # Special regional pages
        special_pages = [
            "massachusetts-forensic-economist",
            "rhode-island-forensic-economist",
            "new-england-economic-expert",
        ]
        
        return locations + special_pages
    
    def location(self, item):
        if item in ["massachusetts-forensic-economist", "rhode-island-forensic-economist", "new-england-economic-expert"]:
            # These have their own URL patterns
            if item == "massachusetts-forensic-economist":
                return reverse("ma_forensic_economist")
            elif item == "rhode-island-forensic-economist":
                return reverse("ri_forensic_economist")
            elif item == "new-england-economic-expert":
                return reverse("ne_economic_expert")
        else:
            return reverse("location", kwargs={"state": item})
    
    def lastmod(self, item):
        return datetime.now()

class CitySitemap(Sitemap):
    """
    Generates sitemap for city pages in New England states
    Creates entries for all major cities in each service category
    """
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"
    
    def items(self):
        from .us_cities_seo_data import US_MAJOR_CITIES
        
        # Generate URLs for all cities
        city_pages = []
        services = ["forensic-economist", "business-valuation", "vocational-expert", "life-care-planner"]
        
        for city_slug, city_data in US_MAJOR_CITIES.items():
            for service in services:
                city_pages.append({
                    "city_slug": city_slug,
                    "service": service,
                    "city_name": city_data["name"],
                    "state": city_data["state_abbr"]
                })
        
        return city_pages
    
    def location(self, item):
        return f"/{item['service']}/{item["city_slug"]}/"
    
    def lastmod(self, item):
        return datetime.now()
    
    def priority(self, item):
        # Higher priority for larger cities
        if item["city_slug"] in ["boston", "providence", "hartford", "new-york", "los-angeles", "chicago"]:
            return 0.9
        return 0.8

class PracticeAreaSitemap(Sitemap):
    """
    Generates sitemap for all practice area pages
    """
    changefreq = "monthly"
    priority = 0.7
    protocol = "https"
    
    def items(self):
        return [area["slug"] for area in PRACTICE_AREAS]
    
    def location(self, item):
        return reverse("practice_area_detail", kwargs={"slug": item})
    
    def lastmod(self, item):
        return datetime.now()