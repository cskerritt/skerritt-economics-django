# Add this to your views to ensure consistent context

def get_service_context(service_slug):
    """Get standardized context for service templates"""
    
    SERVICES = {
        "forensic-economics": {
            "service_name": "Forensic Economics",
            "service_slug": "forensic-economics",
            "service_title": "Forensic Economist",
            "service_description": "Economic damage analysis, lost earnings calculations, and expert witness testimony"
        },
        "business-valuation": {
            "service_name": "Business Valuation",
            "service_slug": "business-valuation",
            "service_title": "Business Valuation Expert",
            "service_description": "Fair market value analysis, business appraisals, and shareholder dispute valuations"
        },
        "business-consulting": {
            "service_name": "Business Consulting",
            "service_slug": "business-consulting",
            "service_title": "Business Consultant",
            "service_description": "Strategic planning, operations improvement, and business transformation services"
        },
        "vocational-expert": {
            "service_name": "Vocational Expert",
            "service_slug": "vocational-expert",
            "service_title": "Vocational Expert",
            "service_description": "Employability assessments, earning capacity evaluations, and vocational rehabilitation planning"
        },
        "life-care-planning": {
            "service_name": "Life Care Planning",
            "service_slug": "life-care-planning",
            "service_title": "Life Care Planner",
            "service_description": "Future medical cost projections, catastrophic injury planning, and assistive technology needs"
        }
    }
    
    return SERVICES.get(service_slug, {})

# Update your view classes to use this:
# context.update(get_service_context(self.service_slug))
