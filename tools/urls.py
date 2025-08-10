from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.ToolsIndexView.as_view(), name='index'),
    path('life-expectancy/', views.LifeExpectancyView.as_view(), name='life_expectancy'),
    path('present-value/', views.PresentValueView.as_view(), name='present_value'),
    path('wage-growth/', views.WageGrowthView.as_view(), name='wage_growth'),
    path('household-services/', views.HouseholdServicesView.as_view(), name='household_services'),
    path('business-valuation/', views.BusinessValuationToolView.as_view(), name='business_valuation'),
    path('medical-costs/', views.MedicalCostsView.as_view(), name='medical_costs'),
]