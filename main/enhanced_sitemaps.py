from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone

class EnhancedStaticSitemap(Sitemap):
    """Enhanced sitemap with proper priorities and change frequencies"""
    protocol = "https"
    
    # Define pages with their priorities and change frequencies
    pages = {
        # High priority pages
        "home": {"priority": 1.0, "changefreq": "daily"},
        "contact": {"priority": 0.9, "changefreq": "monthly"},
        "services_index": {"priority": 0.9, "changefreq": "weekly"},
        
        # Service pages
        "service_forensic": {"priority": 0.8, "changefreq": "weekly"},
        "service_valuation": {"priority": 0.8, "changefreq": "weekly"},
        "service_consulting": {"priority": 0.8, "changefreq": "weekly"},
        "service_vocational": {"priority": 0.8, "changefreq": "weekly"},
        "service_lifecare": {"priority": 0.8, "changefreq": "weekly"},
        
        # About and resources
        "about": {"priority": 0.7, "changefreq": "monthly"},
        "resources": {"priority": 0.6, "changefreq": "weekly"},
        "case_studies": {"priority": 0.7, "changefreq": "weekly"},
        
        # Practice areas
        "practice_areas_index": {"priority": 0.7, "changefreq": "weekly"},
        
        # Locations
        "locations_index": {"priority": 0.7, "changefreq": "monthly"},
        
        # Tools
        "tools:index": {"priority": 0.5, "changefreq": "monthly"},
        "tools:life_expectancy": {"priority": 0.5, "changefreq": "monthly"},
        
        # Lower priority
        "referral": {"priority": 0.4, "changefreq": "yearly"},
    }
    
    def items(self):
        return list(self.pages.keys())
    
    def location(self, item):
        return reverse(item)
    
    def priority(self, item):
        return self.pages.get(item, {}).get("priority", 0.5)
    
    def changefreq(self, item):
        return self.pages.get(item, {}).get("changefreq", "monthly")
    
    def lastmod(self, item):
        # Return recent date for important pages
        if item == "home":
            return timezone.now()
        elif self.pages.get(item, {}).get("priority", 0.5) >= 0.8:
            return timezone.now() - timedelta(days=7)
        else:
            return timezone.now() - timedelta(days=30)

class LocationSitemap(Sitemap):
    """Sitemap for location-specific pages"""
    priority = 0.7
    changefreq = "weekly"
    protocol = "https"
    
    def items(self):
        # Get all states with cities
        from .city_data_all_states import STATES_WITH_CITIES
        
        locations = []
        for state_data in STATES_WITH_CITIES:
            state_slug = state_data["slug"]
            
            # Add state page
            locations.append(("location", state_slug))
            
            # Add city pages for this state
            for city in state_data.get("cities", []):
                city_slug = city["slug"]
                locations.append(("city_service", f"{state_slug}/{city_slug}"))
        
        return locations
    
    def location(self, item):
        view_name, slug = item
        if view_name == "location":
            return reverse(view_name, args=[slug])
        else:
            return f"/locations/{slug}/"
    
    def lastmod(self, item):
        return timezone.now() - timedelta(days=14)

class ServiceLocationSitemap(Sitemap):
    """Sitemap for service-location combination pages"""
    priority = 0.6
    changefreq = "weekly"
    protocol = "https"
    
    def items(self):
        services = [
            "forensic-economics",
            "business-valuation",
            "business-consulting",
            "vocational-expert",
            "life-care-planning"
        ]
        
        locations = [
            "massachusetts",
            "rhode-island",
            "connecticut",
            "new-hampshire",
            "vermont",
            "maine"
        ]
        
        # Generate all combinations
        combinations = []
        for service in services:
            for location in locations:
                combinations.append(f"{location}/{service}")
        
        return combinations
    
    def location(self, item):
        return f"/locations/{item}/"
    
    def lastmod(self, item):
        return timezone.now() - timedelta(days=21)

class BlogSitemap(Sitemap):
    """Sitemap for blog posts"""
    priority = 0.6
    changefreq = "weekly"
    protocol = "https"
    
    def items(self):
        try:
            from blog.models import Post
            return Post.objects.filter(is_published=True).order_by("-created_at")
        except:
            return []
    
    def location(self, obj):
        return reverse("blog:detail", args=[obj.slug])
    
    def lastmod(self, obj):
        return obj.updated_at if hasattr(obj, "updated_at") else obj.created_at
    
    def priority(self, obj):
        # Newer posts get higher priority
        age = (timezone.now() - obj.created_at).days
        if age < 7:
            return 0.8
        elif age < 30:
            return 0.7
        elif age < 90:
            return 0.6
        else:
            return 0.5

def generate_sitemap_index():
    """Generate a sitemap index file"""
    sitemaps = {
        "static": EnhancedStaticSitemap,
        "locations": LocationSitemap,
        "service-locations": ServiceLocationSitemap,
        "blog": BlogSitemap,
    }
    
    sitemap_urls = []
    base_url = "https://skerritteconomics.com"
    
    for name, sitemap_class in sitemaps.items():
        sitemap_urls.append({
            "loc": f"{base_url}/sitemap-{name}.xml",
            "lastmod": timezone.now().isoformat()
        })
    
    return sitemap_urls