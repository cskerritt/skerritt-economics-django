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
        context['state_slug'] = state_name.lower().replace(' ', '-') if state_name else ''
        context['service_type'] = self.service_type
        context['city_slug'] = city_slug
        
        # Add city data for templates that expect it
        context['city'] = {
            'name': city_name,
            'state': state_name,
            'state_name': state_name,
            'state_abbr': state_abbr,
            'county': f'{city_name} County',  # Default county name
            'slug': city_slug
        }
        
        # Add structured data for SEO
        context['structured_data'] = {
            'city_name': city_name,
            'state_name': state_name,
            'service_name': 'Expert Services',  # Default, will be overridden by service-specific
            'latitude': 40.7128,  # Default coordinates
            'longitude': -74.0060
        }
        
        # Add standardized service-specific content
        if self.service_type == 'business_valuation':
            context['service_name'] = 'Business Valuation'
            context['service_slug'] = 'business-valuation'
            context['service_title'] = 'Business Valuation Expert'
            context['service_description'] = 'Fair market value analysis, business appraisals, and shareholder dispute valuations'
            context['meta_title'] = f'Business Valuation Expert in {city_name}, {state_abbr} | Skerritt Economics'
            context['meta_description'] = f'Expert business valuation services in {city_name}, {state_name}. Professional business appraisal and valuation analysis. Call (203) 605-2814 for consultation.'
            context['structured_data']['service_name'] = 'Business Valuation Services'
        elif self.service_type == 'forensic_economics':
            context['service_name'] = 'Forensic Economics'
            context['service_slug'] = 'forensic-economics'
            context['service_title'] = 'Forensic Economist'
            context['service_description'] = 'Economic damage analysis, lost earnings calculations, and expert witness testimony'
            context['meta_title'] = f'Forensic Economist in {city_name}, {state_abbr} | Economic Expert Witness'
            context['meta_description'] = f'Expert forensic economist in {city_name}, {state_name}. Economic damage calculations and expert witness testimony. Call (203) 605-2814 for consultation.'
            context['structured_data']['service_name'] = 'Forensic Economics Services'
        elif self.service_type == 'life_care_planning':
            context['service_name'] = 'Life Care Planning'
            context['service_slug'] = 'life-care-planning'
            context['service_title'] = 'Life Care Planner'
            context['service_description'] = 'Future medical cost projections, catastrophic injury planning, and assistive technology needs'
            context['meta_title'] = f'Life Care Planning Expert in {city_name}, {state_abbr} | Skerritt Economics'
            context['meta_description'] = f'Certified life care planning services in {city_name}, {state_name}. Future medical cost analysis and catastrophic injury planning. Call (203) 605-2814.'
            context['structured_data']['service_name'] = 'Life Care Planning Services'
        elif self.service_type == 'vocational_expert':
            context['service_name'] = 'Vocational Expert'
            context['service_slug'] = 'vocational-expert'
            context['service_title'] = 'Vocational Expert'
            context['service_description'] = 'Employability assessments, earning capacity evaluations, and vocational rehabilitation planning'
            context['meta_title'] = f'Vocational Expert in {city_name}, {state_abbr} | Employability Assessment'
            context['meta_description'] = f'Certified vocational expert services in {city_name}, {state_name}. Employability and earning capacity assessments. Call (203) 605-2814 for consultation.'
            context['structured_data']['service_name'] = 'Vocational Expert Services'
        elif self.service_type == 'business_consulting':
            context['service_name'] = 'Business Consulting'
            context['service_slug'] = 'business-consulting'
            context['service_title'] = 'Business Consultant'
            context['service_description'] = 'Strategic planning, operations improvement, and business transformation services'
            context['meta_title'] = f'Business Consulting Services in {city_name}, {state_abbr} | Expert Advisory'
            context['meta_description'] = f'Professional business consulting services in {city_name}, {state_name}. Strategic planning and operations improvement. Call (203) 605-2814.'
            context['structured_data']['service_name'] = 'Business Consulting Services'
        
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