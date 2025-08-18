from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Location data with SEO-optimized content
LOCATION_DATA = {
    "boston": {
        "city": "Boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "population": "675,647",
        "metro_population": "4.9 million",
        "description": "Expert forensic economics and business valuation services for Boston attorneys and businesses. Serving Suffolk, Middlesex, and Norfolk counties.",
        "meta_description": "Boston forensic economist & business valuation expert. Economic damage calculations for personal injury, wrongful death & commercial litigation. Free consultation: (203) 605-2814",
        "services_focus": ["Personal Injury Economic Analysis", "Medical Malpractice Damages", "Employment Litigation Support", "Business Interruption Claims"],
        "local_courts": ["Massachusetts Superior Court", "U.S. District Court for Massachusetts", "Suffolk County Superior Court"],
        "nearby_cities": ["Cambridge", "Quincy", "Newton", "Somerville", "Brookline"],
        "testimonial": {
            "text": "Mr. Skerritt provided exceptional economic analysis for our complex medical malpractice case in Boston. His testimony was clear and compelling.",
            "author": "Boston Trial Attorney"
        }
    },
    "providence": {
        "city": "Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "population": "190,934",
        "metro_population": "1.6 million",
        "description": "Leading forensic economist serving Providence law firms and businesses. Specializing in economic damages, lost earnings, and business valuation.",
        "meta_description": "Providence RI forensic economist. Expert witness for economic damages, lost earnings & business valuation. Serving all Rhode Island courts. Call (203) 605-2814",
        "services_focus": ["Wrongful Death Economic Loss", "Construction Defect Damages", "Professional Malpractice", "Divorce Business Valuation"],
        "local_courts": ["Rhode Island Superior Court", "U.S. District Court for Rhode Island", "Providence County Superior Court"],
        "nearby_cities": ["Warwick", "Cranston", "Pawtucket", "East Providence", "Newport"],
        "testimonial": {
            "text": "Christopher Skerritt is our go-to expert for economic damage calculations in Providence. His reports are thorough and his testimony is always well-received.",
            "author": "Providence Personal Injury Firm"
        }
    },
    "hartford": {
        "city": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "population": "121,054",
        "metro_population": "1.2 million",
        "description": "Trusted forensic economist for Hartford attorneys. Expert economic analysis for insurance disputes, personal injury, and commercial litigation.",
        "meta_description": "Hartford CT forensic economist & valuation expert. Economic damages for insurance claims, personal injury & business disputes. Free consultation: (203) 605-2814",
        "services_focus": ["Insurance Claim Disputes", "Product Liability Damages", "Toxic Tort Economic Loss", "Partnership Disputes"],
        "local_courts": ["Connecticut Superior Court", "U.S. District Court for Connecticut", "Hartford Judicial District"],
        "nearby_cities": ["West Hartford", "East Hartford", "Manchester", "New Britain", "Middletown"],
        "testimonial": {
            "text": "We have used Skerritt Economics for multiple insurance coverage disputes. Their analysis is always detailed and defensible.",
            "author": "Hartford Insurance Defense Attorney"
        }
    },
    "portland": {
        "city": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "population": "68,408",
        "metro_population": "550,000",
        "description": "Expert forensic economics services for Portland and Southern Maine. Specializing in maritime injuries, fishing industry losses, and business valuation.",
        "meta_description": "Portland Maine forensic economist. Maritime injury damages, fishing industry losses & business valuation expert. Serving all Maine courts. (203) 605-2814",
        "services_focus": ["Maritime Injury Economics", "Fishing Industry Losses", "Tourism Business Valuation", "Forestry Economic Analysis"],
        "local_courts": ["Maine Superior Court", "U.S. District Court for Maine", "Cumberland County Superior Court"],
        "nearby_cities": ["South Portland", "Westbrook", "Biddeford", "Saco", "Brunswick"],
        "testimonial": {
            "text": "Mr. Skerritt understood the unique aspects of maritime economics in our Jones Act case. His expertise was invaluable.",
            "author": "Portland Maritime Attorney"
        }
    },
    "burlington": {
        "city": "Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "population": "44,743",
        "metro_population": "225,000",
        "description": "Vermont\"s premier forensic economist serving Burlington area law firms. Expert in agricultural losses, ski industry damages, and small business valuation.',
        "meta_description": "Burlington VT forensic economist. Agricultural losses, ski industry damages & small business valuation expert. Free consultation: (203) 605-2814",
        "services_focus": ["Agricultural Economic Loss", "Ski Resort Injury Damages", "Small Business Valuation", "Environmental Damage Assessment"],
        "local_courts": ["Vermont Superior Court", "U.S. District Court for Vermont", "Chittenden County Superior Court"],
        "nearby_cities": ["South Burlington", "Colchester", "Essex", "Williston", "Montpelier"],
        "testimonial": {
            "text": "Skerritt Economics provided excellent analysis of lost profits for our client\"s seasonal business. Highly recommended for Vermont cases.',
            "author": "Burlington Business Attorney"
        }
    },
    "manchester": {
        "city": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "population": "115,644",
        "metro_population": "420,000",
        "description": "Leading forensic economist for Manchester and Southern New Hampshire. Specializing in personal injury economics and business valuation.",
        "meta_description": "Manchester NH forensic economist & business valuation expert. Personal injury damages, lost earnings analysis. Serving all NH courts. Call (203) 605-2814",
        "services_focus": ["Personal Injury Economics", "Wrongful Termination Damages", "Business Partnership Disputes", "Medical Malpractice Loss"],
        "local_courts": ["New Hampshire Superior Court", "U.S. District Court for New Hampshire", "Hillsborough County Superior Court"],
        "nearby_cities": ["Nashua", "Concord", "Derry", "Salem", "Portsmouth"],
        "testimonial": {
            "text": "We regularly use Christopher Skerritt for economic damage calculations in our Manchester practice. His work is consistently excellent.",
            "author": "Manchester Litigation Firm"
        }
    }
}

def location_detail(request, location_slug):
    """Display location-specific landing page"""
    location = LOCATION_DATA.get(location_slug)
    
    if not location:
        raise Http404("Location not found")
    
    # Build context for template
    context = {
        "location": location,
        "page_title": f"{location["city"]} Forensic Economist | {location["state"]} Business Valuation Expert",
        "page_description": location["meta_description"],
        "breadcrumb_items": [
            {"name": "Home", "url": "/"},
            {"name": "Locations", "url": "/locations/"},
            {"name": f"{location["city"]}, {location["state_abbr"]}", "url": request.path}
        ]
    }
    
    return render(request, "main/locations/enhanced_location.html", context)

def all_locations(request):
    """Display all location pages"""
    context = {
        "locations": LOCATION_DATA,
        "page_title": "Service Locations | New England Forensic Economist",
        "page_description": "Forensic economics and business valuation services throughout New England. Serving Massachusetts, Rhode Island, Connecticut, Maine, Vermont, and New Hampshire.",
    }
    
    return render(request, "main/locations/all_locations_enhanced.html", context)