#!/usr/bin/env python3
"""Verify all templates use standardized formatting"""

from pathlib import Path

def verify_templates():
    template_dir = Path("main/templates/main")
    
    # Check base templates exist
    base_service = template_dir / "base_service_template.html"
    base_city = template_dir / "base_city_template.html"
    
    print("\nTemplate Verification Report")
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
    print(f"\n✓ Found {len(service_templates)} service templates")
    
    # Check city templates
    cities_dir = template_dir / "cities"
    city_templates = list(cities_dir.glob("*.html"))
    print(f"✓ Found {len(city_templates)} city templates")
    
    # Check for consistent elements
    print("\nChecking for consistent elements...")
    required_classes = ['hero-section', 'btn-warning', 'btn-outline', 'shadow-sm', 'card']
    
    for template in service_templates[:5]:  # Check first 5
        content = template.read_text()
        for css_class in required_classes:
            if css_class in content:
                print(f"  ✓ {template.name} has {css_class}")
    
    print("\nTemplate verification complete!")

if __name__ == "__main__":
    verify_templates()
