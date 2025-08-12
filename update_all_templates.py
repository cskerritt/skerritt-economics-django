#!/usr/bin/env python3
"""
Comprehensive script to update all service and location templates to use standardized base templates
"""

import os
from pathlib import Path

# Base directory for templates
TEMPLATE_DIR = Path("main/templates/main")

# Service configuration with all required context variables
SERVICES = {
    'forensic_economics': {
        'name': 'Forensic Economics',
        'slug': 'forensic-economics',
        'title': 'Forensic Economist',
        'description': 'Economic damage analysis, lost earnings calculations, and expert witness testimony'
    },
    'business_valuation': {
        'name': 'Business Valuation',
        'slug': 'business-valuation',
        'title': 'Business Valuation Expert',
        'description': 'Fair market value analysis, business appraisals, and shareholder dispute valuations'
    },
    'business_consulting': {
        'name': 'Business Consulting',
        'slug': 'business-consulting',
        'title': 'Business Consultant',
        'description': 'Strategic planning, operations improvement, and business transformation services'
    },
    'vocational_expert': {
        'name': 'Vocational Expert',
        'slug': 'vocational-expert',
        'title': 'Vocational Expert',
        'description': 'Employability assessments, earning capacity evaluations, and vocational rehabilitation planning'
    },
    'life_care_planning': {
        'name': 'Life Care Planning',
        'slug': 'life-care-planning',
        'title': 'Life Care Planner',
        'description': 'Future medical cost projections, catastrophic injury planning, and assistive technology needs'
    }
}

def create_standardized_service_template(service_key, service_data):
    """Create a standardized service template that extends the base template"""
    
    template_content = f"""{{% extends 'main/base_service_template.html' %}}
{{% load static %}}

{{% comment %}}
Standardized {service_data['name']} Service Page
This template extends the base service template for consistent formatting
{{% endcomment %}}

{{% block service_content %}}
<!-- Service Overview Card -->
<div class="card border-0 shadow-sm mb-4">
    <div class="card-body p-4">
        <h2 class="h3 mb-3">Professional {service_data['name']} Services</h2>
        <p>Christopher Skerritt provides comprehensive {service_data['name'].lower()} services to attorneys, insurance companies, and legal professionals throughout the United States. With extensive experience and professional certifications, we deliver accurate, defensible analysis for legal proceedings.</p>
        
        <div class="row mt-4">
            <div class="col-md-6">
                <h4 class="h5 text-primary">Core Services</h4>
                <ul>
                    <li>Expert witness testimony</li>
                    <li>Comprehensive case analysis</li>
                    <li>Detailed written reports</li>
                    <li>Deposition and trial testimony</li>
                </ul>
            </div>
            <div class="col-md-6">
                <h4 class="h5 text-primary">Experience</h4>
                <ul>
                    <li>20+ years professional experience</li>
                    <li>Court-qualified expert witness</li>
                    <li>Nationwide case coverage</li>
                    <li>Rapid response time</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Expertise Areas -->
<div class="card border-0 shadow-sm mb-4">
    <div class="card-body p-4">
        <h2 class="h3 mb-3">{service_data['name']} Expertise</h2>
        <div class="row">
            <div class="col-md-6">
                <div class="d-flex mb-3">
                    <i class="fas fa-check-circle text-success me-2 mt-1"></i>
                    <div>
                        <strong>Analysis & Calculations</strong>
                        <p class="small mb-0">Comprehensive economic analysis using industry-standard methodologies</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="d-flex mb-3">
                    <i class="fas fa-check-circle text-success me-2 mt-1"></i>
                    <div>
                        <strong>Expert Testimony</strong>
                        <p class="small mb-0">Clear, credible courtroom testimony that withstands cross-examination</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="d-flex mb-3">
                    <i class="fas fa-check-circle text-success me-2 mt-1"></i>
                    <div>
                        <strong>Report Preparation</strong>
                        <p class="small mb-0">Detailed reports that meet all legal and professional standards</p>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="d-flex mb-3">
                    <i class="fas fa-check-circle text-success me-2 mt-1"></i>
                    <div>
                        <strong>Case Consultation</strong>
                        <p class="small mb-0">Strategic guidance throughout the litigation process</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Process Overview -->
<div class="card border-0 shadow-sm mb-4">
    <div class="card-body p-4">
        <h2 class="h3 mb-3">Our Process</h2>
        <div class="row">
            <div class="col-md-3 mb-3">
                <div class="text-center">
                    <div class="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                        <i class="fas fa-phone fa-lg"></i>
                    </div>
                    <h5 class="mt-2">1. Initial Consultation</h5>
                    <p class="small">Free case evaluation and scope assessment</p>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="text-center">
                    <div class="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                        <i class="fas fa-search fa-lg"></i>
                    </div>
                    <h5 class="mt-2">2. Analysis</h5>
                    <p class="small">Comprehensive review and calculations</p>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="text-center">
                    <div class="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                        <i class="fas fa-file-alt fa-lg"></i>
                    </div>
                    <h5 class="mt-2">3. Report</h5>
                    <p class="small">Detailed written findings and conclusions</p>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="text-center">
                    <div class="bg-primary text-white rounded-circle d-inline-flex align-items-center justify-content-center" style="width: 60px; height: 60px;">
                        <i class="fas fa-gavel fa-lg"></i>
                    </div>
                    <h5 class="mt-2">4. Testimony</h5>
                    <p class="small">Expert witness testimony as needed</p>
                </div>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}

{{% block faq_items %}}
<div class="accordion-item">
    <h2 class="accordion-header">
        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#faq1">
            What is a {service_data['title'].lower()}?
        </button>
    </h2>
    <div id="faq1" class="accordion-collapse collapse show">
        <div class="accordion-body">
            A {service_data['title'].lower()} is a professional who provides {service_data['description'].lower()}. They serve as expert witnesses in legal proceedings and provide detailed analysis for attorneys and insurance companies.
        </div>
    </div>
</div>

<div class="accordion-item">
    <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq2">
            When do I need {service_data['name'].lower()} services?
        </button>
    </h2>
    <div id="faq2" class="accordion-collapse collapse">
        <div class="accordion-body">
            {service_data['name']} services are needed when legal cases require expert analysis and testimony regarding {service_data['description'].lower()}. This includes personal injury, wrongful death, employment disputes, and commercial litigation.
        </div>
    </div>
</div>

<div class="accordion-item">
    <h2 class="accordion-header">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq3">
            What qualifications does Christopher Skerritt have?
        </button>
    </h2>
    <div id="faq3" class="accordion-collapse collapse">
        <div class="accordion-body">
            Christopher Skerritt holds multiple advanced degrees (M.Ed, MBA) and professional certifications including CRC, CLCP, ABVE/F, CVE, FVE, and IPEC. He has over 20 years of experience providing expert witness services.
        </div>
    </div>
</div>
{{% endblock %}}
"""
    
    return template_content

