from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .practice_areas_views import PracticeAreaDetailView
from .city_urls import city_urlpatterns
from .health import health_check

urlpatterns = [
    # Health check endpoint
    path('health/', health_check, name='health_check'),
    
    # SEO files
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    
    # Redirects for old URLs to maintain SEO
    path('locations/', views.LocationsIndexView.as_view(), name='locations_index'),
    path('services/', views.ServicesIndexView.as_view(), name='services_index'),
    path('practice-areas/', views.PracticeAreasIndexView.as_view(), name='practice_areas_index'),
    path('resources/', views.ResourcesView.as_view(), name='resources'),
    path('vocational-expert/', views.VocationalExpertServiceView.as_view(), name='vocational_expert'),
    path('life-care-planning/', views.LifeCarePlanningServiceView.as_view(), name='life_care_planning'),
    

    # Home page
    path('', views.HomeView.as_view(), name='home'),
    
    # Service pages
    path('services/forensic-economics/', views.ForensicEconomicsView.as_view(), name='service_forensic'),
    path('services/business-valuation/', views.BusinessValuationView.as_view(), name='service_valuation'),
    path('services/vocational-expert/', views.VocationalExpertView.as_view(), name='service_vocational'),
    path('services/life-care-planning/', views.LifeCarePlanningView.as_view(), name='service_lifecare'),
    path('services/business-consulting/', views.BusinessConsultingView.as_view(), name='service_consulting'),
    
    # Practice area pages - using dynamic view for all areas
    path('practice-areas/<slug:slug>/', PracticeAreaDetailView.as_view(), name='practice_area_detail'),
    # Specific practice area pages with custom templates
    path('practice-areas/personal-injury/', views.PersonalInjuryView.as_view(), name='practice_personal_injury'),
    path('practice-areas/medical-malpractice/', views.MedicalMalpracticeView.as_view(), name='practice_medical'),
    path('practice-areas/employment-litigation/', views.EmploymentLitigationView.as_view(), name='practice_employment'),
    path('practice-areas/commercial-disputes/', views.CommercialDisputesView.as_view(), name='practice_commercial'),
    path('practice-areas/vocational-expert/', views.VocationalExpertPracticeView.as_view(), name='practice_vocational'),
    path('practice-areas/life-care-planning/', views.LifeCarePlanningPracticeView.as_view(), name='practice_lifecare'),
    path('practice-areas/business-consulting/', views.BusinessConsultingView.as_view(), name='practice_consulting'),
    path('practice-areas/business-valuation/', views.BusinessValuationPracticeView.as_view(), name='practice_valuation'),
    
    # Other pages
    path('about/', views.AboutView.as_view(), name='about'),
    path('case-studies/', views.CaseStudiesView.as_view(), name='case_studies'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/thank-you/', views.ContactThankYouView.as_view(), name='contact_thank_you'),
    path('sitemap/', views.SitemapView.as_view(), name='sitemap_html'),
    
    # Location pages - state level
    path('locations/<slug:state>/', views.LocationView.as_view(), name='location'),
    path('locations/massachusetts-forensic-economist/', views.MassachusettsForensicEconomistView.as_view(), name='ma_forensic_economist'),
    path('locations/rhode-island-forensic-economist/', views.RhodeIslandForensicEconomistView.as_view(), name='ri_forensic_economist'),
    path('locations/new-england-economic-expert/', views.NewEnglandEconomicExpertView.as_view(), name='ne_economic_expert'),
    
    # City pages for each service type (legacy URLs - maintain for SEO)
    path('locations/cities/<slug:city_slug>.html', views.CityPageView.as_view(), name='city_page'),
    path('locations/business-valuation/<slug:city_slug>.html', views.CityBusinessValuationView.as_view(), name='city_business_valuation'),
    path('locations/forensic-economics/<slug:city_slug>.html', views.CityForensicEconomicsView.as_view(), name='city_forensic_economics'),
    path('locations/life-care-planning/<slug:city_slug>.html', views.CityLifeCarePlanningView.as_view(), name='city_life_care'),
    path('locations/vocational-expert/<slug:city_slug>.html', views.CityVocationalExpertView.as_view(), name='city_vocational'),
]

# Add city-specific URLs
urlpatterns += city_urlpatterns

# Import and add SEO city URL patterns
from .city_seo_urls import city_seo_urlpatterns
urlpatterns += city_seo_urlpatterns

# Import and add improved URL patterns
from .improved_urls import all_improved_urls
urlpatterns += all_improved_urls