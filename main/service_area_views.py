"""
Views for service area pages with city-state URL format
"""

from django.views.generic import TemplateView

class ServiceAreaBaseView(TemplateView):
    """Base view for service area pages"""
    template_name = 'main/service_areas/service_area.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = kwargs.get('city', '').replace('-', ' ').title()
        context['state'] = kwargs.get('state', '').upper()
        context['city_name'] = kwargs.get('city_name', context['city'])
        context['state_name'] = kwargs.get('state_name', context['state'])
        context['service_type'] = self.service_type
        context['service_name'] = self.service_name
        context['page_title'] = f'{self.service_name} in {context["city_name"]}, {context["state_name"]}'
        context['meta_description'] = f'Professional {self.service_name.lower()} services in {context["city_name"]}, {context["state_name"]}. Expert testimony and analysis for legal cases.'
        return context

class ServiceAreaVocationalExpertView(ServiceAreaBaseView):
    """View for vocational expert service area pages"""
    service_type = 'vocational-expert'
    service_name = 'Vocational Expert'

class ServiceAreaForensicEconomistView(ServiceAreaBaseView):
    """View for forensic economist service area pages"""
    service_type = 'forensic-economist'
    service_name = 'Forensic Economist'

class ServiceAreaLifeCarePlannerView(ServiceAreaBaseView):
    """View for life care planner service area pages"""
    service_type = 'life-care-planner'
    service_name = 'Life Care Planner'

class ServiceAreaBusinessValuationView(ServiceAreaBaseView):
    """View for business valuation service area pages"""
    service_type = 'business-valuation'
    service_name = 'Business Valuation'