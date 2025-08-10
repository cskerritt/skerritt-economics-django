#!/usr/bin/env python
"""
Populate the database with sample data for Skerritt Economics website
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from blog.models import Category, Post, CaseStudy
from main.models import Testimonial, FAQ
from django.utils import timezone
from django.utils.text import slugify

def create_categories():
    """Create blog categories"""
    categories = [
        {'name': 'Methodology', 'description': 'Economic analysis methodologies and techniques'},
        {'name': 'Case Law', 'description': 'Important legal cases affecting economic damages'},
        {'name': 'Industry Updates', 'description': 'Updates in forensic economics and business valuation'},
        {'name': 'Case Studies', 'description': 'Detailed analysis of representative cases'},
    ]
    
    for cat_data in categories:
        cat, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"Created category: {cat.name}")

def create_blog_posts():
    """Create sample blog posts"""
    methodology_cat = Category.objects.get(name='Methodology')
    case_law_cat = Category.objects.get(name='Case Law')
    
    posts = [
        {
            'title': 'Understanding Present Value Calculations in Personal Injury Cases',
            'category': methodology_cat,
            'excerpt': 'A comprehensive guide to applying discount rates and calculating present value for future economic losses.',
            'content': """
                <p>Present value calculations are fundamental to forensic economics, particularly in personal injury and wrongful death cases. This article explores the methodology behind these calculations and their practical application in litigation.</p>
                
                <h3>The Time Value of Money</h3>
                <p>The core principle underlying present value calculations is that a dollar today is worth more than a dollar in the future. This concept is critical when calculating damages that will occur over many years.</p>
                
                <h3>Selecting Appropriate Discount Rates</h3>
                <p>The choice of discount rate can significantly impact the final damage calculation. Forensic economists typically consider:</p>
                <ul>
                    <li>Risk-free rates (U.S. Treasury securities)</li>
                    <li>Historical average rates</li>
                    <li>Current market conditions</li>
                    <li>Jurisdiction-specific requirements</li>
                </ul>
                
                <h3>Application in Practice</h3>
                <p>When calculating lost future earnings, we must account for both wage growth and discounting. The net discount rate approach simplifies this by combining both factors into a single rate.</p>
            """,
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Recent Developments in Hedonic Damages',
            'category': case_law_cat,
            'excerpt': 'Analysis of recent court decisions regarding the admissibility of hedonic damage testimony.',
            'content': """
                <p>Hedonic damages, representing the loss of enjoyment of life, remain a contentious issue in many jurisdictions. This article examines recent court decisions and their implications for economic experts.</p>
                
                <h3>Current Legal Landscape</h3>
                <p>While some jurisdictions readily accept hedonic damage testimony, others remain skeptical. The key factors courts consider include:</p>
                <ul>
                    <li>Scientific reliability of valuation methods</li>
                    <li>Relevance to the specific case</li>
                    <li>Potential for jury confusion</li>
                </ul>
                
                <h3>Methodological Approaches</h3>
                <p>Economists have developed various methods to quantify hedonic damages, including willingness-to-pay studies and value of statistical life calculations.</p>
            """,
            'status': 'published',
            'featured': True
        },
        {
            'title': 'Vocational Assessment in the Age of Remote Work',
            'category': Category.objects.get(name='Industry Updates'),
            'excerpt': 'How the shift to remote work affects earning capacity evaluations and vocational assessments.',
            'content': """
                <p>The COVID-19 pandemic has fundamentally altered the employment landscape, with remote work becoming a permanent fixture for many occupations. This shift has significant implications for vocational assessments in litigation.</p>
                
                <h3>Expanded Labor Markets</h3>
                <p>Remote work has effectively expanded the geographic scope of labor markets for many positions. Vocational experts must now consider:</p>
                <ul>
                    <li>National rather than local wage data for remote-eligible positions</li>
                    <li>Increased competition from a broader candidate pool</li>
                    <li>New skill requirements for remote work success</li>
                </ul>
                
                <h3>Implications for Disability Cases</h3>
                <p>Remote work options may increase employment opportunities for individuals with certain physical disabilities, while creating new challenges for those with cognitive or social impairments.</p>
            """,
            'status': 'published',
            'featured': False
        }
    ]
    
    for post_data in posts:
        post, created = Post.objects.get_or_create(
            slug=slugify(post_data['title']),
            defaults=post_data
        )
        if created:
            print(f"Created blog post: {post.title}")

def create_case_studies():
    """Create sample case studies"""
    case_studies = [
        {
            'title': 'Construction Worker Traumatic Brain Injury',
            'practice_area': 'personal_injury',
            'background': 'A 42-year-old construction foreman sustained a traumatic brain injury in a workplace incident. Pre-injury annual earnings were $85,000.',
            'analysis': 'Performed vocational assessment and calculated economic losses. Analysis included lost earnings calculations based on work-life expectancy and residual earning capacity in alternative employment. Included fringe benefits and employer contributions.',
            'challenges': 'Analysis addressed post-injury employment in a lower-paying position and mitigation of damages.',
            'outcome': 'Case resolved through settlement.',
            'amount': '$2.3M Economic Analysis',
            'featured': True
        },
        {
            'title': 'Medical Malpractice Birth Injury',
            'practice_area': 'medical_malpractice',
            'background': 'Infant sustained brain injury during delivery. Medical records indicated requirement for long-term care.',
            'analysis': 'Prepared life care plan with projected medical and care costs. Collaborated with medical professionals to identify care requirements through life expectancy. Applied medical cost inflation rates and present value calculations.',
            'challenges': 'Analysis covered projected care needs over expected lifespan with consideration for changing requirements over time.',
            'outcome': 'Case proceeded to trial.',
            'amount': '$18.5M Projected Care Costs',
            'featured': True
        },
        {
            'title': 'Business Interruption Case',
            'practice_area': 'commercial',
            'background': 'Manufacturing company experienced supply chain disruption affecting production and contracts.',
            'analysis': 'Reviewed financial records to establish baseline performance metrics. Applied standard methodologies including before-and-after and yardstick approaches to calculate business losses over 18-month period.',
            'challenges': 'Analysis required separation of claimed losses from market conditions affecting the industry.',
            'outcome': 'Matter resolved through arbitration.',
            'amount': '$4.2M Economic Analysis',
            'featured': True
        }
    ]
    
    for case_data in case_studies:
        case, created = CaseStudy.objects.get_or_create(
            slug=slugify(case_data['title']),
            defaults=case_data
        )
        if created:
            print(f"Created case study: {case.title}")

def create_testimonials():
    """Create testimonials"""
    testimonials = [
        {
            'author': 'Attorney',
            'title': 'Personal Injury Law Firm',
            'content': "Mr. Skerritt provided economic analysis for our personal injury case. His report included detailed calculations of lost earnings and future medical costs with supporting documentation.",
            'featured': True,
            'display_order': 1
        },
        {
            'author': 'Senior Attorney',
            'title': 'Commercial Litigation Practice',
            'content': 'We have retained Mr. Skerritt for multiple cases involving economic damages. His reports include methodology explanations and source citations for all calculations.',
            'featured': True,
            'display_order': 2
        },
        {
            'author': 'Law Firm Partner',
            'title': 'Medical Malpractice Firm',
            'content': 'Mr. Skerritt prepared a life care plan for our case that included itemized future medical costs and care requirements based on medical records and physician recommendations.',
            'featured': True,
            'display_order': 3
        }
    ]
    
    for test_data in testimonials:
        testimonial, created = Testimonial.objects.get_or_create(
            author=test_data['author'],
            defaults=test_data
        )
        if created:
            print(f"Created testimonial from: {testimonial.author}")

def create_faqs():
    """Create FAQs"""
    faqs = [
        {
            'question': 'What is a forensic economist?',
            'answer': 'A forensic economist is an expert who applies economic analysis to legal matters, particularly in calculating economic damages in litigation. We analyze lost earnings, benefits, household services, and business losses to determine the financial impact of injuries, death, or business disputes.',
            'category': 'General',
            'display_order': 1
        },
        {
            'question': 'When should I retain a forensic economist?',
            'answer': 'The earlier the better. Early retention allows for comprehensive case evaluation, identification of necessary documentation, and strategic planning. Many attorneys retain us during case evaluation to assess economic damages before filing.',
            'category': 'General',
            'display_order': 2
        },
        {
            'question': 'What types of cases benefit from economic analysis?',
            'answer': 'Personal injury, wrongful death, medical malpractice, employment discrimination, business valuation, commercial disputes, and any case involving claims for economic damages. Even seemingly straightforward cases benefit from professional economic analysis.',
            'category': 'General',
            'display_order': 3
        },
        {
            'question': 'How are your fees structured?',
            'answer': 'We typically work on an hourly basis, with rates competitive for forensic economic experts. We provide detailed invoices and can offer case budgets upon request. Initial consultations are always free.',
            'category': 'Fees',
            'display_order': 4
        },
        {
            'question': 'Do you testify in court?',
            'answer': 'Yes, we regularly provide expert testimony in depositions, arbitrations, mediations, and trials. Our reports and testimony are designed to be clear, credible, and persuasive to judges and juries.',
            'category': 'Testimony',
            'display_order': 5
        },
        {
            'question': 'What geographic areas do you serve?',
            'answer': 'While based in Rhode Island, we serve clients throughout New England (MA, CT, NH, VT, ME) and accept cases nationwide. We can provide remote testimony when appropriate.',
            'category': 'Coverage',
            'display_order': 6
        }
    ]
    
    for faq_data in faqs:
        faq, created = FAQ.objects.get_or_create(
            question=faq_data['question'],
            defaults=faq_data
        )
        if created:
            print(f"Created FAQ: {faq.question}")

if __name__ == '__main__':
    print("Populating database with sample data...")
    create_categories()
    create_blog_posts()
    create_case_studies()
    create_testimonials()
    create_faqs()
    print("Database population complete!")