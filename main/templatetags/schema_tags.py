from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()

@register.simple_tag
def faq_schema(faqs):
    """
    Generate FAQ schema markup for better SEO
    
    Usage: {% faq_schema faqs %}
    """
    if not faqs:
        return ""
    
    faq_list = []
    for faq in faqs:
        question = getattr(faq, "question", faq.get("question", ""))
        answer = getattr(faq, "answer", faq.get("answer", ""))
        
        if question and answer:
            faq_list.append({
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": answer
                }
            })
    
    if not faq_list:
        return ""
    
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_list
    }
    
    html = f"<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>"
    return mark_safe(html)

@register.simple_tag
def breadcrumb_schema(items):
    """
    Generate breadcrumb schema markup
    
    Usage: {% breadcrumb_schema breadcrumb_items %}
    """
    if not items:
        return ""
    
    item_list = []
    for i, item in enumerate(items, 1):
        name = item.get("name", "")
        url = item.get("url", "")
        
        if name and url:
            item_list.append({
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": url
            })
    
    if not item_list:
        return ""
    
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": item_list
    }
    
    html = f"<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>"
    return mark_safe(html)

@register.simple_tag
def service_schema(service_name, description, provider_name="Skerritt Economics & Consulting", location="Rhode Island"):
    """
    Generate service schema markup
    
    Usage: {% service_schema "Forensic Economics" "Expert economic analysis for legal cases" %}
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": service_name,
        "description": description,
        "provider": {
            "@type": "ProfessionalService",
            "name": provider_name,
            "address": {
                "@type": "PostalAddress",
                "addressRegion": location,
                "addressCountry": "US"
            }
        },
        "serviceType": service_name,
        "areaServed": {
            "@type": "State",
            "name": location
        }
    }
    
    html = f"<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>"
    return mark_safe(html)

@register.simple_tag
def local_business_schema():
    """
    Generate local business schema markup
    """
    schema = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": "Skerritt Economics & Consulting",
        "description": "Expert forensic economics and business valuation services",
        "url": "https://skerritteconomics.com",
        "telephone": "+1-203-605-2814",
        "address": {
            "@type": "PostalAddress",
            "addressRegion": "RI",
            "addressCountry": "US"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 41.8240,
            "longitude": -71.4128
        },
        "priceRange": "$$$",
        "openingHours": "Mo-Fr 09:00-17:00",
        "sameAs": [
            "https://www.linkedin.com/in/christopherskerritt/",
        ]
    }
    
    html = f"<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>"
    return mark_safe(html)