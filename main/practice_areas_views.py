"""
Views for comprehensive practice areas
"""
from django.views.generic import TemplateView
from django.http import Http404
from .practice_areas_data import get_practice_area, get_all_practice_areas, PRACTICE_AREA_CATEGORIES

class PracticeAreaDetailView(TemplateView):
    """Detail view for individual practice areas with comprehensive service breakdown"""
    template_name = "main/practice_areas/practice_area_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = kwargs.get("slug")
        
        # Get practice area data
        practice_area = get_practice_area(slug)
        if not practice_area:
            raise Http404("Practice area not found")
        
        context["practice_area"] = practice_area
        
        # Find related practice areas
        related_areas = []
        for category, areas in PRACTICE_AREA_CATEGORIES.items():
            if slug in areas:
                for area_slug in areas:
                    if area_slug != slug:
                        area_data = get_practice_area(area_slug)
                        if area_data:
                            related_areas.append({
                                "slug": area_slug,
                                "name": area_data["name"],
                                "description": area_data["description"]
                            })
                break
        
        # Limit to 3 related areas
        context["related_areas"] = related_areas[:3]
        
        return context

class PracticeAreasIndexView(TemplateView):
    """Index view showing all practice areas organized by category"""
    template_name = "main/practice_areas/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Organize practice areas by category
        context["personal_injury_areas"] = []
        context["employment_areas"] = []
        context["business_areas"] = []
        
        for slug in PRACTICE_AREA_CATEGORIES["personal_injury_related"]:
            area = get_practice_area(slug)
            if area:
                context["personal_injury_areas"].append({
                    "slug": slug,
                    "name": area["name"],
                    "description": area["description"]
                })
        
        for slug in PRACTICE_AREA_CATEGORIES["employment_related"]:
            area = get_practice_area(slug)
            if area:
                context["employment_areas"].append({
                    "slug": slug,
                    "name": area["name"],
                    "description": area["description"]
                })
        
        for slug in PRACTICE_AREA_CATEGORIES["business_related"]:
            area = get_practice_area(slug)
            if area:
                context["business_areas"].append({
                    "slug": slug,
                    "name": area["name"],
                    "description": area["description"]
                })
        
        return context

# Individual practice area views for specific customization if needed
class PersonalInjuryView(TemplateView):
    template_name = "main/practice_areas/personal_injury.html"

class WrongfulDeathView(TemplateView):
    template_name = "main/practice_areas/wrongful_death.html"

class MedicalMalpracticeView(TemplateView):
    template_name = "main/practice_areas/medical_malpractice.html"

class EmploymentLitigationView(TemplateView):
    template_name = "main/practice_areas/employment_litigation.html"

class BusinessInterruptionView(TemplateView):
    template_name = "main/practice_areas/business_interruption.html"

class CommercialDisputesView(TemplateView):
    template_name = "main/practice_areas/commercial_disputes.html"

class DivorceValuationView(TemplateView):
    template_name = "main/practice_areas/divorce_valuation.html"