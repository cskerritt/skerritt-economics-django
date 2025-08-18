"""
SEO Template Tags for Enhanced Internal Linking and SEO
"""

from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse
import json
import re

register = template.Library()


@register.simple_tag
def internal_links(current_page="", link_type="related", max_links=5):
    """Generate contextual internal links for better SEO"""
    
    # Define link relationships
    link_map = {
        "forensic-economics": {
            "related": [
                {"text": "lost earnings calculations", "url": "/services/forensic-economics/#lost-earnings"},
                {"text": "present value analysis", "url": "/tools/present-value/"},
                {"text": "economic damage expert witness", "url": "/about/"},
                {"text": "personal injury economics", "url": "/practice-areas/personal-injury/"},
                {"text": "wrongful death calculations", "url": "/practice-areas/personal-injury/#wrongful-death"},
            ],
            "tools": [
                {"text": "lost earnings calculator", "url": "/tools/lost-earnings/"},
                {"text": "present value calculator", "url": "/tools/present-value/"},
                {"text": "life expectancy tables", "url": "/tools/life-expectancy/"},
            ],
            "locations": [
                {"text": "Massachusetts forensic economist", "url": "/locations/massachusetts-forensic-economist/"},
                {"text": "Rhode Island economic expert", "url": "/locations/rhode-island-forensic-economist/"},
                {"text": "Boston forensic economics", "url": "/forensic-economist/boston/"},
            ]
        },
        "business-valuation": {
            "related": [
                {"text": "fair market value assessment", "url": "/services/business-valuation/#fair-market"},
                {"text": "business appraisal expert", "url": "/about/"},
                {"text": "divorce business valuation", "url": "/practice-areas/commercial-disputes/#divorce"},
                {"text": "shareholder disputes", "url": "/practice-areas/commercial-disputes/"},
                {"text": "buy-sell agreements", "url": "/services/business-valuation/#buy-sell"},
            ],
            "tools": [
                {"text": "business valuation calculator", "url": "/tools/business-valuation/"},
                {"text": "DCF calculator", "url": "/tools/dcf-calculator/"},
            ],
            "locations": [
                {"text": "Boston business valuation", "url": "/business-valuation/boston/"},
                {"text": "Providence business appraiser", "url": "/business-valuation/providence/"},
            ]
        },
        "vocational-expert": {
            "related": [
                {"text": "earning capacity analysis", "url": "/services/vocational-expert/#earning-capacity"},
                {"text": "employability assessment", "url": "/services/vocational-expert/#employability"},
                {"text": "labor market survey", "url": "/services/vocational-expert/#labor-market"},
                {"text": "vocational rehabilitation", "url": "/services/vocational-expert/#rehabilitation"},
                {"text": "disability evaluation", "url": "/practice-areas/employment-litigation/"},
            ],
            "tools": [
                {"text": "wage growth calculator", "url": "/tools/wage-growth/"},
                {"text": "employment statistics", "url": "/tools/employment-stats/"},
            ],
            "locations": [
                {"text": "New England vocational expert", "url": "/locations/new-england-economic-expert/"},
                {"text": "Boston vocational assessment", "url": "/vocational-expert/boston/"},
            ]
        },
        "life-care-planning": {
            "related": [
                {"text": "catastrophic injury planning", "url": "/services/life-care-planning/#catastrophic"},
                {"text": "future medical costs", "url": "/services/life-care-planning/#medical-costs"},
                {"text": "life care plan development", "url": "/services/life-care-planning/#development"},
                {"text": "medical cost projection", "url": "/tools/medical-costs/"},
                {"text": "traumatic brain injury", "url": "/practice-areas/medical-malpractice/#tbi"},
            ],
            "tools": [
                {"text": "medical cost calculator", "url": "/tools/medical-costs/"},
                {"text": "life expectancy calculator", "url": "/tools/life-expectancy/"},
            ],
            "locations": [
                {"text": "Massachusetts life care planner", "url": "/life-care-planner/boston/"},
                {"text": "Rhode Island life care planning", "url": "/life-care-planner/providence/"},
            ]
        }
    }
    
    # Extract service type from current page
    service_type = None
    for service in link_map.keys():
        if service in current_page.lower():
            service_type = service
            break
    
    if not service_type:
        # Default links for non-service pages
        default_links = [
            {"text": "forensic economics services", "url": "/services/forensic-economics/"},
            {"text": "business valuation expert", "url": "/services/business-valuation/"},
            {"text": "vocational expert witness", "url": "/services/vocational-expert/"},
            {"text": "life care planning", "url": "/services/life-care-planning/"},
            {"text": "free consultation", "url": "/contact/"},
        ]
        links = default_links[:max_links]
    else:
        links = link_map[service_type].get(link_type, [])[:max_links]
    
    # Generate HTML
    html = "<div class="internal-links">"
    for link in links:
        html += f"<a href="{link["url"]}" class="internal-link">{link["text"]}</a>"
        if link != links[-1]:
            html += " | "
    html += "</div>"
    
    return mark_safe(html)


