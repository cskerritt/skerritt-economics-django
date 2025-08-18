"""
SEO Enhancements Module for Skerritt Economics
Comprehensive SEO tools for improved rankings and backlink opportunities
"""

from django.utils.text import slugify
from django.urls import reverse
from datetime import datetime
import json


class SEOManager:
    """Central SEO management for the website"""
    
    @staticmethod
    def generate_internal_links(current_page, content_type="service"):
        """Generate contextual internal links for better SEO"""
        
        internal_links = {
            "service": [
                {"text": "forensic economics expert", "url": "/services/forensic-economics/"},
                {"text": "business valuation services", "url": "/services/business-valuation/"},
                {"text": "vocational expert witness", "url": "/services/vocational-expert/"},
                {"text": "life care planning", "url": "/services/life-care-planning/"},
                {"text": "economic damage calculations", "url": "/services/forensic-economics/"},
                {"text": "lost earnings analysis", "url": "/practice-areas/personal-injury/"},
            ],
            "location": [
                {"text": "nationwide expert witness services", "url": "/locations/"},
                {"text": "Massachusetts forensic economist", "url": "/locations/massachusetts-forensic-economist/"},
                {"text": "Rhode Island economic expert", "url": "/locations/rhode-island-forensic-economist/"},
                {"text": "New England economic consulting", "url": "/locations/new-england-economic-expert/"},
            ],
            "practice": [
                {"text": "personal injury economics", "url": "/practice-areas/personal-injury/"},
                {"text": "medical malpractice damages", "url": "/practice-areas/medical-malpractice/"},
                {"text": "employment litigation expert", "url": "/practice-areas/employment-litigation/"},
                {"text": "commercial dispute valuation", "url": "/practice-areas/commercial-disputes/"},
            ],
            "tools": [
                {"text": "life expectancy calculator", "url": "/tools/life-expectancy/"},
                {"text": "present value calculator", "url": "/tools/present-value/"},
                {"text": "wage growth projections", "url": "/tools/wage-growth/"},
                {"text": "business valuation tools", "url": "/tools/business-valuation/"},
            ]
        }
        
        # Filter out current page
        links = internal_links.get(content_type, [])
        return [link for link in links if link["url"] != current_page]
    
    @staticmethod
    def generate_schema_markup(page_type, **kwargs):
        """Generate enhanced schema.org JSON-LD markup"""
        
        schemas = []
        
        if page_type == "service":
            service_schema = {
                "@context": "https://schema.org",
                "@type": "ProfessionalService",
                "name": kwargs.get("name", "Expert Economic Services"),
                "description": kwargs.get("description", ""),
                "provider": {
                    "@type": "Organization",
                    "name": "Skerritt Economics & Consulting",
                    "url": "https://skerritteconomics.com"
                },
                "areaServed": {
                    "@type": "Country",
                    "name": "United States"
                },
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Service Offerings",
                    "itemListElement": kwargs.get("offerings", [])
                }
            }
            schemas.append(service_schema)
        
        elif page_type == "location":
            location_schema = {
                "@context": "https://schema.org",
                "@type": "LocalBusiness",
                "name": f"Skerritt Economics - {kwargs.get("location_name", "")}",
                "description": kwargs.get("description", ""),
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": kwargs.get("city", ""),
                    "addressRegion": kwargs.get("state", ""),
                    "addressCountry": "US"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": kwargs.get("latitude", ""),
                    "longitude": kwargs.get("longitude", "")
                },
                "url": kwargs.get("url", ""),
                "telephone": "+1-203-605-2814",
                "priceRange": "$$$$"
            }
            schemas.append(location_schema)
        
        elif page_type == "article":
            article_schema = {
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": kwargs.get("title", ""),
                "description": kwargs.get("description", ""),
                "author": {
                    "@type": "Person",
                    "name": "Christopher Skerritt",
                    "url": "https://skerritteconomics.com/about"
                },
                "datePublished": kwargs.get("published_date", datetime.now().isoformat()),
                "dateModified": kwargs.get("modified_date", datetime.now().isoformat()),
                "publisher": {
                    "@type": "Organization",
                    "name": "Skerritt Economics & Consulting",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://skerritteconomics.com/static/images/SEC_LOGO.png"
                    }
                },
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": kwargs.get("url", "")
                },
                "keywords": kwargs.get("keywords", [])
            }
            schemas.append(article_schema)
        
        # Add breadcrumb schema
        if kwargs.get("breadcrumbs"):
            breadcrumb_schema = {
                "@context": "https://schema.org",
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i + 1,
                        "name": crumb["name"],
                        "item": crumb["url"]
                    }
                    for i, crumb in enumerate(kwargs["breadcrumbs"])
                ]
            }
            schemas.append(breadcrumb_schema)
        
        return schemas
    
    @staticmethod
    def generate_backlink_opportunities():
        """Generate content ideas for backlink opportunities"""
        
        backlink_strategies = [
            {
                "type": "resource_pages",
                "title": "Economic Damages Calculator Tools",
                "description": "Free interactive calculators for attorneys and insurance professionals",
                "target_sites": ["law schools", "bar associations", "legal directories"],
                "content_ideas": [
                    "Present value calculator with detailed methodology",
                    "Lost earnings calculator with state-specific data",
                    "Life care cost estimator",
                    "Business valuation quick assessment tool"
                ]
            },
            {
                "type": "guest_posts",
                "title": "Expert Insights on Economic Damages",
                "target_sites": ["legal blogs", "insurance publications", "financial websites"],
                "topics": [
                    "How to Calculate Economic Damages in Personal Injury Cases",
                    "The Role of Vocational Experts in Litigation",
                    "Understanding Present Value in Legal Settlements",
                    "Business Valuation Methods for Divorce Proceedings"
                ]
            },
            {
                "type": "case_studies",
                "title": "Detailed Case Analysis",
                "description": "In-depth analysis of significant cases",
                "value_prop": "Provides attorneys with real-world examples and methodologies",
                "format": "Long-form content with data visualizations"
            },
            {
                "type": "industry_guides",
                "title": "Comprehensive Industry Guides",
                "topics": [
                    "Complete Guide to Forensic Economics",
                    "Attorney's Guide to Economic Expert Witnesses",
                    "Insurance Adjuster's Handbook for Economic Damages",
                    "Life Care Planning Best Practices"
                ]
            },
            {
                "type": "local_citations",
                "title": "Local Business Directory Submissions",
                "directories": [
                    "Google My Business",
                    "Bing Places",
                    "Apple Maps",
                    "Yelp for Business",
                    "Yellow Pages",
                    "Better Business Bureau",
                    "Chamber of Commerce directories",
                    "Professional association directories"
                ]
            },
            {
                "type": "professional_associations",
                "title": "Professional Organization Profiles",
                "organizations": [
                    "National Association of Forensic Economics",
                    "American Board of Vocational Experts",
                    "International Association of Rehabilitation Professionals",
                    "American Economic Association",
                    "State bar associations",
                    "Insurance professional organizations"
                ]
            },
            {
                "type": "educational_content",
                "title": "Educational Resources",
                "formats": [
                    "Webinars on economic damage calculations",
                    "Continuing education courses for attorneys",
                    "White papers on valuation methodologies",
                    "Infographics on economic concepts"
                ]
            },
            {
                "type": "press_releases",
                "title": "Newsworthy Content",
                "topics": [
                    "New service offerings",
                    "Significant case victories",
                    "Industry insights and trends",
                    "Economic impact studies"
                ]
            }
        ]
        
        return backlink_strategies
    
    @staticmethod
    def generate_meta_tags(page_type, **kwargs):
        """Generate comprehensive meta tags for any page"""
        
        meta_tags = {
            "basic": {
                "description": kwargs.get("description", "Skerritt Economics - Expert forensic economics and business valuation services"),
                "keywords": kwargs.get("keywords", "forensic economist, business valuation, expert witness"),
                "author": "Christopher Skerritt, M.Ed, MBA, CRC, CLCP, ABVE/F",
                "robots": "index, follow, max-image-preview:large",
                "viewport": "width=device-width, initial-scale=1.0",
            },
            "opengraph": {
                "og:title": kwargs.get("og_title", kwargs.get("title", "Skerritt Economics & Consulting")),
                "og:description": kwargs.get("og_description", kwargs.get("description", "")),
                "og:type": kwargs.get("og_type", "website"),
                "og:url": kwargs.get("url", ""),
                "og:image": kwargs.get("og_image", "https://skerritteconomics.com/static/images/seo-share-image.jpg"),
                "og:site_name": "Skerritt Economics & Consulting",
                "og:locale": "en_US",
            },
            "twitter": {
                "twitter:card": "summary_large_image",
                "twitter:site": "@SkerrittEcon",
                "twitter:creator": "@ChrisSkerritt",
                "twitter:title": kwargs.get("twitter_title", kwargs.get("title", "")),
                "twitter:description": kwargs.get("twitter_description", kwargs.get("description", "")),
                "twitter:image": kwargs.get("twitter_image", "https://skerritteconomics.com/static/images/seo-share-image.jpg"),
            },
            "geo": {
                "geo.region": kwargs.get("geo_region", "US-RI"),
                "geo.placename": kwargs.get("geo_placename", "Smithfield, Rhode Island"),
                "geo.position": kwargs.get("geo_position", "41.8669;-71.5493"),
                "ICBM": kwargs.get("icbm", "41.8669, -71.5493"),
            }
        }
        
        return meta_tags
    
    @staticmethod
    def generate_silo_structure():
        """Generate content silo structure for better SEO"""
        
        silo_structure = {
            "services": {
                "parent": "/services/",
                "title": "Expert Economic Services",
                "children": [
                    {
                        "url": "/services/forensic-economics/",
                        "title": "Forensic Economics",
                        "children": [
                            "/forensic-economist/boston/",
                            "/forensic-economist/providence/",
                            "/practice-areas/personal-injury/",
                            "/tools/lost-earnings-calculator/",
                        ]
                    },
                    {
                        "url": "/services/business-valuation/",
                        "title": "Business Valuation",
                        "children": [
                            "/business-valuation/boston/",
                            "/business-valuation/providence/",
                            "/practice-areas/commercial-disputes/",
                            "/tools/business-valuation/",
                        ]
                    },
                    {
                        "url": "/services/vocational-expert/",
                        "title": "Vocational Expert",
                        "children": [
                            "/vocational-expert/boston/",
                            "/vocational-expert/providence/",
                            "/practice-areas/employment-litigation/",
                            "/tools/wage-growth/",
                        ]
                    },
                    {
                        "url": "/services/life-care-planning/",
                        "title": "Life Care Planning",
                        "children": [
                            "/life-care-planner/boston/",
                            "/life-care-planner/providence/",
                            "/practice-areas/medical-malpractice/",
                            "/tools/medical-costs/",
                        ]
                    }
                ]
            },
            "locations": {
                "parent": "/locations/",
                "title": "Service Areas",
                "children": [
                    {
                        "url": "/locations/massachusetts-forensic-economist/",
                        "title": "Massachusetts",
                        "children": [
                            "/forensic-economist/boston/",
                            "/business-valuation/cambridge/",
                            "/vocational-expert/worcester/",
                        ]
                    },
                    {
                        "url": "/locations/rhode-island-forensic-economist/",
                        "title": "Rhode Island",
                        "children": [
                            "/forensic-economist/providence/",
                            "/business-valuation/warwick/",
                            "/life-care-planner/cranston/",
                        ]
                    }
                ]
            }
        }
        
        return silo_structure