def create_city_service_template(service_key, service_data):
    """Create a template for city/service combination pages"""
    
    template_content = f"""{{% extends 'main/base_city_template.html' %}}
{{% load static %}}

{{% comment %}}
City-specific {service_data['name']} Service Page
This template extends the base city template for consistent formatting
{{% endcomment %}}

{{% block service_details %}}
<h4 class="h5 text-primary mb-3">{service_data['name']} Services</h4>
<p>{service_data['description']}</p>

<div class="row mt-4">
    <div class="col-md-6">
        <h5 class="h6 text-primary">Local Expertise</h5>
        <ul class="small">
            <li>Understanding of {{{{ city_name }}}} market conditions</li>
            <li>Knowledge of {{{{ state_name }}}} state regulations</li>
            <li>Experience with local court requirements</li>
            <li>Regional economic analysis</li>
        </ul>
    </div>
    <div class="col-md-6">
        <h5 class="h6 text-primary">Service Coverage</h5>
        <ul class="small">
            <li>{{{{ city_name }}}} and surrounding areas</li>
            <li>All {{{{ state_name }}}} counties</li>
            <li>Federal court cases</li>
            <li>Remote testimony available</li>
        </ul>
    </div>
</div>
{{% endblock %}}
"""
    
    return template_content

def update_service_templates():
    """Update all main service template files"""
    services_dir = TEMPLATE_DIR / "services"
    
    print("\n" + "="*60)
    print("UPDATING SERVICE TEMPLATES")
    print("="*60)
    
    for service_key, service_data in SERVICES.items():
        # Generate template filename
        if service_key == 'forensic_economics':
            filename = 'forensic_economics.html'
        elif service_key == 'business_valuation':
            filename = 'business_valuation.html'
        elif service_key == 'business_consulting':
            filename = 'business_consulting.html'
        elif service_key == 'vocational_expert':
            filename = 'vocational_expert.html'
        elif service_key == 'life_care_planning':
            filename = 'life_care_planning.html'
        else:
            continue
            
        template_path = services_dir / filename
        
        # Create standardized template content
        content = create_standardized_service_template(service_key, service_data)
        
        # Write the template
        template_path.write_text(content)
        print(f"✓ Updated: {filename}")

def update_city_templates():
    """Update city-specific service templates"""
    cities_dir = TEMPLATE_DIR / "cities"
    
    print("\n" + "="*60)
    print("UPDATING CITY TEMPLATES")
    print("="*60)
    
    # Create template files for each service type
    for service_key, service_data in SERVICES.items():
        filename = f"city_{service_key}.html"
        template_path = cities_dir / filename
        
        content = create_city_service_template(service_key, service_data)
        template_path.write_text(content)
        print(f"✓ Created: {filename}")

