"""
Industry-specific pages for business consulting services
"""

from django.urls import path
from .industry_views import IndustryConsultingView

# Industries for business consulting
INDUSTRIES = [
    {
        'slug': 'professional-services-consulting',
        'name': 'Professional Services',
        'description': 'Consulting for law firms, accounting firms, and professional service providers'
    },
    {
        'slug': 'technology-consulting',
        'name': 'Technology',
        'description': 'Business consulting for technology companies and startups'
    },
    {
        'slug': 'healthcare-consulting',
        'name': 'Healthcare',
        'description': 'Economic analysis and consulting for healthcare organizations'
    },
    {
        'slug': 'manufacturing-consulting',
        'name': 'Manufacturing',
        'description': 'Business valuation and consulting for manufacturing companies'
    },
    {
        'slug': 'retail-consulting',
        'name': 'Retail',
        'description': 'Economic consulting for retail and e-commerce businesses'
    },
    {
        'slug': 'financial-services-consulting',
        'name': 'Financial Services',
        'description': 'Consulting for banks, insurance companies, and financial institutions'
    },
    {
        'slug': 'real-estate-consulting',
        'name': 'Real Estate',
        'description': 'Economic analysis for real estate development and investment'
    },
    {
        'slug': 'hospitality-consulting',
        'name': 'Hospitality',
        'description': 'Business consulting for hotels, restaurants, and tourism'
    },
    {
        'slug': 'education-consulting',
        'name': 'Education',
        'description': 'Economic consulting for educational institutions'
    },
    {
        'slug': 'nonprofit-consulting',
        'name': 'Nonprofit',
        'description': 'Business consulting for nonprofit organizations'
    },
    {
        'slug': 'energy-consulting',
        'name': 'Energy',
        'description': 'Economic analysis for energy and utility companies'
    },
    {
        'slug': 'transportation-consulting',
        'name': 'Transportation',
        'description': 'Business consulting for transportation and logistics companies'
    },
    {
        'slug': 'construction-consulting',
        'name': 'Construction',
        'description': 'Economic consulting for construction and engineering firms'
    },
    {
        'slug': 'agriculture-consulting',
        'name': 'Agriculture',
        'description': 'Business valuation and consulting for agricultural businesses'
    },
    {
        'slug': 'media-consulting',
        'name': 'Media & Entertainment',
        'description': 'Economic consulting for media and entertainment companies'
    },
    {
        'slug': 'telecommunications-consulting',
        'name': 'Telecommunications',
        'description': 'Business consulting for telecom and communications companies'
    },
    {
        'slug': 'pharmaceutical-consulting',
        'name': 'Pharmaceutical',
        'description': 'Economic analysis for pharmaceutical and biotech companies'
    },
    {
        'slug': 'automotive-consulting',
        'name': 'Automotive',
        'description': 'Business consulting for automotive industry companies'
    },
    {
        'slug': 'insurance-consulting',
        'name': 'Insurance',
        'description': 'Economic consulting for insurance companies and agencies'
    },
    {
        'slug': 'government-consulting',
        'name': 'Government',
        'description': 'Economic analysis and consulting for government agencies'
    }
]

industry_urlpatterns = []

# Generate URLs for each industry
for industry in INDUSTRIES:
    industry_urlpatterns.append(
        path(
            f'services/business-consulting/industries/{industry["slug"]}/',
            IndustryConsultingView.as_view(),
            name=f'industry_{industry["slug"].replace("-", "_")}',
            kwargs={
                'industry_slug': industry['slug'],
                'industry_name': industry['name'],
                'industry_description': industry['description']
            }
        )
    )