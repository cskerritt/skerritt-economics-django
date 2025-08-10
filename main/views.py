from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Testimonial, FAQ
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

class BusinessValuationView(TemplateView):
    template_name = 'main/services/business_valuation.html'

class VocationalExpertView(TemplateView):
    template_name = 'main/services/vocational_expert.html'

class LifeCarePlanningView(TemplateView):
    template_name = 'main/services/life_care_planning.html'

class BusinessConsultingView(TemplateView):
    template_name = 'main/services/business_consulting.html'

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

class ContactView(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_thank_you')
    
    def form_valid(self, form):
        # Save the inquiry
        inquiry = form.save()
        
        # Prepare email
        subject = f"New Case Consultation Request - {inquiry.get_case_type_display()}"
        message = f"""
        New consultation request received:
        
        Name: {inquiry.name}
        Email: {inquiry.email}
        Phone: {inquiry.phone}
        Organization: {inquiry.organization or 'Not provided'}
        
        Case Type: {inquiry.get_case_type_display()}
        Jurisdiction: {inquiry.get_jurisdiction_display()}
        Timeline: {inquiry.get_timeline_display()}
        
        Case Details:
        {inquiry.case_details}
        
        ---
        This inquiry was submitted on {inquiry.created_date.strftime('%B %d, %Y at %I:%M %p')}
        """
        
        # Send email
        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.ADMIN_EMAIL],
                reply_to=[inquiry.email]
            )
            email.send()
            messages.success(self.request, "Thank you for your inquiry. We'll respond within 24 hours.")
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.warning(self.request, "Your inquiry was received but there was an issue sending the notification. We'll still respond within 24 hours.")
        
        return super().form_valid(form)

class ContactThankYouView(TemplateView):
    template_name = 'main/contact_thank_you.html'

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
