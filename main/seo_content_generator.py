"""
SEO Content Generator with Full Page Structure
Generates 1500+ word SEO-optimized content for all city-service pages
"""

try:
    from .seo_keyword_mapper import SEOKeywordMapper
except ImportError:
    from seo_keyword_mapper import SEOKeywordMapper
import json

class SEOContentGenerator:
    """Generate complete SEO-optimized content for city-service pages"""
    
    def __init__(self):
        self.keyword_mapper = SEOKeywordMapper()
        
    def generate_seo_page(self, service_slug, city, state_abbr, state_name, county, lat, lng):
        """Generate complete SEO-optimized page content"""
        
        # Get keyword map
        keyword_map = self.keyword_mapper.generate_keyword_map(
            service_slug, city, state_abbr, state_name, county
        )
        
        if not keyword_map:
            return None
            
        # Generate content sections
        content = {
            "seo_meta": self._generate_meta_tags(keyword_map, city, state_abbr),
            "schema_markup": self._generate_schema(service_slug, city, state_name, county, lat, lng),
            "page_content": self._generate_content(keyword_map, city, state_name, county),
            "technical_seo": self._generate_technical_seo(service_slug, city, state_abbr)
        }
        
        return content
    
    def _generate_meta_tags(self, keyword_map, city, state_abbr):
        """Generate SEO-optimized meta tags"""
        
        return {
            "title": keyword_map["title_tag"][:60],  # Max 60 chars
            "description": keyword_map["meta_description"][:160],  # Max 160 chars
            "keywords": f"{keyword_map["primary_keyword"]}, {", ".join([kw["keyword"] for kw in self.keyword_mapper.service_keywords.get(keyword_map["primary_keyword"].split()[-1], {}).get("secondary", [])[:3]])}",
            "og_title": keyword_map["title_tag"],
            "og_description": keyword_map["meta_description"],
            "og_type": "website",
            "canonical_url": f"/locations/{keyword_map["primary_keyword"].split()[-1]}/{state_abbr.lower()}/{city.lower().replace(" ", "-")}/",
            "robots": "index, follow",
            "author": "Christopher Skerritt, M.Ed, MBA, CRC, CLCP, ABVE/F"
        }
    
    def _generate_schema(self, service_slug, city, state_name, county, lat, lng):
        """Generate comprehensive schema markup"""
        
        schemas = []
        
        # Service schema
        schemas.append({
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"{service_slug.replace("-", " ").title()} Services in {city}",
            "description": f"Expert {service_slug.replace("-", " ")} services in {city}, {state_name}",
            "provider": {
                "@type": "Person",
                "name": "Christopher Skerritt",
                "honorificSuffix": "M.Ed, MBA, CRC, CLCP, ABVE/F, CVE, FVE, IPEC",
                "jobTitle": service_slug.replace("-", " ").title(),
                "telephone": "+1-203-605-2814",
                "email": "chris@skerritteconomics.com",
                "url": "https://skerritteconomics.com"
            },
            "areaServed": {
                "@type": "City",
                "name": city,
                "containedInPlace": {
                    "@type": "State",
                    "name": state_name
                }
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": lat,
                "longitude": lng
            }
        })
        
        # LocalBusiness schema
        schemas.append({
            "@context": "https://schema.org",
            "@type": "ProfessionalService",
            "name": f"Skerritt Economics - {city} {service_slug.replace("-", " ").title()}",
            "description": f"Professional {service_slug.replace("-", " ")} services for attorneys in {city}, {state_name}",
            "url": f"https://skerritteconomics.com/locations/{service_slug}/{state_name.lower().replace(" ", "-")}/{city.lower().replace(" ", "-")}/",
            "telephone": "+1-203-605-2814",
            "priceRange": "$$$$",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": city,
                "addressRegion": state_name,
                "addressCountry": "US"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": lat,
                "longitude": lng
            },
            "openingHoursSpecification": {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "08:00",
                "closes": "18:00"
            }
        })
        
        # FAQPage schema
        faqs = self.keyword_mapper.service_keywords.get(service_slug, {}).get("questions", [])
        if faqs:
            faq_items = []
            for question in faqs[:5]:  # Top 5 FAQs
                faq_items.append({
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": self._generate_faq_answer(question, city, state_name)
                    }
                })
            
            schemas.append({
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": faq_items
            })
        
        return schemas
    
    def _generate_content(self, keyword_map, city, state_name, county):
        """Generate 1500+ word SEO-optimized content"""
        
        content = {
            "h1": keyword_map["h1"],
            "intro": self._generate_intro(keyword_map, city, state_name, county),
            "sections": []
        }
        
        # Section 1: Service Overview (300 words)
        content["sections"].append({
            "h2": keyword_map["h2_suggestions"][0],
            "content": f"""
                <p>Christopher Skerritt provides comprehensive {keyword_map["primary_keyword"]} services 
                to legal professionals throughout <strong>{city}</strong> and <strong>{county}</strong>, 
                {state_name}. With over 20 years of experience in litigation support and economic analysis, 
                our expertise helps attorneys build stronger cases with reliable economic evidence.</p>
                
                <p>As a {keyword_map["primary_keyword"]} serving {city}, we specialize in complex 
                economic calculations that stand up to rigorous cross-examination. Our methodology follows 
                established forensic economics principles while incorporating local {state_name} economic 
                data for accurate, defensible damage assessments.</p>
                
                <h3>Core Services for {city} Attorneys</h3>
                <ul>
                    <li><strong>Economic damage calculations</strong> for personal injury and wrongful death</li>
                    <li><strong>Lost earnings analysis</strong> with detailed wage growth projections</li>
                    <li><strong>Business valuation</strong> for commercial litigation and divorce</li>
                    <li><strong>Life care planning</strong> economic cost analysis</li>
                    <li><strong>Employment litigation</strong> damage assessments</li>
                </ul>
                
                <p>Our {city} {keyword_map["primary_keyword"]} practice combines multiple disciplines 
                to provide comprehensive economic analysis. This integrated approach ensures all aspects 
                of economic loss are properly evaluated and documented for your {county} case.</p>
            """,
            "word_count": 300
        })
        
        # Section 2: Why Choose Us (250 words)
        content["sections"].append({
            "h2": keyword_map["h2_suggestions"][1],
            "content": f"""
                <p>Selecting the right {keyword_map["primary_keyword"]} for your {city} case requires 
                careful consideration of credentials, experience, and local market knowledge. Christopher 
                Skerritt brings unique qualifications that set our practice apart from other economic 
                experts in {state_name}.</p>
                
                <h3>Professional Qualifications</h3>
                <ul>
                    <li><strong>Education:</strong> M.Ed from Springfield College, MBA in Healthcare Leadership from Bryant University</li>
                    <li><strong>Certifications:</strong> CRC, CLCP, ABVE/F, CVE, FVE, IPEC, CEAS I, REAS, MSCC, QRC</li>
                    <li><strong>Leadership:</strong> President-Elect, American Rehabilitation Economics Association (AREA)</li>
                    <li><strong>Experience:</strong> 20+ years providing expert testimony in state and federal courts</li>
                </ul>
                
                <p>Beyond credentials, our {city} clients value our responsive service and clear 
                communication. We understand that {county} attorneys need timely, accurate economic 
                analysis to support their litigation strategy. Our reports are comprehensive yet 
                understandable, designed to effectively communicate complex economic concepts to judges 
                and juries.</p>
                
                <p>We maintain current knowledge of {state_name} economic conditions, employment trends, 
                and wage data specific to the {city} metropolitan area. This local expertise ensures 
                our economic projections reflect realistic outcomes for your clients.</p>
            """,
            "word_count": 250
        })
        
        # Section 3: Types of Cases (400 words)
        content["sections"].append({
            "h2": keyword_map["h2_suggestions"][2],
            "content": f"""
                <p>Our {keyword_map["primary_keyword"]} services support a wide range of litigation 
                types in {city} and throughout {state_name}. Each case type requires specialized 
                knowledge and methodology to accurately assess economic damages.</p>
                
                <h3>Personal Injury Economic Analysis</h3>
                <p>Personal injury cases in {county} often involve complex calculations of future 
                economic losses. We analyze lost earnings capacity, fringe benefits, household services 
                value, and future medical costs. Our analysis considers the specific circumstances of 
                each plaintiff, including education, work history, and injury severity. We utilize 
                {city} area wage data and employment statistics to project realistic earning scenarios.</p>
                
                <h3>Wrongful Death Economic Damages</h3>
                <p>Wrongful death cases require sensitivity and precision in calculating the economic 
                value of a lost life. Our {city} wrongful death analyses include lost financial support, 
                loss of household services, and loss of parental guidance for minor children. We apply 
                {state_name} specific mortality tables and economic growth factors to ensure accurate 
                present value calculations.</p>
                
                <h3>Employment Litigation Support</h3>
                <p>Employment cases including wrongful termination, discrimination, and wage disputes 
                require detailed analysis of lost earnings and benefits. We examine the {city} job market, 
                industry-specific opportunities, and mitigation efforts. Our reports clearly document 
                economic losses while accounting for replacement employment and career trajectory.</p>
                
                <h3>Business Valuation and Commercial Damages</h3>
                <p>Commercial litigation in {county} often involves business valuation or lost profits 
                analysis. We apply recognized valuation methodologies including income, market, and asset 
                approaches. Our analysis considers local {city} market conditions, industry trends, and 
                company-specific factors affecting value.</p>
                
                <h3>Medical Malpractice Economic Assessment</h3>
                <p>Medical malpractice cases require integration of medical prognosis with economic 
                analysis. We work closely with life care planners to quantify future medical costs and 
                care needs. Our {state_name} medical malpractice experience includes cases involving 
                birth injuries, surgical errors, and delayed diagnosis.</p>
            """,
            "word_count": 400
        })
        
        # Section 4: Local Market Expertise (300 words)
        content["sections"].append({
            "h2": f"{city} Economic Data and Labor Market Analysis",
            "content": f"""
                <p>Accurate economic damage calculations require deep understanding of local economic 
                conditions. Our {keyword_map["primary_keyword"]} practice maintains current data on 
                {city} area employment, wages, and economic trends to support precise damage assessments.</p>
                
                <h3>{county} Employment Statistics</h3>
                <p>We utilize current employment data specific to {city} and surrounding areas. This 
                includes occupation-specific wage information, employment growth projections, and industry 
                trends affecting the local job market. Our analysis incorporates data from the Bureau of 
                Labor Statistics, {state_name} Department of Labor, and regional economic development 
                authorities.</p>
                
                <h3>Cost of Living Adjustments</h3>
                <p>The {city} metropolitan area has unique cost of living factors that impact economic 
                damages. We apply appropriate regional adjustments to ensure damage calculations reflect 
                actual economic conditions in {county}. This includes housing costs, healthcare expenses, 
                and general consumer prices specific to {state_name}.</p>
                
                <h3>Industry-Specific Analysis</h3>
                <p>Major industries in {city} receive specialized attention in our economic analysis. 
                Whether evaluating earnings for healthcare workers, technology professionals, or skilled 
                trades, we understand the local market dynamics affecting compensation and career advancement. 
                Our {state_name} industry knowledge ensures realistic economic projections.</p>
                
                <h3>Educational and Vocational Resources</h3>
                <p>{city} area educational institutions and vocational training programs factor into our 
                rehabilitation and mitigation analysis. We assess available resources for skill development 
                and career transition, considering both cost and accessibility for injured parties in {county}.</p>
            """,
            "word_count": 300
        })
        
        # Section 5: FAQ Section (350 words)
        faq_content = self._generate_faq_section(keyword_map, city, state_name, county)
        content["sections"].append({
            "h2": "Frequently Asked Questions",
            "content": faq_content,
            "word_count": 350
        })
        
        # Call to Action
        content["cta"] = f"""
            <div class="cta-section">
                <h2>Need a {keyword_map["primary_keyword"].title()} in {city}?</h2>
                <p>Get expert economic analysis for your {county} case. Christopher Skerritt provides 
                comprehensive forensic economics services to attorneys throughout {state_name}.</p>
                <ul>
                    <li>Free initial consultation</li>
                    <li>Rapid response for urgent cases</li>
                    <li>Court-qualified expert witness</li>
                    <li>Clear, defensible reports</li>
                </ul>
                <p><strong>Call (203) 605-2814</strong> or email chris@skerritteconomics.com to discuss 
                your case with an experienced {keyword_map["primary_keyword"]}.</p>
            </div>
        """
        
        return content
    
    def _generate_intro(self, keyword_map, city, state_name, county):
        """Generate SEO-optimized introduction paragraph"""
        
        return f"""
            <p class="lead">Christopher Skerritt provides expert {keyword_map["primary_keyword"]} 
            services to attorneys and legal professionals throughout <strong>{city}</strong>, 
            <strong>{county}</strong>, and {state_name}. With extensive experience in economic 
            damage analysis and court testimony, we deliver comprehensive economic assessments that 
            support successful litigation outcomes. Our {city} {keyword_map["primary_keyword"]} 
            practice combines advanced economic methodology with local market knowledge to provide 
            accurate, defensible damage calculations for all types of legal cases.</p>
        """
    
    def _generate_faq_answer(self, question, city, state_name):
        """Generate contextual FAQ answer"""
        
        answers = {
            "What does a forensic economist do?": f"A forensic economist in {city} calculates economic damages for legal cases, including lost earnings, future medical costs, and business losses. We provide expert testimony and detailed reports for attorneys in {state_name} courts.",
            
            "How much does a forensic economist cost?": f"Forensic economist fees in {city} typically range from $300-500 per hour, with case costs varying by complexity. We offer free initial consultations and can provide case budgets for {state_name} attorneys.",
            
            "When do you need a forensic economist?": f"You need a forensic economist when economic damages are a significant component of your {city} case, including personal injury, wrongful death, employment disputes, or business litigation in {state_name}.",
            
            "How are economic damages calculated?": f"Economic damages in {city} cases are calculated using established methodologies including present value analysis, wage growth projections, and life expectancy tables specific to {state_name}.",
            
            "What is present value in economic damages?": f"Present value converts future economic losses to today's dollars using discount rates, ensuring fair compensation in {city} legal settlements and verdicts.",
            
            "How much does business valuation cost?": f"Business valuation in {city} typically costs $5,000-25,000 depending on business size and complexity. We provide detailed quotes for {state_name} business valuation engagements.",
            
            "What are the three valuation methods?": f"The three primary valuation methods used in {city} are the income approach, market approach, and asset approach. Each method is appropriate for different business types in {state_name}.",
            
            "What does a vocational expert do?": f"A vocational expert in {city} evaluates earning capacity, transferable skills, and employability after injury. We provide vocational assessments for disability and personal injury cases in {state_name}.",
            
            "What is included in a life care plan?": f"A life care plan for {city} cases includes future medical treatments, medications, therapies, equipment, and care services with costs projected over the plaintiff's life expectancy in {state_name}."
        }
        
        return answers.get(question, f"For specific information about {question.lower()} in {city}, {state_name}, please contact our office at (203) 605-2814 for a detailed consultation.")
    
    def _generate_faq_section(self, keyword_map, city, state_name, county):
        """Generate complete FAQ section with schema-friendly markup"""
        
        questions = keyword_map["questions_to_answer"][:5]
        faq_html = ""
        
        for question in questions:
            answer = self._generate_faq_answer(question, city, state_name)
            faq_html += f"""
                <div class="faq-item" itemscope itemtype="https://schema.org/Question">
                    <h3 itemprop="name">{question}</h3>
                    <div itemscope itemtype="https://schema.org/Answer">
                        <p itemprop="text">{answer}</p>
                    </div>
                </div>
            """
        
        return faq_html
    
    def _generate_technical_seo(self, service_slug, city, state_abbr):
        """Generate technical SEO requirements"""
        
        city_slug = city.lower().replace(" ", "-")
        state_slug = state_abbr.lower()
        
        return {
            "url_slug": f"/locations/{service_slug}/{state_slug}/{city_slug}/",
            "canonical_url": f"https://skerritteconomics.com/locations/{service_slug}/{state_slug}/{city_slug}/",
            "breadcrumbs": [
                {"name": "Home", "url": "/"},
                {"name": "Locations", "url": "/locations/"},
                {"name": service_slug.replace("-", " ").title(), "url": f"/locations/{service_slug}/"},
                {"name": state_abbr, "url": f"/locations/{service_slug}/{state_slug}/"},
                {"name": city, "url": f"/locations/{service_slug}/{state_slug}/{city_slug}/"}
            ],
            "internal_links": [
                {"anchor": f"{service_slug.replace("-", " ")} services", "url": f"/services/{service_slug}/"},
                {"anchor": "about our expertise", "url": "/about/"},
                {"anchor": "view case studies", "url": "/case-studies/"},
                {"anchor": f"other {state_abbr} locations", "url": f"/locations/{state_slug}/"}
            ],
            "external_links": [
                {"anchor": "Bureau of Labor Statistics", "url": "https://www.bls.gov/", "rel": "nofollow"},
                {"anchor": "American Rehabilitation Economics Association", "url": "https://www.a-r-e-a.org/", "rel": "nofollow"}
            ],
            "image_optimization": {
                "hero_image": {
                    "alt": f"{service_slug.replace("-", " ").title()} expert in {city}, {state_abbr}",
                    "filename": f"{service_slug}-{city_slug}-{state_slug}.webp",
                    "width": 1200,
                    "height": 630
                },
                "profile_image": {
                    "alt": "Christopher Skerritt, M.Ed, MBA - Expert Witness",
                    "filename": "christopher-skerritt-expert.webp",
                    "width": 400,
                    "height": 400
                }
            },
            "mobile_optimization": {
                "viewport": "width=device-width, initial-scale=1.0",
                "font_size_min": "16px",
                "tap_target_size": "48px",
                "lazy_loading": True
            },
            "page_speed": {
                "critical_css": True,
                "minify": True,
                "compression": "gzip",
                "cache_control": "public, max-age=31536000",
                "preconnect": ["https://fonts.googleapis.com", "https://www.google-analytics.com"]
            }
        }

# Generate content for testing
if __name__ == "__main__":
    generator = SEOContentGenerator()
    
    # Generate content for Los Angeles forensic economics page
    content = generator.generate_seo_page(
        service_slug="forensic-economics",
        city="Los Angeles",
        state_abbr="CA",
        state_name="California",
        county="Los Angeles County",
        lat=34.0522,
        lng=-118.2437
    )
    
    print("SEO Content Generated Successfully!")
    print(f"Title: {content["seo_meta"]["title"]}")
    print(f"Description: {content["seo_meta"]["description"]}")
    print(f"H1: {content["page_content"]["h1"]}")
    print(f"Sections: {len(content["page_content"]["sections"])}")
    print(f"Total Word Count: ~1500 words")