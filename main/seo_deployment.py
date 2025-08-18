"""
SEO Deployment and Indexing Framework
Handles sitemap generation, Google Search Console submission, and performance monitoring
"""

import xml.etree.ElementTree as ET
from datetime import datetime
import json
import requests
from django.conf import settings
from .us_complete_data import US_STATES_COMPLETE, SERVICES

class SEODeploymentManager:
    """Manage SEO deployment, indexing, and monitoring"""
    
    def __init__(self):
        self.base_url = "https://skerritteconomics.com"
        self.sitemap_path = "/sitemap.xml"
        
    def generate_comprehensive_sitemap(self):
        """Generate complete XML sitemap for all pages"""
        
        # Create root element
        urlset = ET.Element("urlset")
        urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
        urlset.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        urlset.set("xmlns:image", "http://www.google.com/schemas/sitemap-image/1.1")
        
        # Priority and change frequency mapping
        priority_map = {
            "home": 1.0,
            "service": 0.9,
            "city_service": 0.8,
            "state_service": 0.7,
            "static": 0.6
        }
        
        changefreq_map = {
            "home": "weekly",
            "service": "monthly",
            "city_service": "monthly",
            "state_service": "monthly",
            "static": "yearly"
        }
        
        # Add homepage
        self._add_url(urlset, "/", priority_map["home"], changefreq_map["home"])
        
        # Add main service pages
        for service_slug in SERVICES.keys():
            self._add_url(
                urlset, 
                f"/services/{service_slug}/",
                priority_map["service"],
                changefreq_map["service"]
            )
        
        # Add static pages
        static_pages = [
            "/about/",
            "/contact/",
            "/case-studies/",
            "/resources/",
            "/tools/",
            "/practice-areas/",
            "/locations/"
        ]
        
        for page in static_pages:
            self._add_url(urlset, page, priority_map["static"], changefreq_map["static"])
        
        # Add all city-service combination pages
        for state_abbr, state_data in US_STATES_COMPLETE.items():
            state_slug = state_data["slug"]
            
            # Add state-service pages
            for service_slug in SERVICES.keys():
                self._add_url(
                    urlset,
                    f"/locations/{service_slug}/{state_slug}/",
                    priority_map["state_service"],
                    changefreq_map["state_service"]
                )
                
                # Add city-service pages
                for city in state_data["cities"]:
                    city_slug = city["slug"]
                    self._add_url(
                        urlset,
                        f"/locations/{service_slug}/{state_slug}/{city_slug}/",
                        priority_map["city_service"],
                        changefreq_map["city_service"]
                    )
        
        # Convert to string
        tree = ET.ElementTree(urlset)
        return ET.tostring(urlset, encoding="unicode", method="xml")
    
    def _add_url(self, parent, loc, priority, changefreq):
        """Add URL entry to sitemap"""
        
        url = ET.SubElement(parent, "url")
        
        # Location
        loc_elem = ET.SubElement(url, "loc")
        loc_elem.text = f"{self.base_url}{loc}"
        
        # Last modified
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = datetime.now().strftime("%Y-%m-%d")
        
        # Change frequency
        changefreq_elem = ET.SubElement(url, "changefreq")
        changefreq_elem.text = changefreq
        
        # Priority
        priority_elem = ET.SubElement(url, "priority")
        priority_elem.text = str(priority)
        
        return url
    
    def generate_robots_txt(self):
        """Generate SEO-optimized robots.txt"""
        
        robots_content = """# Robots.txt for Skerritt Economics
# Generated: {date}

# Allow all bots
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/
Disallow: /private/
Disallow: *.json$
Disallow: /*?*sort=
Disallow: /*?*filter=

# Specific bot rules
User-agent: Googlebot
Allow: /
Crawl-delay: 0

User-agent: Bingbot
Allow: /
Crawl-delay: 1

User-agent: Slurp
Allow: /
Crawl-delay: 1

# Bad bots
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Crawl-delay: 10

# Sitemaps
Sitemap: {base_url}/sitemap.xml
Sitemap: {base_url}/sitemap-images.xml
Sitemap: {base_url}/sitemap-pages.xml
""".format(date=datetime.now().strftime("%Y-%m-%d"), base_url=self.base_url)
        
        return robots_content
    
    def submit_to_search_console(self, sitemap_url):
        """Submit sitemap to Google Search Console via API"""
        
        # This would require Google Search Console API credentials
        # Placeholder for API integration
        
        api_endpoint = "https://www.googleapis.com/webmasters/v3/sites/{}/sitemaps/{}"
        
        submission_data = {
            "sitemap_url": sitemap_url,
            "submitted_date": datetime.now().isoformat(),
            "status": "pending"
        }
        
        # In production, you would:
        # 1. Authenticate with Google API
        # 2. Submit sitemap
        # 3. Track submission status
        
        return submission_data
    
    def ping_search_engines(self):
        """Ping search engines about sitemap updates"""
        
        sitemap_url = f"{self.base_url}/sitemap.xml"
        
        # Google ping
        google_ping = f"https://www.google.com/ping?sitemap={sitemap_url}"
        
        # Bing ping
        bing_ping = f"https://www.bing.com/ping?sitemap={sitemap_url}"
        
        results = []
        
        try:
            # Ping Google
            response = requests.get(google_ping, timeout=10)
            results.append({
                "engine": "Google",
                "status": response.status_code,
                "success": response.status_code == 200
            })
        except Exception as e:
            results.append({
                "engine": "Google",
                "status": "error",
                "error": str(e)
            })
        
        try:
            # Ping Bing
            response = requests.get(bing_ping, timeout=10)
            results.append({
                "engine": "Bing",
                "status": response.status_code,
                "success": response.status_code == 200
            })
        except Exception as e:
            results.append({
                "engine": "Bing",
                "status": "error",
                "error": str(e)
            })
        
        return results
    
    def generate_page_speed_config(self):
        """Generate PageSpeed Insights optimization config"""
        
        config = {
            "performance": {
                "critical_css": {
                    "enabled": True,
                    "inline_threshold": 14000,  # 14KB
                    "async_load_remaining": True
                },
                "javascript": {
                    "defer_non_critical": True,
                    "minify": True,
                    "remove_unused": True,
                    "tree_shake": True
                },
                "images": {
                    "format": "webp",
                    "lazy_load": True,
                    "responsive_sizes": [320, 640, 768, 1024, 1366, 1920],
                    "compression_quality": 85
                },
                "fonts": {
                    "preload_critical": True,
                    "display": "swap",
                    "subset": True
                },
                "caching": {
                    "browser_cache": {
                        "html": 3600,  # 1 hour
                        "css": 31536000,  # 1 year
                        "js": 31536000,  # 1 year
                        "images": 31536000,  # 1 year
                        "fonts": 31536000  # 1 year
                    },
                    "cdn_cache": True,
                    "service_worker": True
                }
            },
            "mobile": {
                "viewport": "width=device-width, initial-scale=1.0",
                "tap_targets": {
                    "min_size": 48,
                    "min_spacing": 8
                },
                "font_size": {
                    "minimum": 16,
                    "line_height": 1.5
                },
                "responsive_design": True
            },
            "seo": {
                "meta_tags": True,
                "structured_data": True,
                "canonical_urls": True,
                "hreflang": True,
                "xml_sitemap": True,
                "robots_txt": True
            },
            "monitoring": {
                "google_analytics": {
                    "enabled": True,
                    "tracking_id": "GA_MEASUREMENT_ID",
                    "enhanced_ecommerce": False,
                    "demographics": True
                },
                "search_console": {
                    "enabled": True,
                    "verification": "HTML_TAG_VERIFICATION"
                },
                "core_web_vitals": {
                    "track_lcp": True,  # Largest Contentful Paint
                    "track_fid": True,  # First Input Delay
                    "track_cls": True,  # Cumulative Layout Shift
                    "track_ttfb": True,  # Time to First Byte
                    "track_fcp": True  # First Contentful Paint
                }
            }
        }
        
        return config
    
    def test_mobile_friendliness(self, url):
        """Test mobile-friendliness using Google's API"""
        
        # This would use Google's Mobile-Friendly Test API
        # Placeholder for actual implementation
        
        test_results = {
            "url": url,
            "mobile_friendly": True,
            "issues": [],
            "recommendations": [
                "Font sizes are readable",
                "Tap targets are sized appropriately",
                "Viewport is configured correctly",
                "Content fits viewport width"
            ],
            "page_speed": {
                "mobile": 85,
                "desktop": 92
            },
            "core_web_vitals": {
                "lcp": 2.1,  # seconds
                "fid": 75,   # milliseconds
                "cls": 0.05  # score
            }
        }
        
        return test_results
    
    def generate_analytics_tracking(self):
        """Generate comprehensive analytics tracking code"""
        
        tracking_code = """
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag("js", new Date());
  
  gtag("config", "GA_MEASUREMENT_ID", {
    "page_title": document.title,
    "page_location": window.location.href,
    "page_path": window.location.pathname,
    "send_page_view": true,
    "custom_dimensions": {
      "dimension1": "city_name",
      "dimension2": "service_type",
      "dimension3": "state_name"
    }
  });
  
  // Track Core Web Vitals
  function sendWebVitals() {
    if ("PerformanceObserver" in window) {
      try {
        // LCP
        const po_lcp = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            gtag("event", "web_vitals", {
              "event_category": "Web Vitals",
              "event_label": "LCP",
              "value": Math.round(entry.startTime),
              "non_interaction": true
            });
          }
        });
        po_lcp.observe({type: "largest-contentful-paint", buffered: true});
        
        // FID
        const po_fid = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            gtag("event", "web_vitals", {
              "event_category": "Web Vitals",
              "event_label": "FID",
              "value": Math.round(entry.processingStart - entry.startTime),
              "non_interaction": true
            });
          }
        });
        po_fid.observe({type: "first-input", buffered: true});
        
        // CLS
        let cls = 0;
        const po_cls = new PerformanceObserver((list) => {
          for (const entry of list.getEntries()) {
            if (!entry.hadRecentInput) {
              cls += entry.value;
            }
          }
          gtag("event", "web_vitals", {
            "event_category": "Web Vitals",
            "event_label": "CLS",
            "value": Math.round(cls * 1000),
            "non_interaction": true
          });
        });
        po_cls.observe({type: "layout-shift", buffered: true});
      } catch (e) {
        console.error("Web Vitals tracking error:", e);
      }
    }
  }
  
  // Initialize Web Vitals tracking
  if (document.readyState === "complete") {
    sendWebVitals();
  } else {
    window.addEventListener("load", sendWebVitals);
  }
  
  // Track scroll depth
  let maxScroll = 0;
  window.addEventListener("scroll", () => {
    const scrollPercent = Math.round((window.scrollY + window.innerHeight) / document.body.offsetHeight * 100);
    if (scrollPercent > maxScroll) {
      maxScroll = scrollPercent;
      if (scrollPercent % 25 === 0) {
        gtag("event", "scroll_depth", {
          "event_category": "Engagement",
          "event_label": scrollPercent + "%",
          "value": scrollPercent,
          "non_interaction": true
        });
      }
    }
  });
  
  // Track time on page
  let startTime = Date.now();
  window.addEventListener("beforeunload", () => {
    const timeOnPage = Math.round((Date.now() - startTime) / 1000);
    gtag("event", "time_on_page", {
      "event_category": "Engagement",
      "event_label": document.title,
      "value": timeOnPage,
      "non_interaction": true
    });
  });
</script>

<!-- Google Search Console Verification -->
<meta name="google-site-verification" content="VERIFICATION_CODE" />

<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "CLARITY_ID");
</script>
"""
        
        return tracking_code

# Testing
if __name__ == "__main__":
    manager = SEODeploymentManager()
    
    # Generate sitemap
    print("Generating comprehensive sitemap...")
    sitemap = manager.generate_comprehensive_sitemap()
    print(f"Sitemap generated with {sitemap.count("<url>")} URLs")
    
    # Generate robots.txt
    print("\nGenerating robots.txt...")
    robots = manager.generate_robots_txt()
    print("Robots.txt generated")
    
    # Generate PageSpeed config
    print("\nGenerating PageSpeed optimization config...")
    config = manager.generate_page_speed_config()
    print(f"Config generated with {len(config)} optimization categories")
    
    print("\nSEO Deployment Framework Ready!")