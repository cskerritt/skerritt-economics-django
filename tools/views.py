from django.shortcuts import render
from django.views.generic import TemplateView

class ToolsIndexView(TemplateView):
    template_name = "tools/index.html"

class LifeExpectancyView(TemplateView):
    template_name = "tools/life_expectancy.html"

class PresentValueView(TemplateView):
    template_name = "tools/present_value.html"

class WageGrowthView(TemplateView):
    template_name = "tools/wage_growth.html"

class HouseholdServicesView(TemplateView):
    template_name = "tools/household_services.html"

class BusinessValuationToolView(TemplateView):
    template_name = "tools/business_valuation.html"

class MedicalCostsView(TemplateView):
    template_name = "tools/medical_costs.html"