class BacklinkBuilder:
    """Tools for building high-quality backlinks"""
    
    @staticmethod
    def generate_linkable_assets():
        """Create linkable asset ideas"""
        
        linkable_assets = [
            {
                "type": "interactive_tool",
                "title": "Economic Damages Calculator Suite",
                "description": "Comprehensive calculator tools for legal professionals",
                "features": [
                    "Lost earnings calculator with inflation adjustments",
                    "Present value calculator with multiple discount rates",
                    "Life care cost estimator with medical inflation",
                    "Household services valuation tool",
                    "Business valuation quick estimator"
                ],
                "embed_code": True,
                "api_access": True
            },
            {
                "type": "data_study",
                "title": "Annual Economic Damages Report",
                "description": "Comprehensive analysis of economic damage trends",
                "sections": [
                    "Average settlement values by case type",
                    "Regional variations in economic damages",
                    "Impact of inflation on damage calculations",
                    "Vocational assessment trends"
                ],
                "format": "PDF download with web summary"
            },
            {
                "type": "resource_library",
                "title": "Expert Witness Resource Center",
                "contents": [
                    "Sample expert reports",
                    "Deposition preparation guides",
                    "Cross-examination strategies",
                    "Economic terminology glossary",
                    "Case law summaries"
                ]
            },
            {
                "type": "infographic_series",
                "title": "Visual Guides to Economic Concepts",
                "topics": [
                    "Understanding Present Value",
                    "Life Care Planning Process",
                    "Business Valuation Methods",
                    "Economic Loss Components"
                ]
            }
        ]
        
        return linkable_assets
    
    @staticmethod
    def outreach_templates():
        """Generate outreach email templates for link building"""
        
        templates = {
            "resource_page": {
                "subject": "Resource Addition: Economic Damages Calculator for Legal Professionals",
                "body": """Dear [Name],

I noticed your excellent resource page for legal professionals at [URL] and wanted to suggest a valuable addition.

We've developed a comprehensive suite of economic damages calculators specifically designed for attorneys and insurance professionals. These free tools include:

• Lost earnings calculator with state-specific data
• Present value calculator with multiple methodologies
• Life care cost estimator
• Business valuation quick assessment

The calculators are based on accepted forensic economic principles and include detailed methodology explanations.

Would this be a valuable addition to your resource page? I'd be happy to provide additional information or a guest post explaining how attorneys can use these tools effectively.

Best regards,
Christopher Skerritt
Skerritt Economics & Consulting
"""
            },
            "guest_post": {
                "subject": "Guest Post Proposal: Economic Expert Witness Best Practices",
                "body": """Dear [Name],

I've been following [Website] and appreciate your coverage of litigation support topics.

As a forensic economist with 15+ years of experience, I'd like to contribute a guest post on one of these topics:

1. "5 Critical Mistakes Attorneys Make When Hiring Economic Experts"
2. "How to Calculate Economic Damages: A Step-by-Step Guide"
3. "The Hidden Costs of Injury: What Attorneys Often Overlook"

Each article would be 1,500-2,000 words with practical insights and real case examples (anonymized).

I can also provide custom graphics or calculators to accompany the article.

Would any of these topics interest your readers?

Best regards,
Christopher Skerritt, MBA, CRC, CLCP
"""
            },
            "broken_link": {
                "subject": "Broken Link on [Page Title]",
                "body": """Dear [Name],

While researching economic expert resources, I noticed a broken link on your page [URL].

The link to [Broken Resource] appears to be no longer working.

As an alternative, you might consider our comprehensive guide on [Relevant Topic] at [Your URL], which covers similar information and includes interactive calculators.

Hope this helps improve your valuable resource page!

Best regards,
Christopher Skerritt
"""
            }
        }
        
        return templates
    
    @staticmethod
    def competitor_analysis_framework():
        """Framework for analyzing competitor backlinks"""
        
        analysis_framework = {
            "competitors": [
                "forensiceconomics.com",
                "economicexpert.com",
                "businessvaluationexpert.com",
                "vocationalexpert.com"
            ],
            "link_types_to_target": [
                "Legal directories",
                "Bar association resources",
                "Insurance industry sites",
                "Educational institutions",
                "Professional associations",
                "Legal blogs and publications"
            ],
            "content_gaps": [
                "State-specific damage calculation guides",
                "Industry-specific valuation methodologies",
                "Interactive calculation tools",
                "Video explanations of economic concepts",
                "Podcast appearances"
            ],
            "monitoring_tools": [
                "Google Alerts for brand mentions",
                "Ahrefs for backlink tracking",
                "SEMrush for competitor analysis",
                "BuzzSumo for content opportunities"
            ]
        }
        
        return analysis_framework


