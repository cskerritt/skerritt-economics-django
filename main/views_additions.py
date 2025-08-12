"""
Additional views for SEO pages and location handlers
"""
from django.views.generic import TemplateView
from django.http import Http404
import json
import os
from .us_cities_data import US_STATES, PRACTICE_AREAS

# Index Pages
class LocationsIndexView(TemplateView):
    template_name = 'main/locations/all_locations.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .city_data import CITY_DATA
        
        # Organize states by region for better display
        regions = {
            'Northeast': ['connecticut', 'maine', 'massachusetts', 'new-hampshire', 'new-jersey', 
                         'new-york', 'pennsylvania', 'rhode-island', 'vermont'],
            'Southeast': ['alabama', 'arkansas', 'delaware', 'florida', 'georgia', 'kentucky', 
                         'louisiana', 'maryland', 'mississippi', 'north-carolina', 'south-carolina', 
                         'tennessee', 'virginia', 'west-virginia'],
            'Midwest': ['illinois', 'indiana', 'iowa', 'kansas', 'michigan', 'minnesota', 
                       'missouri', 'nebraska', 'north-dakota', 'ohio', 'south-dakota', 'wisconsin'],
            'Southwest': ['arizona', 'new-mexico', 'oklahoma', 'texas'],
            'West': ['alaska', 'california', 'colorado', 'hawaii', 'idaho', 'montana', 
                    'nevada', 'oregon', 'utah', 'washington', 'wyoming']
        }
        
        # Add city data organized by region
        context['regions'] = {}
        for region_name, state_slugs in regions.items():
            context['regions'][region_name] = []
            for state_slug in state_slugs:
                if state_slug in CITY_DATA:
                    state_data = CITY_DATA[state_slug]
                    context['regions'][region_name].append({
                        'slug': state_slug,
                        'name': state_data['state_name'],
                        'abbr': state_data['state_abbr'],
                        'cities': state_data['cities']
                    })
        
        context['total_cities'] = sum(len(state['cities']) for state in CITY_DATA.values())
        context['total_pages'] = context['total_cities'] * 5  # 5 services per city (including business consulting)
        
        return context

class ServicesIndexView(TemplateView):
    template_name = 'main/services/index.html'

class PracticeAreasIndexView(TemplateView):
    template_name = 'main/practice_areas/index.html'

class ResourcesView(TemplateView):
    template_name = 'main/resources.html'

# Service landing pages (duplicates for URL structure)
class VocationalExpertServiceView(TemplateView):
    template_name = 'main/services/vocational_expert.html'

class LifeCarePlanningServiceView(TemplateView):
    template_name = 'main/services/life_care_planning.html'

# Regional Pages
class MassachusettsForensicEconomistView(TemplateView):
    template_name = 'main/locations/massachusetts_forensic_economist.html'

class RhodeIslandForensicEconomistView(TemplateView):
    template_name = 'main/locations/rhode_island_forensic_economist.html'

class NewEnglandEconomicExpertView(TemplateView):
    template_name = 'main/locations/new_england_economic_expert.html'

# City Page Base View
class BaseCityPageView(TemplateView):
    """Base view for all city-specific pages"""
    service_type = None
    
    def get_template_names(self):
        # Try specific template first, fall back to generic
        templates = []
        if self.service_type:
            templates.append(f'main/locations/city_{self.service_type}.html')
        templates.append('main/locations/city_generic.html')
        return templates
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_slug = kwargs.get('city_slug', '')
        
        # Parse city and state from slug
        parts = city_slug.replace('.html', '').split('-')
        
        # Extract state abbreviation (last part should be state)
        if len(parts) >= 2:
            state_abbr = parts[-1].upper()
            city_parts = parts[:-1]
            city_name = ' '.join(city_parts).title()
            
            # Get full state name
            if state_abbr in US_STATES:
                state_data = US_STATES[state_abbr]
                state_name = state_data['name']
                # Verify city is in state
                cities_lower = [c.lower() for c in state_data['cities']]
                if city_name.lower() not in cities_lower:
                    # Try to find the correct city name
                    for city in state_data['cities']:
                        if city.lower().replace(' ', '-').replace('.', '').replace("'", '') == '-'.join(city_parts):
                            city_name = city
                            break
            else:
                state_name = state_abbr
        else:
            state_abbr = ''
            state_name = ''
            city_name = city_slug.replace('-', ' ').title()
        
        context['city_name'] = city_name
        context['state'] = state_abbr
        context['state_name'] = state_name
        context['service_type'] = self.service_type
        context['city_slug'] = city_slug
        
        # Add service-specific content
        if self.service_type == 'business_valuation':
            context['service_title'] = 'Business Valuation Analyst'
            context['service_description'] = 'Expert business valuation services'
        elif self.service_type == 'forensic_economics':
            context['service_title'] = 'Forensic Economist'
            context['service_description'] = 'Economic damage analysis and expert testimony'
        elif self.service_type == 'life_care_planning':
            context['service_title'] = 'Life Care Planner'
            context['service_description'] = 'Comprehensive life care planning services'
        elif self.service_type == 'vocational_expert':
            context['service_title'] = 'Vocational Expert'
            context['service_description'] = 'Vocational assessment and earning capacity evaluation'
        elif self.service_type == 'business_consulting':
            context['service_title'] = 'Business Consultant'
            context['service_description'] = 'Strategic business consulting and advisory services'
        
        return context

# City Page Views
class CityPageView(BaseCityPageView):
    """Generic city page handler"""
    pass

class CityBusinessValuationView(BaseCityPageView):
    service_type = 'business_valuation'

class CityForensicEconomicsView(BaseCityPageView):
    service_type = 'forensic_economics'

class CityLifeCarePlanningView(BaseCityPageView):
    service_type = 'life_care_planning'

class CityVocationalExpertView(BaseCityPageView):
    service_type = 'vocational_expert'

class CityBusinessConsultingView(BaseCityPageView):
    service_type = 'business_consulting'