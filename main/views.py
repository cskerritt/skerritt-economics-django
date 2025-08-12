from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm, ReferralForm
from .models import Testimonial, FAQ, Referral
from blog.models import Post, CaseStudy

# Import additional views
from .views_additions import *

class HomeView(TemplateView):
    template_name = 'main/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(featured=True)[:3]
        context['recent_posts'] = Post.objects.filter(status='published', featured=True)[:3]
        context['case_studies'] = CaseStudy.objects.filter(featured=True)[:3]
        context['faqs'] = FAQ.objects.filter(active=True)[:6]
        return context

# Service Pages
class ForensicEconomicsView(TemplateView):
    template_name = 'main/services/forensic_economics.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_name'] = 'Forensic Economics'
        context['service_slug'] = 'forensic-economics'
        context['service_title'] = 'Forensic Economist'
        context['service_description'] = 'Economic damage analysis, lost earnings calculations, and expert witness testimony'
        return context

class BusinessValuationView(TemplateView):
    template_name = 'main/services/business_valuation.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_name'] = 'Business Valuation'
        context['service_slug'] = 'business-valuation'
        context['service_title'] = 'Business Valuation Expert'
        context['service_description'] = 'Fair market value analysis, business appraisals, and shareholder dispute valuations'
        return context

class VocationalExpertView(TemplateView):
    template_name = 'main/services/vocational_expert.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_name'] = 'Vocational Expert'
        context['service_slug'] = 'vocational-expert'
        context['service_title'] = 'Vocational Expert'
        context['service_description'] = 'Employability assessments, earning capacity evaluations, and vocational rehabilitation planning'
        return context

class LifeCarePlanningView(TemplateView):
    template_name = 'main/services/life_care_planning.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_name'] = 'Life Care Planning'
        context['service_slug'] = 'life-care-planning'
        context['service_title'] = 'Life Care Planner'
        context['service_description'] = 'Future medical cost projections, catastrophic injury planning, and assistive technology needs'
        return context

class BusinessConsultingView(TemplateView):
    template_name = 'main/services/business_consulting.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_name'] = 'Business Consulting'
        context['service_slug'] = 'business-consulting'
        context['service_title'] = 'Business Consultant'
        context['service_description'] = 'Strategic planning, operations improvement, and business transformation services'
        return context

# Practice Area Pages
class PersonalInjuryView(TemplateView):
    template_name = 'main/practice_areas/personal_injury.html'

class MedicalMalpracticeView(TemplateView):
    template_name = 'main/practice_areas/medical_malpractice.html'

class EmploymentLitigationView(TemplateView):
    template_name = 'main/practice_areas/employment_litigation.html'

class CommercialDisputesView(TemplateView):
    template_name = 'main/practice_areas/commercial_disputes.html'

class VocationalExpertPracticeView(TemplateView):
    template_name = 'main/practice_areas/vocational_expert.html'

class LifeCarePlanningPracticeView(TemplateView):
    template_name = 'main/practice_areas/life_care_planning.html'

class BusinessConsultingView(TemplateView):
    template_name = 'main/practice_areas/business_consulting.html'

class BusinessValuationPracticeView(TemplateView):
    template_name = 'main/practice_areas/business_valuation.html'

# Other Pages
class AboutView(TemplateView):
    template_name = 'main/about.html'

class CaseStudiesView(TemplateView):
    template_name = 'main/case_studies.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['case_studies'] = CaseStudy.objects.filter(published=True)
        return context

class ContactView(TemplateView):
    """Contact form using Formspree for email handling"""
    template_name = 'main/contact_formspree.html'

class ContactThankYouView(TemplateView):
    template_name = 'main/contact_thank_you.html'