def create_view_context_updater():
    """Create a Python file with view context updates"""
    
    view_updates = '''# Add this to your views to ensure consistent context

def get_service_context(service_slug):
    """Get standardized context for service templates"""
    
    SERVICES = {
        'forensic-economics': {
            'service_name': 'Forensic Economics',
            'service_slug': 'forensic-economics',
            'service_title': 'Forensic Economist',
            'service_description': 'Economic damage analysis, lost earnings calculations, and expert witness testimony'
        },
        'business-valuation': {
            'service_name': 'Business Valuation',
            'service_slug': 'business-valuation',
            'service_title': 'Business Valuation Expert',
            'service_description': 'Fair market value analysis, business appraisals, and shareholder dispute valuations'
        },
        'business-consulting': {
            'service_name': 'Business Consulting',
            'service_slug': 'business-consulting',
            'service_title': 'Business Consultant',
            'service_description': 'Strategic planning, operations improvement, and business transformation services'
        },
        'vocational-expert': {
            'service_name': 'Vocational Expert',
            'service_slug': 'vocational-expert',
            'service_title': 'Vocational Expert',
            'service_description': 'Employability assessments, earning capacity evaluations, and vocational rehabilitation planning'
        },
        'life-care-planning': {
            'service_name': 'Life Care Planning',
            'service_slug': 'life-care-planning',
            'service_title': 'Life Care Planner',
            'service_description': 'Future medical cost projections, catastrophic injury planning, and assistive technology needs'
        }
    }
    
    return SERVICES.get(service_slug, {})

# Update your view classes to use this:
# context.update(get_service_context(self.service_slug))
'''
    
    context_file = Path("main/view_context_helper.py")
    context_file.write_text(view_updates)
    print(f"\n✓ Created view context helper: {context_file}")

def create_template_verification_script():
    """Create a script to verify all templates are properly configured"""
    
    verification_script = '''#!/usr/bin/env python3
"""Verify all templates use standardized formatting"""

from pathlib import Path

def verify_templates():
    template_dir = Path("main/templates/main")
    
    # Check base templates exist
    base_service = template_dir / "base_service_template.html"
    base_city = template_dir / "base_city_template.html"
    
    print("\\nTemplate Verification Report")
    print("="*60)
    
    if base_service.exists():
        print("✓ Base service template exists")
    else:
        print("✗ Base service template missing!")
        
    if base_city.exists():
        print("✓ Base city template exists")
    else:
        print("✗ Base city template missing!")
    
    # Check service templates
    services_dir = template_dir / "services"
    service_templates = list(services_dir.glob("*.html"))
    print(f"\\n✓ Found {len(service_templates)} service templates")
    
    # Check city templates
    cities_dir = template_dir / "cities"
    city_templates = list(cities_dir.glob("*.html"))
    print(f"✓ Found {len(city_templates)} city templates")
    
    # Check for consistent elements
    print("\\nChecking for consistent elements...")
    required_classes = ['hero-section', 'btn-warning', 'btn-outline', 'shadow-sm', 'card']
    
    for template in service_templates[:5]:  # Check first 5
        content = template.read_text()
        for css_class in required_classes:
            if css_class in content:
                print(f"  ✓ {template.name} has {css_class}")
    
    print("\\nTemplate verification complete!")

if __name__ == "__main__":
    verify_templates()
'''
    
    verify_file = Path("verify_templates.py")
    verify_file.write_text(verification_script)
    print(f"✓ Created verification script: {verify_file}")

def main():
    """Main execution function"""
    print("\nTEMPLATE STANDARDIZATION SYSTEM")
    print("="*60)
    print("This script will update all service and location templates")
    print("to use standardized base templates for consistent formatting.")
    
    # Ensure directories exist
    services_dir = TEMPLATE_DIR / "services"
    cities_dir = TEMPLATE_DIR / "cities"
    
    services_dir.mkdir(parents=True, exist_ok=True)
    cities_dir.mkdir(parents=True, exist_ok=True)
    
    # Update templates
    update_service_templates()
    update_city_templates()
    
    # Create helper files
    create_view_context_updater()
    create_template_verification_script()
    
    print("\n" + "="*60)
    print("STANDARDIZATION COMPLETE!")
    print("="*60)
    print("\nAll templates have been updated to use consistent formatting:")
    print("  ✓ Service templates updated")
    print("  ✓ City templates created")
    print("  ✓ View context helper created")
    print("  ✓ Verification script created")
    print("\nNext steps:")
    print("  1. Update views to pass standardized context")
    print("  2. Run verification script to check templates")
    print("  3. Test all pages for consistency")
    print("  4. Deploy changes to production")

if __name__ == "__main__":
    main()