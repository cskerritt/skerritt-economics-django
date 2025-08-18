"""
SEO Keyword Research and Mapping System
Comprehensive keyword targeting for state-by-service pages
"""

class SEOKeywordMapper:
    """Generate SEO-optimized keyword maps for city-service pages"""
    
    def __init__(self):
        # Primary service keywords with search volume and difficulty
        self.service_keywords = {
            "forensic-economics": {
                "primary": {
                    "keyword": "forensic economist",
                    "volume": 2400,
                    "difficulty": 45,
                    "intent": "transactional"
                },
                "secondary": [
                    {"keyword": "economic damage expert", "volume": 880, "difficulty": 38},
                    {"keyword": "lost earnings calculator", "volume": 720, "difficulty": 32},
                    {"keyword": "economic expert witness", "volume": 1300, "difficulty": 42},
                    {"keyword": "personal injury economist", "volume": 590, "difficulty": 35},
                    {"keyword": "wrongful death economic damages", "volume": 480, "difficulty": 40}
                ],
                "long_tail": [
                    "how to calculate lost earnings for personal injury",
                    "economic damages in wrongful death cases",
                    "forensic economist vs vocational expert",
                    "cost of forensic economist expert witness",
                    "economic loss calculation methods"
                ],
                "questions": [
                    "What does a forensic economist do?",
                    "How much does a forensic economist cost?",
                    "When do you need a forensic economist?",
                    "How are economic damages calculated?",
                    "What is present value in economic damages?"
                ]
            },
            "business-valuation": {
                "primary": {
                    "keyword": "business valuation expert",
                    "volume": 1900,
                    "difficulty": 48,
                    "intent": "transactional"
                },
                "secondary": [
                    {"keyword": "business appraisal services", "volume": 1100, "difficulty": 44},
                    {"keyword": "company valuation analyst", "volume": 620, "difficulty": 40},
                    {"keyword": "business worth calculator", "volume": 3600, "difficulty": 28},
                    {"keyword": "divorce business valuation", "volume": 880, "difficulty": 45},
                    {"keyword": "small business valuation expert", "volume": 720, "difficulty": 42}
                ],
                "long_tail": [
                    "business valuation methods for litigation",
                    "how to value a business for divorce",
                    "fair market value vs fair value standard",
                    "business interruption loss calculation",
                    "minority shareholder discount valuation"
                ],
                "questions": [
                    "How much does business valuation cost?",
                    "What are the three valuation methods?",
                    "When is business valuation needed?",
                    "How long does business valuation take?",
                    "What documents are needed for business valuation?"
                ]
            },
            "vocational-expert": {
                "primary": {
                    "keyword": "vocational expert",
                    "volume": 1600,
                    "difficulty": 40,
                    "intent": "transactional"
                },
                "secondary": [
                    {"keyword": "vocational assessment expert", "volume": 480, "difficulty": 35},
                    {"keyword": "earning capacity evaluation", "volume": 390, "difficulty": 38},
                    {"keyword": "employability expert witness", "volume": 320, "difficulty": 42},
                    {"keyword": "transferable skills analysis", "volume": 260, "difficulty": 30},
                    {"keyword": "vocational rehabilitation expert", "volume": 720, "difficulty": 36}
                ],
                "long_tail": [
                    "vocational expert for social security disability",
                    "earning capacity after injury assessment",
                    "vocational expert testimony in court",
                    "transferable skills analysis methodology",
                    "vocational evaluation for workers compensation"
                ],
                "questions": [
                    "What does a vocational expert do?",
                    "How much does a vocational expert cost?",
                    "What is earning capacity evaluation?",
                    "When is a vocational expert needed?",
                    "How do vocational experts determine disability?"
                ]
            },
            "life-care-planning": {
                "primary": {
                    "keyword": "life care planner",
                    "volume": 880,
                    "difficulty": 38,
                    "intent": "transactional"
                },
                "secondary": [
                    {"keyword": "certified life care planner", "volume": 590, "difficulty": 42},
                    {"keyword": "future medical cost expert", "volume": 320, "difficulty": 35},
                    {"keyword": "catastrophic injury planning", "volume": 260, "difficulty": 40},
                    {"keyword": "medical needs assessment", "volume": 480, "difficulty": 32},
                    {"keyword": "life care plan cost analysis", "volume": 210, "difficulty": 38}
                ],
                "long_tail": [
                    "life care planning for spinal cord injury",
                    "traumatic brain injury life care plan",
                    "pediatric life care planning expert",
                    "life care plan components and costs",
                    "medicare set aside life care planning"
                ],
                "questions": [
                    "What is included in a life care plan?",
                    "How much does life care planning cost?",
                    "Who can create a life care plan?",
                    "When is a life care plan needed?",
                    "How are future medical costs calculated?"
                ]
            }
        }
        
        # Location modifiers for local SEO
        self.location_modifiers = [
            "near me",
            "in {city}",
            "{city} {state}",
            "{county} county",
            "best in {city}",
            "top rated {city}",
            "{city} area",
            "local {city}"
        ]
        
    def generate_keyword_map(self, service_slug, city, state_abbr, state_name, county):
        """Generate complete keyword map for a city-service page"""
        
        if service_slug not in self.service_keywords:
            return None
            
        service_kw = self.service_keywords[service_slug]
        
        # Build location-specific keyword variations
        location_keywords = []
        primary = service_kw["primary"]["keyword"]
        
        # Add city-specific variations
        location_keywords.extend([
            f"{primary} {city}",
            f"{primary} in {city}",
            f"{primary} {city} {state_abbr}",
            f"{city} {primary}",
            f"best {primary} {city}",
            f"{primary} near me",
            f"{primary} {county}",
            f"{primary} {state_name}"
        ])
        
        # Create keyword map with suggested usage
        keyword_map = {
            "primary_keyword": f"{primary} {city}",
            "title_tag": f"{service_kw["primary"]["keyword"].title()} in {city}, {state_abbr} | Expert Witness",
            "meta_description": f"Expert {primary} services in {city}, {state_name}. {service_kw["secondary"][0]["keyword"].title()} for attorneys. Call (203) 605-2814.",
            "h1": f"{service_kw["primary"]["keyword"].title()} in {city}, {state_name}",
            "h2_suggestions": [
                f"{service_kw["secondary"][0]["keyword"].title()} Services in {city}",
                f"Why Choose Our {city} {service_kw["primary"]["keyword"].title()}",
                f"{service_kw["secondary"][1]["keyword"].title()} for {county} Cases",
                f"Expert {service_kw["secondary"][2]["keyword"].title()} in {state_name}",
                f"{city} {service_kw["primary"]["keyword"].title()} Qualifications"
            ],
            "h3_suggestions": [
                f"Types of Cases We Handle in {city}",
                f"Our {county} Court Experience",
                f"{state_name} Economic Analysis Expertise",
                "Professional Certifications & Credentials",
                f"Free Consultation for {city} Attorneys"
            ],
            "long_tail_targets": [
                lt.replace("{city}", city).replace("{state}", state_name) 
                for lt in service_kw["long_tail"]
            ],
            "questions_to_answer": service_kw["questions"],
            "lsi_keywords": [
                "expert witness", "litigation support", "court testimony",
                "deposition", "expert report", "damage calculation",
                "attorney", "law firm", "legal professional",
                city.lower(), county.lower(), state_name.lower()
            ],
            "competitor_analysis": {
                "search_volume": service_kw["primary"]["volume"],
                "difficulty": service_kw["primary"]["difficulty"],
                "intent": service_kw["primary"]["intent"],
                "recommended_word_count": 1500,
                "content_depth": "comprehensive"
            }
        }
        
        return keyword_map
    
    def generate_content_outline(self, keyword_map):
        """Generate SEO-optimized content outline based on keyword map"""
        
        outline = {
            "intro": {
                "word_count": 150,
                "elements": [
                    "Primary keyword in first sentence",
                    "Answer search intent immediately",
                    "Include city and state name",
                    "Mention key credentials",
                    "Clear value proposition"
                ]
            },
            "sections": [
                {
                    "heading": keyword_map["h2_suggestions"][0],
                    "word_count": 250,
                    "keywords": ["secondary keyword 1", "city name", "service benefits"],
                    "elements": ["bullet points", "service list", "local context"]
                },
                {
                    "heading": keyword_map["h2_suggestions"][1],
                    "word_count": 200,
                    "keywords": ["secondary keyword 2", "credentials", "experience"],
                    "elements": ["credibility indicators", "testimonial quote", "statistics"]
                },
                {
                    "heading": keyword_map["h2_suggestions"][2],
                    "word_count": 300,
                    "keywords": ["long-tail keyword", "case types", "local market"],
                    "elements": ["case examples", "industry expertise", "methodology"]
                },
                {
                    "heading": "Frequently Asked Questions",
                    "word_count": 400,
                    "keywords": ["question keywords", "informational intent"],
                    "elements": ["FAQ schema", "5-7 questions", "detailed answers"]
                }
            ],
            "cta_sections": [
                {
                    "placement": "after_intro",
                    "type": "soft_cta",
                    "text": "Free consultation for qualifying cases"
                },
                {
                    "placement": "sidebar",
                    "type": "contact_form",
                    "text": "Get expert analysis for your case"
                },
                {
                    "placement": "end_of_content",
                    "type": "strong_cta",
                    "text": "Call now for immediate assistance"
                }
            ],
            "internal_links": [
                {"anchor": "forensic economics services", "target": "/services/forensic-economics/"},
                {"anchor": "our credentials", "target": "/about/"},
                {"anchor": "case studies", "target": "/case-studies/"},
                {"anchor": f"other {keyword_map["primary_keyword"].split()[-1]} locations", "target": "/locations/"}
            ],
            "external_links": [
                {"anchor": "American Rehabilitation Economics Association", "target": "https://www.a-r-e-a.org/"},
                {"anchor": "economic data source", "target": "https://www.bls.gov/"}
            ]
        }
        
        return outline

# Usage example
if __name__ == "__main__":
    mapper = SEOKeywordMapper()
    
    # Generate keyword map for Los Angeles forensic economics page
    keyword_map = mapper.generate_keyword_map(
        service_slug="forensic-economics",
        city="Los Angeles",
        state_abbr="CA",
        state_name="California",
        county="Los Angeles County"
    )
    
    print("SEO Keyword Map Generated:")
    print(f"Title Tag: {keyword_map["title_tag"]}")
    print(f"Meta Description: {keyword_map["meta_description"]}")
    print(f"H1: {keyword_map["h1"]}")
    print(f"Primary Keyword: {keyword_map["primary_keyword"]}")
    print(f"Search Volume: {keyword_map["competitor_analysis"]["search_volume"]}")
    print(f"Difficulty: {keyword_map["competitor_analysis"]["difficulty"]}/100")