@register.simple_tag
def breadcrumb_schema(path=""):
    """Generate breadcrumb schema markup"""
    
    # Parse path into breadcrumbs
    parts = [p for p in path.strip("/").split("/") if p]
    
    if not parts:
        return ""
    
    breadcrumbs = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://skerritteconomics.com/"
        }
    ]
    
    # Build breadcrumb trail
    current_path = ""
    for i, part in enumerate(parts):
        current_path += f"/{part}"
        
        # Format the name
        name = part.replace("-", " ").title()
        
        # Special name mappings
        name_map = {
            "Forensic Economist": "Forensic Economics",
            "Business Valuation": "Business Valuation",
            "Vocational Expert": "Vocational Expert Services",
            "Life Care Planner": "Life Care Planning",
        }
        
        name = name_map.get(name, name)
        
        breadcrumbs.append({
            "@type": "ListItem",
            "position": i + 2,
            "name": name,
            "item": f"https://skerritteconomics.com{current_path}/"
        })
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumbs
    }
    
    return mark_safe(f"<script type="application/ld+json">{json.dumps(schema)}</script>")


@register.simple_tag
def related_services(current_service="", max_services=4):
    """Show related services for cross-linking"""
    
    all_services = {
        "forensic-economics": {
            "name": "Forensic Economics",
            "url": "/services/forensic-economics/",
            "description": "Economic damage calculations and lost earnings analysis"
        },
        "business-valuation": {
            "name": "Business Valuation",
            "url": "/services/business-valuation/",
            "description": "Fair market value assessments and business appraisals"
        },
        "vocational-expert": {
            "name": "Vocational Expert",
            "url": "/services/vocational-expert/",
            "description": "Employability assessments and earning capacity analysis"
        },
        "life-care-planning": {
            "name": "Life Care Planning",
            "url": "/services/life-care-planning/",
            "description": "Future medical costs and catastrophic injury planning"
        },
        "business-consulting": {
            "name": "Business Consulting",
            "url": "/services/business-consulting/",
            "description": "Strategic business consulting and advisory services"
        }
    }
    
    # Remove current service from list
    services = {k: v for k, v in all_services.items() if k != current_service}
    
    # Take only max_services
    services = dict(list(services.items())[:max_services])
    
    html = "<div class="related-services">"
    html += "<h3>Related Services</h3>"
    html += "<div class="services-grid">"
    
    for key, service in services.items():
        html += f""'
        <div class="service-card">
            <h4><a href="{service["url"]}">{service["name"]}</a></h4>
            <p>{service["description"]}</p>
            <a href="{service["url"]}" class="learn-more">Learn More →</a>
        </div>
        ""'
    
    html += "</div></div>"
    
    return mark_safe(html)


@register.simple_tag
def location_links(state="", service=""):
    """Generate location-based internal links"""
    
    major_cities = {
        "massachusetts": ["Boston", "Cambridge", "Worcester", "Springfield", "Lowell"],
        "rhode-island": ["Providence", "Warwick", "Cranston", "Pawtucket", "Newport"],
        "connecticut": ["Hartford", "New Haven", "Stamford", "Bridgeport", "Waterbury"],
        "new-hampshire": ["Manchester", "Nashua", "Concord", "Portsmouth", "Dover"],
        "vermont": ["Burlington", "Montpelier", "Rutland", "Barre", "Bennington"],
        "maine": ["Portland", "Augusta", "Bangor", "Lewiston", "South Portland"]
    }
    
    cities = major_cities.get(state.lower(), [])
    
    if not cities:
        return ""
    
    service_slug = service.lower().replace(" ", "-")
    
    html = "<div class="location-links">"
    html += f"<p>Serving {state.title()} including: "
    
    for i, city in enumerate(cities):
        city_slug = city.lower().replace(" ", "-")
        html += f"<a href="/{service_slug}/{city_slug}/">{city}</a>"
        if i < len(cities) - 1:
            html += ", "
    
    html += "</p></div>"
    
    return mark_safe(html)


