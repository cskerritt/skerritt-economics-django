"""
Enhanced sitemap generator with comprehensive metadata for SEO and AI crawlers
"""
from datetime import datetime
from xml.etree import ElementTree as ET
from django.http import HttpResponse
from django.urls import reverse
from blog.models import Post, CaseStudy
from .us_cities_data import US_STATES, PRACTICE_AREAS
from .us_cities_seo_data import US_MAJOR_CITIES


def generate_enhanced_sitemap_xml(request):
    """Generate an enhanced sitemap with comprehensive metadata"""
    
    # Create root element with additional namespaces for rich metadata
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:xhtml", "http://www.w3.org/1999/xhtml")
    urlset.set("xmlns:image", "http://www.google.com/schemas/sitemap-image/1.1")
    urlset.set("xmlns:video", "http://www.google.com/schemas/sitemap-video/1.1")
    urlset.set("xmlns:news", "http://www.google.com/schemas/sitemap-news/0.9")
    urlset.set("xmlns:mobile", "http://www.google.com/schemas/sitemap-mobile/1.0")
    urlset.set("xmlns:pagemap", "http://www.google.com/schemas/sitemap-pagemap/1.0")
    
    base_url = "https://skerritteconomics.com"
    current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    
    # Helper function to add enhanced URL with metadata
    def add_enhanced_url(path, changefreq="weekly", priority="0.8", 
                        title=None, description=None, keywords=None,
                        image_url=None, category=None, author=None):
        url = ET.SubElement(urlset, "url")
        
        # Basic sitemap elements
        loc = ET.SubElement(url, "loc")
        loc.text = f"{base_url}{path}"
        
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = current_date
        
        cf = ET.SubElement(url, "changefreq")
        cf.text = changefreq
        
        pr = ET.SubElement(url, "priority")
        pr.text = str(priority)
        
        # Add mobile indicator
        mobile = ET.SubElement(url, "mobile:mobile")
        
        # Add PageMap data for enhanced Google indexing
        if title or description or keywords:
            pagemap = ET.SubElement(url, "pagemap:pagemap")
            dataobject = ET.SubElement(pagemap, "pagemap:DataObject")
            dataobject.set("type", "document")
            
            if title:
                attribute = ET.SubElement(dataobject, "pagemap:Attribute")
                attribute.set("name", "title")
                attribute.text = title
            
            if description:
                attribute = ET.SubElement(dataobject, "pagemap:Attribute")
                attribute.set("name", "description")
                attribute.text = description
            
            if keywords:
                attribute = ET.SubElement(dataobject, "pagemap:Attribute")
                attribute.set("name", "keywords")
                attribute.text = keywords
            
            if category:
                attribute = ET.SubElement(dataobject, "pagemap:Attribute")
                attribute.set("name", "category")
                attribute.text = category
            
            if author:
                attribute = ET.SubElement(dataobject, "pagemap:Attribute")
                attribute.set("name", "author")
                attribute.text = author
        
        # Add image if provided
        if image_url:
            image = ET.SubElement(url, "image:image")
            image_loc = ET.SubElement(image, "image:loc")
            image_loc.text = f"{base_url}{image_url}"
            if title:
                image_title = ET.SubElement(image, "image:title")
                image_title.text = title
            if description:
                image_caption = ET.SubElement(image, "image:caption")
                image_caption.text = description
        
        # Add alternate language versions
        for lang in ["en-US", "en"]:
            xhtml_link = ET.SubElement(url, "xhtml:link")
            xhtml_link.set("rel", "alternate")
            xhtml_link.set("hreflang", lang)
            xhtml_link.set("href", f"{base_url}{path}")
    
    # Priority 1.0 - Homepage
    add_enhanced_url(
        "/", 
        changefreq="daily", 
        priority=1.0,
        title="Skerritt Economics & Consulting - Expert Forensic Economist",
        description="Premier forensic economics and business valuation firm providing expert witness services for litigation support across all 50 states.",
        keywords="forensic economist, business valuation, expert witness, economic damages, Christopher Skerritt",
        image_url="/static/images/SEC_LOGO.png",
        category="Professional Services",
        author="Christopher Skerritt"
    )
    
    # Priority 0.95 - Core service pages
    core_services = [
        {
            "path": "/services/",
            "title": "Expert Economic Services - Forensic Economics & Business Valuation",
            "description": "Comprehensive economic services including forensic economics, business valuation, vocational assessment, and life care planning.",
            "keywords": "economic services, forensic economics, business valuation, expert witness services",
            "category": "Services"
        },
        {
            "path": "/services/forensic-economics/",
            "title": "Forensic Economics Expert - Economic Damage Calculations",
            "description": "Expert forensic economics services for personal injury, wrongful death, and employment litigation cases.",
            "keywords": "forensic economics, economic damages, lost earnings, expert testimony",
            "category": "Forensic Economics"
        },
        {
            "path": "/services/business-valuation/",
            "title": "Business Valuation Expert - Fair Market Value Assessments",
            "description": "Professional business valuation services for litigation, divorce, and estate planning.",
            "keywords": "business valuation, fair market value, business appraisal, valuation expert",
            "category": "Business Valuation"
        },
        {
            "path": "/services/vocational-expert/",
            "title": "Vocational Expert Services - Earning Capacity Analysis",
            "description": "Vocational assessment and earning capacity analysis for disability and injury cases.",
            "keywords": "vocational expert, earning capacity, employability, vocational assessment",
            "category": "Vocational Services"
        },
        {
            "path": "/services/life-care-planning/",
            "title": "Life Care Planning - Future Medical Cost Projections",
            "description": "Comprehensive life care planning and future medical cost projections for catastrophic injury cases.",
            "keywords": "life care planning, medical costs, future care, CLCP",
            "category": "Life Care Planning"
        }
    ]
    
    for service in core_services:
        add_enhanced_url(
            service["path"],
            changefreq="weekly",
            priority=0.95,
            title=service["title"],
            description=service["description"],
            keywords=service["keywords"],
            category=service["category"],
            author="Christopher Skerritt, MBA, CRC, CLCP"
        )
    
    # Priority 0.9 - Important pages
    important_pages = [
        ("/about/", "About Christopher Skerritt - Forensic Economist", "About"),
        ("/contact/", "Contact Skerritt Economics - Free Consultation", "Contact"),
        ("/practice-areas/", "Practice Areas - Types of Cases We Handle", "Practice Areas"),
        ("/locations/", "Service Locations - All 50 States Coverage", "Locations"),
        ("/case-studies/", "Case Studies - Successful Engagements", "Case Studies"),
        ("/resources/", "Resources - Tools and Information", "Resources")
    ]
    
    for path, title, category in important_pages:
        add_enhanced_url(
            path,
            changefreq="weekly",
            priority=0.9,
            title=title,
            category=category,
            author="Christopher Skerritt"
        )
    
    # Priority 0.85 - Practice area pages
    practice_areas = [
        ("personal-injury", "Personal Injury Economics", "personal injury, economic damages, lost earnings"),
        ("medical-malpractice", "Medical Malpractice Damages", "medical malpractice, economic losses, future care"),
        ("wrongful-death", "Wrongful Death Economic Analysis", "wrongful death, economic damages, loss of support"),
        ("employment", "Employment Litigation Economics", "employment damages, wrongful termination, discrimination"),
        ("commercial", "Commercial Dispute Valuation", "business disputes, commercial damages, lost profits")
    ]
    
    for slug, title, keywords in practice_areas:
        add_enhanced_url(
            f"/practice-areas/{slug}/",
            changefreq="monthly",
            priority=0.85,
            title=f"{title} - Expert Economic Analysis",
            description=f"Expert economic analysis and testimony for {title.lower()} cases.",
            keywords=keywords,
            category="Practice Areas"
        )
    
    # Priority 0.8 - State pages
    for state_data in US_STATES:
        state = state_data["abbreviation"].lower()
        state_name = state_data["name"]
        add_enhanced_url(
            f"/locations/{state}/",
            changefreq="monthly",
            priority=0.8,
            title=f"{state_name} Forensic Economist - Expert Witness Services",
            description=f"Expert forensic economics and business valuation services in {state_name}.",
            keywords=f"{state_name} forensic economist, {state_name} expert witness, {state_name} economic damages",
            category="State Locations"
        )
    
    # Priority 0.75 - City pages (sample of major cities)
    city_count = 0
    for city_data in US_MAJOR_CITIES[:100]:  # Limit to top 100 cities for sitemap size
        if city_count >= 100:
            break
        
        city_slug = city_data.get("slug", "")
        city_name = city_data.get("city", "")
        state_name = city_data.get("state", "")
        
        if city_slug and city_name:
            add_enhanced_url(
                f"/forensic-economist/{city_slug}/",
                changefreq="monthly",
                priority=0.75,
                title=f"{city_name}, {state_name} Forensic Economist",
                description=f"Local forensic economics expert serving {city_name}, {state_name} and surrounding areas.",
                keywords=f"{city_name} forensic economist, {city_name} expert witness, {state_name} economic expert",
                category="City Locations"
            )
            city_count += 1
    
    # Priority 0.7 - Blog posts
    try:
        posts = Post.objects.filter(status="published").order_by("-created_at")[:50]
        for post in posts:
            add_enhanced_url(
                f"/blog/{post.slug}/",
                changefreq="monthly",
                priority=0.7,
                title=post.title,
                description=post.excerpt[:160] if hasattr(post, "excerpt") else post.title,
                keywords=post.tags if hasattr(post, "tags") else "forensic economics, expert insights",
                category="Blog",
                author=str(post.author) if post.author else "Christopher Skerritt"
            )
    except:
        pass  # Blog posts might not exist yet
    
    # Priority 0.7 - Case studies
    try:
        case_studies = CaseStudy.objects.filter(is_published=True).order_by("-created_at")[:20]
        for case in case_studies:
            add_enhanced_url(
                f"/case-studies/{case.slug}/",
                changefreq="monthly",
                priority=0.7,
                title=case.title,
                description=case.summary[:160] if hasattr(case, "summary") else case.title,
                keywords=f"{case.case_type}, case study, expert testimony" if hasattr(case, "case_type") else "case study",
                category="Case Studies",
                author="Christopher Skerritt"
            )
    except:
        pass  # Case studies might not exist yet
    
    # Priority 0.6 - Tool pages
    tool_pages = [
        ("/tools/", "Professional Tools for Economic Analysis", "economic tools, calculators"),
        ("/tools/life-expectancy/", "Life Expectancy Calculator", "life expectancy, actuarial tables")
    ]
    
    for path, title, keywords in tool_pages:
        add_enhanced_url(
            path,
            changefreq="monthly",
            priority=0.6,
            title=title,
            keywords=keywords,
            category="Tools"
        )
    
    # Priority 0.5 - Legal and utility pages
    utility_pages = [
        ("/privacy/", "Privacy Policy"),
        ("/terms/", "Terms of Service"),
        ("/sitemap/", "Site Map"),
        ("/referral/", "Referral Program"),
        ("/referral/thank-you/", "Thank You")
    ]
    
    for path, title in utility_pages:
        add_enhanced_url(
            path,
            changefreq="yearly",
            priority=0.5,
            title=title,
            category="Legal"
        )
    
    # Generate XML string
    xml_string = ET.tostring(urlset, encoding="unicode", method="xml")
    
    # Add XML declaration and format
    xml_declaration = "<?xml version="1.0" encoding="UTF-8"?>\n"
    xml_string = xml_declaration + xml_string
    
    # Add stylesheet for better viewing in browsers
    stylesheet = "<?xml-stylesheet type="text/xsl" href="/static/sitemap.xsl"?>\n"
    xml_string = xml_declaration + stylesheet + xml_string[len(xml_declaration):]
    
    # Return HTTP response
    response = HttpResponse(xml_string, content_type="application/xml")
    response["Cache-Control"] = "max-age=3600"  # Cache for 1 hour
    return response