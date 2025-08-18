"""
Advanced Sitemap Generator with Image and Video Sitemaps
Implements comprehensive sitemap functionality for better SEO
"""

from datetime import datetime
from xml.etree import ElementTree as ET
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from blog.models import Post, CaseStudy
from .us_cities_data import US_STATES, PRACTICE_AREAS
from .us_cities_seo_data import US_MAJOR_CITIES
import hashlib


class AdvancedSitemapGenerator:
    """Generate comprehensive sitemaps with all extensions"""
    
    def __init__(self, domain="https://skerritteconomics.com"):
        self.domain = domain
        self.namespaces = {
            "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9",
            "xmlns:xhtml": "http://www.w3.org/1999/xhtml",
            "xmlns:image": "http://www.google.com/schemas/sitemap-image/1.1",
            "xmlns:video": "http://www.google.com/schemas/sitemap-video/1.1",
            "xmlns:news": "http://www.google.com/schemas/sitemap-news/0.9",
            "xmlns:mobile": "http://www.google.com/schemas/sitemap-mobile/1.0"
        }
    
    def generate_main_sitemap(self, request):
        """Generate the main sitemap index"""
        
        sitemapindex = ET.Element("sitemapindex")
        for key, value in self.namespaces.items():
            sitemapindex.set(key, value)
        
        # List of sub-sitemaps
        sitemaps = [
            ("pages", "Main pages and static content"),
            ("services", "Service pages"),
            ("locations", "Location and city pages"),
            ("blog", "Blog posts and articles"),
            ("practice-areas", "Practice area pages"),
            ("tools", "Calculator and tool pages"),
            ("images", "Image sitemap"),
        ]
        
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        for sitemap_name, description in sitemaps:
            sitemap = ET.SubElement(sitemapindex, "sitemap")
            loc = ET.SubElement(sitemap, "loc")
            loc.text = f"{self.domain}/sitemap-{sitemap_name}.xml"
            lastmod = ET.SubElement(sitemap, "lastmod")
            lastmod.text = current_date
        
        xml_str = "<?xml version="1.0" encoding="UTF-8"?>\n"
        xml_str += ET.tostring(sitemapindex, encoding="unicode", method="xml")
        
        return HttpResponse(xml_str, content_type="application/xml")
    
    def generate_pages_sitemap(self, request):
        """Generate sitemap for main static pages"""
        
        urlset = self._create_urlset()
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        # Priority pages
        priority_pages = [
            ("/", 1.0, "daily"),
            ("/about/", 0.9, "weekly"),
            ("/contact/", 0.9, "weekly"),
            ("/services/", 0.9, "weekly"),
            ("/locations/", 0.9, "weekly"),
            ("/practice-areas/", 0.9, "weekly"),
            ("/resources/", 0.8, "weekly"),
            ("/case-studies/", 0.8, "weekly"),
            ("/referral/", 0.7, "monthly"),
            ("/tools/", 0.8, "weekly"),
        ]
        
        for path, priority, changefreq in priority_pages:
            url_elem = self._create_url_element(
                urlset,
                path,
                current_date,
                changefreq,
                priority
            )
            
            # Add image if homepage
            if path == "/":
                self._add_image_to_url(
                    url_elem,
                    "/static/images/SEC_LOGO.png",
                    "Skerritt Economics & Consulting - Forensic Economics Experts"
                )
        
        return self._generate_response(urlset)
    
    def generate_services_sitemap(self, request):
        """Generate sitemap for service pages"""
        
        urlset = self._create_urlset()
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        services = [
            {
                "path": "/services/forensic-economics/",
                "title": "Forensic Economics Services",
                "image": "/static/images/forensic-economics.jpg",
                "priority": 0.9
            },
            {
                "path": "/services/business-valuation/",
                "title": "Business Valuation Services",
                "image": "/static/images/business-valuation.jpg",
                "priority": 0.9
            },
            {
                "path": "/services/vocational-expert/",
                "title": "Vocational Expert Services",
                "image": "/static/images/vocational-expert.jpg",
                "priority": 0.9
            },
            {
                "path": "/services/life-care-planning/",
                "title": "Life Care Planning Services",
                "image": "/static/images/life-care-planning.jpg",
                "priority": 0.9
            },
            {
                "path": "/services/business-consulting/",
                "title": "Business Consulting Services",
                "image": "/static/images/business-consulting.jpg",
                "priority": 0.8
            }
        ]
        
        for service in services:
            url_elem = self._create_url_element(
                urlset,
                service["path"],
                current_date,
                "weekly",
                service["priority"]
            )
            
            # Add alternate language versions if applicable
            self._add_alternates(url_elem, service["path"])
        
        return self._generate_response(urlset)
    
    def generate_locations_sitemap(self, request):
        """Generate comprehensive location sitemap"""
        
        urlset = self._create_urlset()
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        # State pages
        states = ["massachusetts", "rhode-island", "connecticut", "new-hampshire", "vermont", "maine"]
        for state in states:
            self._create_url_element(
                urlset,
                f"/locations/{state}/",
                current_date,
                "monthly",
                0.8
            )
        
        # Special location pages
        special_pages = [
            ("/locations/massachusetts-forensic-economist/", 0.9),
            ("/locations/rhode-island-forensic-economist/", 0.9),
            ("/locations/new-england-economic-expert/", 0.9),
        ]
        
        for path, priority in special_pages:
            self._create_url_element(
                urlset,
                path,
                current_date,
                "weekly",
                priority
            )
        
        # City pages for all services
        services = ["forensic-economist", "business-valuation", "vocational-expert", "life-care-planner"]
        priority_cities = ["boston", "providence", "hartford", "new-york", "los-angeles", "chicago"]
        
        for city_slug, city_data in US_MAJOR_CITIES.items():
            for service in services:
                priority = 0.9 if city_slug in priority_cities else 0.8
                changefreq = "weekly" if city_slug in priority_cities else "monthly"
                
                self._create_url_element(
                    urlset,
                    f"/{service}/{city_slug}/",
                    current_date,
                    changefreq,
                    priority
                )
        
        return self._generate_response(urlset)
    
    def generate_blog_sitemap(self, request):
        """Generate sitemap for blog posts with enhanced metadata"""
        
        urlset = self._create_urlset()
        
        try:
            posts = Post.objects.filter(status="published").order_by("-created_date")
            
            for post in posts:
                url_elem = self._create_url_element(
                    urlset,
                    post.get_absolute_url(),
                    post.updated_date.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                    "monthly",
                    0.7
                )
                
                # Add news sitemap tags if recent
                if (datetime.now() - post.created_date).days < 2:
                    self._add_news_tags(url_elem, post)
                
                # Add image if featured image exists
                if hasattr(post, "featured_image") and post.featured_image:
                    self._add_image_to_url(
                        url_elem,
                        post.featured_image.url,
                        post.title
                    )
        except:
            pass
        
        # Add case studies
        try:
            cases = CaseStudy.objects.filter(published=True)
            for case in cases:
                self._create_url_element(
                    urlset,
                    case.get_absolute_url(),
                    case.created_date.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                    "monthly",
                    0.6
                )
        except:
            pass
        
        return self._generate_response(urlset)
    
    def generate_image_sitemap(self, request):
        """Generate image sitemap for better image SEO"""
        
        urlset = self._create_urlset()
        current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        # Define images for key pages
        image_data = [
            {
                "loc": "/",
                "images": [
                    {
                        "url": "/static/images/SEC_LOGO.png",
                        "caption": "Skerritt Economics & Consulting Logo",
                        "title": "Forensic Economics Expert Witness Services"
                    },
                    {
                        "url": "/static/images/christopher-skerritt.jpg",
                        "caption": "Christopher Skerritt, MBA, CRC, CLCP",
                        "title": "Forensic Economist and Business Valuation Expert"
                    }
                ]
            },
            {
                "loc": "/services/forensic-economics/",
                "images": [
                    {
                        "url": "/static/images/economic-damages-chart.png",
                        "caption": "Economic Damages Calculation Methodology",
                        "title": "Forensic Economics Analysis"
                    }
                ]
            },
            {
                "loc": "/services/business-valuation/",
                "images": [
                    {
                        "url": "/static/images/business-valuation-process.png",
                        "caption": "Business Valuation Process Diagram",
                        "title": "Professional Business Valuation Services"
                    }
                ]
            }
        ]
        
        for page in image_data:
            url_elem = ET.SubElement(urlset, "url")
            loc = ET.SubElement(url_elem, "loc")
            loc.text = f"{self.domain}{page['loc']}"
            
            for img in page["images"]:
                image_elem = ET.SubElement(url_elem, "image:image")
                image_loc = ET.SubElement(image_elem, "image:loc")
                image_loc.text = f"{self.domain}{img['url']}"
                
                if "caption" in img:
                    caption = ET.SubElement(image_elem, "image:caption")
                    caption.text = img["caption"]
                
                if "title" in img:
                    title = ET.SubElement(image_elem, "image:title")
                    title.text = img["title"]
        
        return self._generate_response(urlset)
    
    def _create_urlset(self):
        """Create urlset element with namespaces"""
        urlset = ET.Element("urlset")
        for key, value in self.namespaces.items():
            urlset.set(key, value)
        return urlset
    
    def _create_url_element(self, parent, path, lastmod, changefreq, priority):
        """Create a URL element with standard tags"""
        url_elem = ET.SubElement(parent, "url")
        
        loc = ET.SubElement(url_elem, "loc")
        loc.text = f"{self.domain}{path}"
        
        lastmod_elem = ET.SubElement(url_elem, "lastmod")
        lastmod_elem.text = lastmod
        
        changefreq_elem = ET.SubElement(url_elem, "changefreq")
        changefreq_elem.text = changefreq
        
        priority_elem = ET.SubElement(url_elem, "priority")
        priority_elem.text = str(priority)
        
        return url_elem
    
    def _add_image_to_url(self, url_elem, image_path, caption):
        """Add image information to URL element"""
        image_elem = ET.SubElement(url_elem, "image:image")
        image_loc = ET.SubElement(image_elem, "image:loc")
        image_loc.text = f"{self.domain}{image_path}"
        image_caption = ET.SubElement(image_elem, "image:caption")
        image_caption.text = caption
    
    def _add_alternates(self, url_elem, path):
        """Add alternate language versions"""
        # For now just English, but structure supports multiple languages
        xhtml_link = ET.SubElement(url_elem, "xhtml:link")
        xhtml_link.set("rel", "alternate")
        xhtml_link.set("hreflang", "en")
        xhtml_link.set("href", f"{self.domain}{path}")
    
    def _add_news_tags(self, url_elem, post):
        """Add Google News tags for recent articles"""
        news = ET.SubElement(url_elem, "news:news")
        
        publication = ET.SubElement(news, "news:publication")
        name = ET.SubElement(publication, "news:name")
        name.text = "Skerritt Economics Blog"
        language = ET.SubElement(publication, "news:language")
        language.text = "en"
        
        pub_date = ET.SubElement(news, "news:publication_date")
        pub_date.text = post.created_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
        
        title = ET.SubElement(news, "news:title")
        title.text = post.title
    
    def _generate_response(self, urlset):
        """Generate HTTP response from urlset"""
        xml_str = "<?xml version="1.0" encoding="UTF-8"?>\n"
        xml_str += ET.tostring(urlset, encoding="unicode", method="xml")
        return HttpResponse(xml_str, content_type="application/xml")


