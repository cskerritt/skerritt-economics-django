"""
URL configuration using function-based views.
"""

from django.urls import path, include
from django.views.generic import TemplateView

from . import views_functional as views
from .health import health_check
from .rss_feed import BlogRSSFeed

urlpatterns = [
    # Health check endpoint
    path("health/", health_check, name="health_check"),
    
    # SEO files
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
    
    # RSS Feed
    path("blog/rss/", BlogRSSFeed(), name="blog_rss_feed"),
    
    # Home page
    path("", views.home_view, name="home"),
    
    # Service pages
    path("services/", views.services_index_view, name="services_index"),
    path("services/forensic-economics/", views.forensic_economics_view, name="service_forensic"),
    path("services/business-valuation/", views.business_valuation_view, name="service_valuation"),
    path("services/vocational-expert/", views.vocational_expert_view, name="service_vocational"),
    path("services/life-care-planning/", views.life_care_planning_view, name="service_lifecare"),
    path("services/business-consulting/", views.business_consulting_view, name="service_consulting"),
    
    # Practice area pages
    path("practice-areas/", views.practice_areas_index_view, name="practice_areas_index"),
    path("practice-areas/personal-injury/", views.personal_injury_view, name="practice_personal_injury"),
    path("practice-areas/medical-malpractice/", views.medical_malpractice_view, name="practice_medical"),
    path("practice-areas/employment-litigation/", views.employment_litigation_view, name="practice_employment"),
    path("practice-areas/commercial-disputes/", views.commercial_disputes_view, name="practice_commercial"),
    
    # Other pages
    path("about/", views.about_view, name="about"),
    path("case-studies/", views.case_studies_view, name="case_studies"),
    path("resources/", views.resources_view, name="resources"),
    path("contact/", views.contact_view, name="contact"),
    path("contact/thank-you/", views.contact_thank_you_view, name="contact_thank_you"),
    path("referral/", views.referral_view, name="referral"),
    path("referral/thank-you/", views.referral_thank_you_view, name="referral_thank_you"),
    path("sitemap/", views.sitemap_view, name="sitemap_html"),
    
    # Location pages
    path("locations/", views.locations_index_view, name="locations_index"),
    path("location/<str:state>/", views.location_view, name="location"),
]