class ContentOptimizer:
    """Optimize content for SEO and user engagement"""
    
    @staticmethod
    def optimize_content(content, target_keywords):
        """Add SEO optimizations to content"""
        
        optimizations = {
            "keyword_density": "1-2% for primary keywords",
            "related_terms": ContentOptimizer.get_related_terms(target_keywords),
            "content_structure": {
                "use_headers": "H2 and H3 tags every 200-300 words",
                "bullet_points": "Break up long paragraphs",
                "internal_links": "3-5 contextual links per page",
                "external_links": "1-2 authoritative sources",
                "images": "Include alt text with keywords",
                "meta_description": "150-160 characters with primary keyword",
                "url_structure": "Include primary keyword in URL slug"
            }
        }
        
        return optimizations
    
    @staticmethod
    def get_related_terms(primary_keyword):
        """Get LSI and related keywords"""
        
        keyword_map = {
            "forensic economist": [
                "economic damages expert",
                "litigation economist",
                "economic loss analysis",
                "financial expert witness",
                "damage calculations"
            ],
            "business valuation": [
                "company appraisal",
                "fair market value",
                "business worth assessment",
                "enterprise valuation",
                "business appraisal expert"
            ],
            "vocational expert": [
                "employability assessment",
                "earning capacity expert",
                "vocational rehabilitation",
                "labor market analysis",
                "vocational evaluator"
            ],
            "life care planning": [
                "future medical costs",
                "catastrophic injury planning",
                "medical cost projection",
                "life care plan development",
                "future care needs"
            ]
        }
        
        return keyword_map.get(primary_keyword, [])
    
    @staticmethod
    def generate_content_calendar():
        """Generate SEO-focused content calendar"""
        
        content_calendar = {
            "weekly": [
                {
                    "type": "blog_post",
                    "topics": [
                        "Case law updates affecting economic damages",
                        "Economic trends impacting valuations",
                        "Practical tips for attorneys",
                        "Industry news and analysis"
                    ]
                }
            ],
            "monthly": [
                {
                    "type": "comprehensive_guide",
                    "topics": [
                        "State-specific economic damage laws",
                        "Industry valuation guides",
                        "Practice area deep dives",
                        "Methodology explanations"
                    ]
                },
                {
                    "type": "case_study",
                    "format": "Detailed analysis with data"
                }
            ],
            "quarterly": [
                {
                    "type": "research_report",
                    "topics": [
                        "Economic damage trends analysis",
                        "Regional market studies",
                        "Industry benchmarking reports"
                    ]
                },
                {
                    "type": "webinar",
                    "topics": [
                        "Economic damages for attorneys",
                        "Business valuation methodologies",
                        "Life care planning best practices"
                    ]
                }
            ],
            "annual": [
                {
                    "type": "comprehensive_report",
                    "title": "Annual State of Economic Damages Report",
                    "sections": [
                        "Trend analysis",
                        "Case law developments",
                        "Methodology updates",
                        "Regional variations"
                    ]
                }
            ]
        }
        
        return content_calendar