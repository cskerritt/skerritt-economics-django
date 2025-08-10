"""
Views for expanded practice areas
"""
from django.views.generic import TemplateView
from .us_cities_data import PRACTICE_AREAS

class PracticeAreaDetailView(TemplateView):
    """Dynamic view for all practice areas"""
    template_name = 'main/practice_areas/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get('slug', '')
        
        # Find the practice area
        practice_area = None
        for area in PRACTICE_AREAS:
            if area['slug'] == slug:
                practice_area = area
                break
        
        if not practice_area:
            # Default fallback
            practice_area = {
                'name': slug.replace('-', ' ').title(),
                'description': f'Expert forensic economic analysis for {slug.replace("-", " ")} cases'
            }
        
        context['practice_area'] = practice_area
        context['all_practice_areas'] = PRACTICE_AREAS
        
        return context

# Individual practice area views for specific customization if needed
class PersonalInjuryView(TemplateView):
    template_name = 'main/practice_areas/personal_injury.html'

class WrongfulDeathView(TemplateView):
    template_name = 'main/practice_areas/wrongful_death.html'

class MedicalMalpracticeView(TemplateView):
    template_name = 'main/practice_areas/medical_malpractice.html'

class EmploymentLitigationView(TemplateView):
    template_name = 'main/practice_areas/employment_litigation.html'

class BusinessInterruptionView(TemplateView):
    template_name = 'main/practice_areas/business_interruption.html'

class CommercialDisputesView(TemplateView):
    template_name = 'main/practice_areas/commercial_disputes.html'

class DivorceValuationView(TemplateView):
    template_name = 'main/practice_areas/divorce_valuation.html'