class ReferralView(FormView):
    template_name = 'main/referral.html'
    form_class = ReferralForm
    success_url = reverse_lazy('referral_thank_you')
    
    def form_valid(self, form):
        # Save the referral
        referral = form.save()
        
        # Send email notification
        try:
            subject = f'New Expert Referral: {referral.referrer_name} - {referral.get_case_type_display()}'
            
            message = f"""
New expert referral received:

REFERRER INFORMATION:
Name: {referral.referrer_name}
Email: {referral.referrer_email}
Phone: {referral.referrer_phone}
Firm: {referral.referrer_firm}
Title: {referral.referrer_title}
Location: {referral.referrer_location}

REFERRAL TYPE: {referral.get_referral_type_display()}

CASE INFORMATION:
Type: {referral.get_case_type_display()}
Caption: {referral.case_caption}
Court: {referral.court_jurisdiction}
Case #: {referral.case_number}

EXPERT SERVICES NEEDED:
{referral.expert_needed_for}

Opposing Expert: {referral.opposing_expert}

TIMELINE:
Urgency: {referral.get_urgency_display()}
Trial Date: {referral.trial_date}
Discovery Deadline: {referral.discovery_deadline}

DAMAGES ESTIMATE: {referral.damages_estimate}

CASE DESCRIPTION:
{referral.case_description}

ADDITIONAL REQUIREMENTS:
{referral.specific_requirements}

CONTACT PREFERENCE:
Method: {referral.get_preferred_contact_method_display()}
Best Time: {referral.best_time_to_contact}

---
Submitted: {referral.created_date.strftime('%Y-%m-%d %H:%M')}
"""
            
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['chris@skerritteconomics.com'],
                fail_silently=True,
            )
        except Exception as e:
            # Log error but don't fail the form submission
            print(f"Error sending referral email: {e}")
        
        messages.success(self.request, 'Thank you for your referral. We will review it and contact you shortly.')
        return super().form_valid(form)


class ReferralThankYouView(TemplateView):
    template_name = 'main/referral_thank_you.html'

class SitemapView(TemplateView):
    template_name = 'main/sitemap.html'

class LocationView(TemplateView):
    template_name = 'main/location.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state_slug = kwargs.get('state', '')
        
        # Import US_STATES data
        from .us_cities_data import US_STATES
        
        # Convert slug to state abbreviation
        state_lookup = {
            'alabama': 'AL', 'alaska': 'AK', 'arizona': 'AZ', 'arkansas': 'AR',
            'california': 'CA', 'colorado': 'CO', 'connecticut': 'CT', 'delaware': 'DE',
            'florida': 'FL', 'georgia': 'GA', 'hawaii': 'HI', 'idaho': 'ID',
            'illinois': 'IL', 'indiana': 'IN', 'iowa': 'IA', 'kansas': 'KS',
            'kentucky': 'KY', 'louisiana': 'LA', 'maine': 'ME', 'maryland': 'MD',
            'massachusetts': 'MA', 'michigan': 'MI', 'minnesota': 'MN', 'mississippi': 'MS',
            'missouri': 'MO', 'montana': 'MT', 'nebraska': 'NE', 'nevada': 'NV',
            'new-hampshire': 'NH', 'new-jersey': 'NJ', 'new-mexico': 'NM', 'new-york': 'NY',
            'north-carolina': 'NC', 'north-dakota': 'ND', 'ohio': 'OH', 'oklahoma': 'OK',
            'oregon': 'OR', 'pennsylvania': 'PA', 'rhode-island': 'RI', 'south-carolina': 'SC',
            'south-dakota': 'SD', 'tennessee': 'TN', 'texas': 'TX', 'utah': 'UT',
            'vermont': 'VT', 'virginia': 'VA', 'washington': 'WA', 'west-virginia': 'WV',
            'wisconsin': 'WI', 'wyoming': 'WY'
        }
        
        state_abbr = state_lookup.get(state_slug, '')
        if state_abbr and state_abbr in US_STATES:
            state_data = US_STATES[state_abbr]
            context['state'] = state_data['name']
            context['cities'] = state_data['cities'][:15]  # Top 15 cities
            context['state_info'] = {
                'name': state_data['name'],
                'cities': state_data['cities'][:15],
                'description': f'Expert forensic economics and business valuation services throughout {state_data["name"]}.'
            }
        else:
            context['state'] = state_slug.replace('-', ' ').title()
            context['cities'] = []
            context['state_info'] = {
                'name': state_slug.replace('-', ' ').title(),
                'cities': [],
                'description': 'Expert forensic economics and business valuation services.'
            }
        
        return context