class DynamicSitemapManager:
    """Manage dynamic sitemap generation and caching"""
    
    @staticmethod
    def get_priority(url_path):
        """Calculate priority based on URL depth and importance"""
        
        # Homepage gets highest priority
        if url_path == "/":
            return 1.0
        
        # Count depth
        depth = url_path.strip("/").count("/")
        
        # High priority patterns
        high_priority = ["/services/", "/about/", "/contact/"]
        if any(pattern in url_path for pattern in high_priority):
            return max(0.9 - (depth * 0.1), 0.5)
        
        # Medium priority patterns
        medium_priority = ["/locations/", "/practice-areas/", "/tools/"]
        if any(pattern in url_path for pattern in medium_priority):
            return max(0.8 - (depth * 0.1), 0.4)
        
        # Default priority based on depth
        return max(0.7 - (depth * 0.1), 0.3)
    
    @staticmethod
    def get_changefreq(url_path):
        """Determine change frequency based on content type"""
        
        if url_path == "/":
            return "daily"
        
        if "/blog/" in url_path:
            return "weekly"
        
        if "/services/" in url_path or "/about/" in url_path:
            return "weekly"
        
        if "/locations/" in url_path:
            return "monthly"
        
        if "/tools/" in url_path:
            return "monthly"
        
        return "weekly"
    
    @staticmethod
    def should_include_in_sitemap(url_path):
        """Determine if URL should be included in sitemap"""
        
        # Exclude patterns
        exclude_patterns = [
            "/admin/",
            "/api/",
            "/accounts/",
            "/static/",
            "/media/",
            "?",  # URLs with query parameters
            "#",  # URLs with anchors
            "/search/",
            "/thank-you/",
            "/404/",
            "/500/"
        ]
        
        for pattern in exclude_patterns:
            if pattern in url_path:
                return False
        
        return True
    
    @staticmethod
    def generate_sitemap_index():
        """Generate sitemap index for large sites"""
        
        sitemap_types = [
            {
                "name": "pages",
                "max_urls": 10000,
                "description": "Static pages and main content"
            },
            {
                "name": "cities",
                "max_urls": 50000,
                "description": "City-specific service pages"
            },
            {
                "name": "blog",
                "max_urls": 10000,
                "description": "Blog posts and articles"
            },
            {
                "name": "practice-areas",
                "max_urls": 5000,
                "description": "Practice area pages"
            },
            {
                "name": "tools",
                "max_urls": 1000,
                "description": "Calculator and tool pages"
            }
        ]
        
        return sitemap_types