@register.filter
def add_internal_links(content, keyword_map=None):
    """Automatically add internal links to content based on keywords"""
    
    if not keyword_map:
        keyword_map = {
            "forensic economist": "/services/forensic-economics/",
            "business valuation": "/services/business-valuation/",
            "vocational expert": "/services/vocational-expert/",
            "life care planning": "/services/life-care-planning/",
            "economic damages": "/services/forensic-economics/",
            "lost earnings": "/services/forensic-economics/#lost-earnings",
            "present value": "/tools/present-value/",
            "earning capacity": "/services/vocational-expert/#earning-capacity",
            "fair market value": "/services/business-valuation/#fair-market",
            "expert witness": "/about/",
            "free consultation": "/contact/",
        }
    
    # Process content to add links
    for keyword, url in keyword_map.items():
        # Only link first occurrence
        pattern = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
        replacement = f"<a href="{url}">{keyword}</a>"
        content = pattern.sub(replacement, content, count=1)
    
    return mark_safe(content)


@register.simple_tag
def seo_footer_links():
    """Generate SEO-optimized footer links"""
    
    footer_sections = {
        "Services": [
            {"text": "Forensic Economics", "url": "/services/forensic-economics/"},
            {"text": "Business Valuation", "url": "/services/business-valuation/"},
            {"text": "Vocational Expert", "url": "/services/vocational-expert/"},
            {"text": "Life Care Planning", "url": "/services/life-care-planning/"},
            {"text": "Business Consulting", "url": "/services/business-consulting/"},
        ],
        "Practice Areas": [
            {"text": "Personal Injury", "url": "/practice-areas/personal-injury/"},
            {"text": "Medical Malpractice", "url": "/practice-areas/medical-malpractice/"},
            {"text": "Employment Litigation", "url": "/practice-areas/employment-litigation/"},
            {"text": "Commercial Disputes", "url": "/practice-areas/commercial-disputes/"},
        ],
        "Resources": [
            {"text": "Economic Calculators", "url": "/tools/"},
            {"text": "Case Studies", "url": "/case-studies/"},
            {"text": "Blog", "url": "/blog/"},
            {"text": "Resources", "url": "/resources/"},
        ],
        "Locations": [
            {"text": "Massachusetts", "url": "/locations/massachusetts-forensic-economist/"},
            {"text": "Rhode Island", "url": "/locations/rhode-island-forensic-economist/"},
            {"text": "New England", "url": "/locations/new-england-economic-expert/"},
            {"text": "All Locations", "url": "/locations/"},
        ]
    }
    
    html = "<div class="footer-links-grid">"
    
    for section, links in footer_sections.items():
        html += f"<div class="footer-section">"
        html += f"<h4>{section}</h4>"
        html += "<ul>"
        for link in links:
            html += f"<li><a href="{link["url"]}">{link["text"]}</a></li>"
        html += "</ul>"
        html += "</div>"
    
    html += "</div>"
    
    return mark_safe(html)


@register.simple_tag
def structured_data(data_type="", **kwargs):
    """Generate structured data for various content types"""
    
    if data_type == "faq":
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": kwargs.get("questions", [])
        }
    elif data_type == "howto":
        schema = {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": kwargs.get("name", ""),
            "description": kwargs.get("description", ""),
            "step": kwargs.get("steps", [])
        }
    elif data_type == "review":
        schema = {
            "@context": "https://schema.org",
            "@type": "Review",
            "itemReviewed": {
                "@type": "ProfessionalService",
                "name": "Skerritt Economics & Consulting"
            },
            "reviewRating": {
                "@type": "Rating",
                "ratingValue": kwargs.get("rating", 5),
                "bestRating": 5
            },
            "author": {
                "@type": "Person",
                "name": kwargs.get("author", "Client")
            },
            "reviewBody": kwargs.get("review_text", "")
        }
    else:
        return ""
    
    return mark_safe(f"<script type="application/ld+json">{json.dumps(schema)}</script>")


@register.simple_tag
def city_service_links(service="forensic-economist", limit=10):
    """Generate links to major city service pages"""
    
    major_cities = [
        ("Boston", "boston"),
        ("New York", "new-york"),
        ("Providence", "providence"),
        ("Hartford", "hartford"),
        ("Philadelphia", "philadelphia"),
        ("Chicago", "chicago"),
        ("Los Angeles", "los-angeles"),
        ("Houston", "houston"),
        ("Miami", "miami"),
        ("Atlanta", "atlanta"),
    ]
    
    html = "<div class="city-service-links">"
    html += f"<h3>{service.replace("-", " ").title()} Services by City</h3>"
    html += "<ul class="city-links">"
    
    for city_name, city_slug in major_cities[:limit]:
        html += f"<li><a href="/{service}/{city_slug}/">{city_name} {service.replace("-", " ").title()}</a></li>"
    
    html += "</ul>"
    html += "</div>"
    
    return mark_safe(html)