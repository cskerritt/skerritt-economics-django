"""
Views for industry-specific business consulting pages
"""

from django.views.generic import TemplateView

class IndustryConsultingView(TemplateView):
    """View for industry-specific business consulting pages"""
    template_name = "main/industries/industry_consulting.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["industry_slug"] = kwargs.get("industry_slug", "")
        context["industry_name"] = kwargs.get("industry_name", "")
        context["industry_description"] = kwargs.get("industry_description", "")
        context["page_title"] = f"{context["industry_name"]} Business Consulting Services"
        context["meta_description"] = context["industry_description"]
        
        # Add related services
        context["related_services"] = [
            {
                "name": "Business Valuation",
                "url": "/services/business-valuation/",
                "description": "Expert business valuation services"
            },
            {
                "name": "Forensic Economics",
                "url": "/services/forensic-economics/",
                "description": "Economic damage analysis and expert testimony"
            },
            {
                "name": "Life Care Planning",
                "url": "/services/life-care-planning/",
                "description": "Comprehensive life care cost projections"
            }
        ]
        
        # Industry-specific case types
        context["case_types"] = self.get_industry_case_types(context["industry_slug"])
        
        return context
    
    def get_industry_case_types(self, industry_slug):
        """Get relevant case types for each industry"""
        case_types_map = {
            "professional-services-consulting": [
                "Partnership disputes",
                "Professional liability",
                "Business interruption",
                "Unfair competition"
            ],
            "technology-consulting": [
                "Intellectual property disputes",
                "Trade secret misappropriation",
                "Startup valuations",
                "Merger & acquisition analysis"
            ],
            "healthcare-consulting": [
                "Medical practice valuations",
                "Healthcare fraud analysis",
                "Hospital merger economics",
                "Medical malpractice damages"
            ],
            "manufacturing-consulting": [
                "Product liability economics",
                "Supply chain disruption",
                "Industrial accident damages",
                "Equipment valuation"
            ],
            "retail-consulting": [
                "Lost profits analysis",
                "Franchise disputes",
                "Commercial lease disputes",
                "Inventory valuation"
            ],
            "financial-services-consulting": [
                "Securities litigation",
                "Banking disputes",
                "Investment loss analysis",
                "Regulatory compliance economics"
            ],
            "real-estate-consulting": [
                "Property valuation disputes",
                "Construction defect damages",
                "Eminent domain valuation",
                "Real estate fraud analysis"
            ],
            "hospitality-consulting": [
                "Hotel valuation",
                "Restaurant business interruption",
                "Tourism impact analysis",
                "Franchise agreement disputes"
            ],
            "education-consulting": [
                "School funding analysis",
                "Educational institution valuation",
                "Student loan economics",
                "Academic salary disputes"
            ],
            "nonprofit-consulting": [
                "Nonprofit valuation",
                "Charitable trust disputes",
                "Grant funding analysis",
                "Donor restriction compliance"
            ],
            "energy-consulting": [
                "Energy project valuation",
                "Environmental damage economics",
                "Utility rate disputes",
                "Oil & gas royalty analysis"
            ],
            "transportation-consulting": [
                "Transportation accident damages",
                "Logistics business valuation",
                "Freight claim disputes",
                "Fleet valuation"
            ],
            "construction-consulting": [
                "Construction delay damages",
                "Contractor dispute analysis",
                "Project cost overrun analysis",
                "Construction defect economics"
            ],
            "agriculture-consulting": [
                "Farm valuation",
                "Crop damage analysis",
                "Agricultural subsidy disputes",
                "Livestock valuation"
            ],
            "media-consulting": [
                "Media company valuation",
                "Copyright infringement damages",
                "Entertainment contract disputes",
                "Advertising revenue analysis"
            ],
            "telecommunications-consulting": [
                "Telecom infrastructure valuation",
                "Service interruption damages",
                "Spectrum rights valuation",
                "Network expansion economics"
            ],
            "pharmaceutical-consulting": [
                "Drug patent valuation",
                "Clinical trial economics",
                "Pharmaceutical liability",
                "FDA compliance costs"
            ],
            "automotive-consulting": [
                "Dealership valuation",
                "Auto defect economics",
                "Supply chain analysis",
                "Warranty claim economics"
            ],
            "insurance-consulting": [
                "Insurance agency valuation",
                "Bad faith claim analysis",
                "Premium dispute economics",
                "Reinsurance analysis"
            ],
            "government-consulting": [
                "Government contract disputes",
                "Public project economics",
                "Regulatory impact analysis",
                "Municipal finance analysis"
            ]
        }
        
        return case_types_map.get(industry_slug, [
            "Business valuation",
            "Economic damage analysis",
            "Lost profits calculation",
            "Expert testimony"
        ])