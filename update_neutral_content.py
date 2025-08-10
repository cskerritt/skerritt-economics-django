#!/usr/bin/env python
"""
Update existing testimonials and case studies to be more neutral
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skerritt_site.settings')
django.setup()

from blog.models import CaseStudy
from main.models import Testimonial

def update_testimonials():
    """Update testimonials to be neutral"""
    
    # Update Sarah Mitchell testimonial
    try:
        t1 = Testimonial.objects.get(author='Sarah Mitchell')
        t1.content = "Mr. Skerritt provided economic analysis for our personal injury case. His report included detailed calculations of lost earnings and future medical costs with supporting documentation."
        t1.save()
        print(f"Updated testimonial: {t1.author}")
    except Testimonial.DoesNotExist:
        pass
    
    # Update Robert Chen testimonial
    try:
        t2 = Testimonial.objects.get(author='Robert Chen')
        t2.content = "We have retained Mr. Skerritt for multiple cases involving economic damages. His reports include methodology explanations and source citations for all calculations."
        t2.save()
        print(f"Updated testimonial: {t2.author}")
    except Testimonial.DoesNotExist:
        pass
    
    # Update Jennifer Walsh testimonial
    try:
        t3 = Testimonial.objects.get(author='Jennifer Walsh')
        t3.content = "Mr. Skerritt prepared a life care plan for our case that included itemized future medical costs and care requirements based on medical records and physician recommendations."
        t3.save()
        print(f"Updated testimonial: {t3.author}")
    except Testimonial.DoesNotExist:
        pass

def update_case_studies():
    """Update case studies to be neutral"""
    
    # Update Construction Worker case
    try:
        c1 = CaseStudy.objects.get(title='Construction Worker Traumatic Brain Injury')
        c1.background = 'A 42-year-old construction foreman sustained a traumatic brain injury in a workplace incident. Pre-injury annual earnings were $85,000.'
        c1.analysis = 'Performed vocational assessment and calculated economic losses. Analysis included lost earnings calculations based on work-life expectancy and residual earning capacity in alternative employment. Included fringe benefits and employer contributions.'
        c1.challenges = 'Analysis addressed post-injury employment in a lower-paying position and mitigation of damages.'
        c1.outcome = 'Case resolved through settlement.'
        c1.amount = '$2.3M Economic Analysis'
        c1.save()
        print(f"Updated case study: {c1.title}")
    except CaseStudy.DoesNotExist:
        pass
    
    # Update Medical Malpractice case
    try:
        c2 = CaseStudy.objects.get(title='Medical Malpractice Birth Injury')
        c2.background = 'Infant sustained brain injury during delivery. Medical records indicated requirement for long-term care.'
        c2.analysis = 'Prepared life care plan with projected medical and care costs. Collaborated with medical professionals to identify care requirements through life expectancy. Applied medical cost inflation rates and present value calculations.'
        c2.challenges = 'Analysis covered projected care needs over expected lifespan with consideration for changing requirements over time.'
        c2.outcome = 'Case proceeded to trial.'
        c2.amount = '$18.5M Projected Care Costs'
        c2.save()
        print(f"Updated case study: {c2.title}")
    except CaseStudy.DoesNotExist:
        pass
    
    # Update Business Interruption case - check both possible titles
    for title in ['Business Interruption from Supply Chain Disruption', 'Business Interruption Case']:
        try:
            c3 = CaseStudy.objects.get(title=title)
            c3.title = 'Business Interruption Case'
            c3.background = 'Manufacturing company experienced supply chain disruption affecting production and contracts.'
            c3.analysis = 'Reviewed financial records to establish baseline performance metrics. Applied standard methodologies including before-and-after and yardstick approaches to calculate business losses over 18-month period.'
            c3.challenges = 'Analysis required separation of claimed losses from market conditions affecting the industry.'
            c3.outcome = 'Matter resolved through arbitration.'
            c3.amount = '$4.2M Economic Analysis'
            c3.save()
            print(f"Updated case study: {c3.title}")
            break
        except CaseStudy.DoesNotExist:
            continue

if __name__ == '__main__':
    print("Updating content to be more neutral...")
    update_testimonials()
    update_case_studies()
    print("Content update complete!")