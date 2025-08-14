"""
Comprehensive SEO Location System
Generates all location-based URLs for maximum SEO coverage
"""

from django.urls import path
from . import seo_location_views

# Core services for location combinations
CORE_SERVICES = [
    {
        'slug': 'forensic-economist',
        'title': 'Forensic Economist',
        'description': 'Expert forensic economics services'
    },
    {
        'slug': 'business-valuation',
        'title': 'Business Valuation Expert',
        'description': 'Professional business valuation and appraisal'
    },
    {
        'slug': 'personal-injury-economist',
        'title': 'Personal Injury Economist',
        'description': 'Economic damages for personal injury cases'
    },
    {
        'slug': 'wrongful-death-damages',
        'title': 'Wrongful Death Economic Expert',
        'description': 'Economic loss calculations for wrongful death'
    },
    {
        'slug': 'employment-litigation',
        'title': 'Employment Litigation Expert',
        'description': 'Economic analysis for employment disputes'
    },
    {
        'slug': 'lost-earnings-expert',
        'title': 'Lost Earnings Expert',
        'description': 'Lost wages and earnings capacity analysis'
    },
    {
        'slug': 'divorce-business-valuation',
        'title': 'Divorce Business Valuation',
        'description': 'Business valuation for divorce proceedings'
    },
    {
        'slug': 'economic-damages-expert',
        'title': 'Economic Damages Expert',
        'description': 'Comprehensive economic damage calculations'
    }
]

# Major metro areas for dedicated pages
METRO_AREAS = [
    {
        'slug': 'greater-boston-area',
        'name': 'Greater Boston Area',
        'states': ['MA'],
        'cities': ['Boston', 'Cambridge', 'Quincy', 'Newton', 'Somerville'],
        'description': 'Serving the Greater Boston metropolitan area'
    },
    {
        'slug': 'new-york-metro',
        'name': 'New York Metropolitan Area',
        'states': ['NY', 'NJ', 'CT'],
        'cities': ['New York City', 'Newark', 'Jersey City', 'Yonkers', 'Stamford'],
        'description': 'Covering the tri-state New York metropolitan region'
    },
    {
        'slug': 'philadelphia-metro',
        'name': 'Greater Philadelphia',
        'states': ['PA', 'NJ', 'DE'],
        'cities': ['Philadelphia', 'Camden', 'Wilmington', 'Chester'],
        'description': 'Serving the Delaware Valley region'
    },
    {
        'slug': 'washington-dc-metro',
        'name': 'Washington DC Metro Area',
        'states': ['DC', 'VA', 'MD'],
        'cities': ['Washington', 'Arlington', 'Alexandria', 'Bethesda'],
        'description': 'National Capital Region coverage'
    },
    {
        'slug': 'san-francisco-bay-area',
        'name': 'San Francisco Bay Area',
        'states': ['CA'],
        'cities': ['San Francisco', 'Oakland', 'San Jose', 'Berkeley', 'Palo Alto'],
        'description': 'Bay Area forensic economics services'
    },
    {
        'slug': 'los-angeles-metro',
        'name': 'Greater Los Angeles',
        'states': ['CA'],
        'cities': ['Los Angeles', 'Long Beach', 'Anaheim', 'Santa Monica', 'Pasadena'],
        'description': 'Southern California metropolitan coverage'
    },
    {
        'slug': 'chicago-metro',
        'name': 'Chicagoland',
        'states': ['IL', 'IN', 'WI'],
        'cities': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville'],
        'description': 'Chicago metropolitan area services'
    },
    {
        'slug': 'dallas-fort-worth',
        'name': 'Dallas-Fort Worth Metroplex',
        'states': ['TX'],
        'cities': ['Dallas', 'Fort Worth', 'Arlington', 'Plano', 'Irving'],
        'description': 'DFW Metroplex coverage'
    },
    {
        'slug': 'miami-metro',
        'name': 'Greater Miami',
        'states': ['FL'],
        'cities': ['Miami', 'Fort Lauderdale', 'West Palm Beach', 'Miami Beach'],
        'description': 'South Florida metropolitan services'
    },
    {
        'slug': 'atlanta-metro',
        'name': 'Metro Atlanta',
        'states': ['GA'],
        'cities': ['Atlanta', 'Sandy Springs', 'Roswell', 'Alpharetta', 'Marietta'],
        'description': 'Atlanta metropolitan area coverage'
    }
]

# State-level pages
US_STATES = {
    'alabama': {'name': 'Alabama', 'abbr': 'AL'},
    'alaska': {'name': 'Alaska', 'abbr': 'AK'},
    'arizona': {'name': 'Arizona', 'abbr': 'AZ'},
    'arkansas': {'name': 'Arkansas', 'abbr': 'AR'},
    'california': {'name': 'California', 'abbr': 'CA'},
    'colorado': {'name': 'Colorado', 'abbr': 'CO'},
    'connecticut': {'name': 'Connecticut', 'abbr': 'CT'},
    'delaware': {'name': 'Delaware', 'abbr': 'DE'},
    'florida': {'name': 'Florida', 'abbr': 'FL'},
    'georgia': {'name': 'Georgia', 'abbr': 'GA'},
    'hawaii': {'name': 'Hawaii', 'abbr': 'HI'},
    'idaho': {'name': 'Idaho', 'abbr': 'ID'},
    'illinois': {'name': 'Illinois', 'abbr': 'IL'},
    'indiana': {'name': 'Indiana', 'abbr': 'IN'},
    'iowa': {'name': 'Iowa', 'abbr': 'IA'},
    'kansas': {'name': 'Kansas', 'abbr': 'KS'},
    'kentucky': {'name': 'Kentucky', 'abbr': 'KY'},
    'louisiana': {'name': 'Louisiana', 'abbr': 'LA'},
    'maine': {'name': 'Maine', 'abbr': 'ME'},
    'maryland': {'name': 'Maryland', 'abbr': 'MD'},
    'massachusetts': {'name': 'Massachusetts', 'abbr': 'MA'},
    'michigan': {'name': 'Michigan', 'abbr': 'MI'},
    'minnesota': {'name': 'Minnesota', 'abbr': 'MN'},
    'mississippi': {'name': 'Mississippi', 'abbr': 'MS'},
    'missouri': {'name': 'Missouri', 'abbr': 'MO'},
    'montana': {'name': 'Montana', 'abbr': 'MT'},
    'nebraska': {'name': 'Nebraska', 'abbr': 'NE'},
    'nevada': {'name': 'Nevada', 'abbr': 'NV'},
    'new-hampshire': {'name': 'New Hampshire', 'abbr': 'NH'},
    'new-jersey': {'name': 'New Jersey', 'abbr': 'NJ'},
    'new-mexico': {'name': 'New Mexico', 'abbr': 'NM'},
    'new-york': {'name': 'New York', 'abbr': 'NY'},
    'north-carolina': {'name': 'North Carolina', 'abbr': 'NC'},
    'north-dakota': {'name': 'North Dakota', 'abbr': 'ND'},
    'ohio': {'name': 'Ohio', 'abbr': 'OH'},
    'oklahoma': {'name': 'Oklahoma', 'abbr': 'OK'},
    'oregon': {'name': 'Oregon', 'abbr': 'OR'},
    'pennsylvania': {'name': 'Pennsylvania', 'abbr': 'PA'},
    'rhode-island': {'name': 'Rhode Island', 'abbr': 'RI'},
    'south-carolina': {'name': 'South Carolina', 'abbr': 'SC'},
    'south-dakota': {'name': 'South Dakota', 'abbr': 'SD'},
    'tennessee': {'name': 'Tennessee', 'abbr': 'TN'},
    'texas': {'name': 'Texas', 'abbr': 'TX'},
    'utah': {'name': 'Utah', 'abbr': 'UT'},
    'vermont': {'name': 'Vermont', 'abbr': 'VT'},
    'virginia': {'name': 'Virginia', 'abbr': 'VA'},
    'washington': {'name': 'Washington', 'abbr': 'WA'},
    'west-virginia': {'name': 'West Virginia', 'abbr': 'WV'},
    'wisconsin': {'name': 'Wisconsin', 'abbr': 'WI'},
    'wyoming': {'name': 'Wyoming', 'abbr': 'WY'}
}

# Major counties for SEO
MAJOR_COUNTIES = [
    {'slug': 'los-angeles-county', 'name': 'Los Angeles County', 'state': 'CA'},
    {'slug': 'cook-county', 'name': 'Cook County', 'state': 'IL'},
    {'slug': 'harris-county', 'name': 'Harris County', 'state': 'TX'},
    {'slug': 'maricopa-county', 'name': 'Maricopa County', 'state': 'AZ'},
    {'slug': 'san-diego-county', 'name': 'San Diego County', 'state': 'CA'},
    {'slug': 'orange-county-ca', 'name': 'Orange County', 'state': 'CA'},
    {'slug': 'miami-dade-county', 'name': 'Miami-Dade County', 'state': 'FL'},
    {'slug': 'dallas-county', 'name': 'Dallas County', 'state': 'TX'},
    {'slug': 'riverside-county', 'name': 'Riverside County', 'state': 'CA'},
    {'slug': 'san-bernardino-county', 'name': 'San Bernardino County', 'state': 'CA'},
    {'slug': 'clark-county', 'name': 'Clark County', 'state': 'NV'},
    {'slug': 'king-county', 'name': 'King County', 'state': 'WA'},
    {'slug': 'tarrant-county', 'name': 'Tarrant County', 'state': 'TX'},
    {'slug': 'santa-clara-county', 'name': 'Santa Clara County', 'state': 'CA'},
    {'slug': 'broward-county', 'name': 'Broward County', 'state': 'FL'},
    {'slug': 'bexar-county', 'name': 'Bexar County', 'state': 'TX'},
    {'slug': 'wayne-county', 'name': 'Wayne County', 'state': 'MI'},
    {'slug': 'alameda-county', 'name': 'Alameda County', 'state': 'CA'},
    {'slug': 'middlesex-county-ma', 'name': 'Middlesex County', 'state': 'MA'},
    {'slug': 'suffolk-county-ma', 'name': 'Suffolk County', 'state': 'MA'},
    {'slug': 'philadelphia-county', 'name': 'Philadelphia County', 'state': 'PA'},
    {'slug': 'sacramento-county', 'name': 'Sacramento County', 'state': 'CA'},
    {'slug': 'palm-beach-county', 'name': 'Palm Beach County', 'state': 'FL'},
    {'slug': 'nassau-county-ny', 'name': 'Nassau County', 'state': 'NY'},
    {'slug': 'suffolk-county-ny', 'name': 'Suffolk County', 'state': 'NY'},
    {'slug': 'cuyahoga-county', 'name': 'Cuyahoga County', 'state': 'OH'},
    {'slug': 'allegheny-county', 'name': 'Allegheny County', 'state': 'PA'},
    {'slug': 'hennepin-county', 'name': 'Hennepin County', 'state': 'MN'},
    {'slug': 'fairfax-county', 'name': 'Fairfax County', 'state': 'VA'},
    {'slug': 'contra-costa-county', 'name': 'Contra Costa County', 'state': 'CA'},
    {'slug': 'montgomery-county-md', 'name': 'Montgomery County', 'state': 'MD'},
    {'slug': 'fulton-county', 'name': 'Fulton County', 'state': 'GA'},
    {'slug': 'wake-county', 'name': 'Wake County', 'state': 'NC'},
    {'slug': 'westchester-county', 'name': 'Westchester County', 'state': 'NY'},
    {'slug': 'milwaukee-county', 'name': 'Milwaukee County', 'state': 'WI'},
    {'slug': 'mecklenburg-county', 'name': 'Mecklenburg County', 'state': 'NC'}
]

def generate_all_location_urls():
    """Generate all location-based URL patterns"""
    urlpatterns = []
    
    # State-level pages
    for state_slug, state_data in US_STATES.items():
        urlpatterns.append(
            path(f'forensic-economist-{state_slug}/', 
                 seo_location_views.state_page, 
                 {'state_slug': state_slug},
                 name=f'state-{state_slug}')
        )
        
        # State + Service combinations
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f'{service["slug"]}-{state_slug}/', 
                     seo_location_views.state_service_page,
                     {'state_slug': state_slug, 'service_slug': service['slug']},
                     name=f'{service["slug"]}-{state_slug}')
            )
    
    # Metro area pages
    for metro in METRO_AREAS:
        urlpatterns.append(
            path(f'{metro["slug"]}-economist/', 
                 seo_location_views.metro_area_page,
                 {'metro_slug': metro['slug']},
                 name=f'metro-{metro["slug"]}')
        )
        
        # Metro + Service combinations
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f'{metro["slug"]}-{service["slug"]}/', 
                     seo_location_views.metro_service_page,
                     {'metro_slug': metro['slug'], 'service_slug': service['slug']},
                     name=f'{metro["slug"]}-{service["slug"]}')
            )
    
    # County pages
    for county in MAJOR_COUNTIES:
        urlpatterns.append(
            path(f'{county["slug"]}-economist/', 
                 seo_location_views.county_page,
                 {'county_slug': county['slug']},
                 name=f'county-{county["slug"]}')
        )
        
        # County + Service combinations  
        for service in CORE_SERVICES:
            urlpatterns.append(
                path(f'{county["slug"]}-{service["slug"]}/', 
                     seo_location_views.county_service_page,
                     {'county_slug': county['slug'], 'service_slug': service['slug']},
                     name=f'{county["slug"]}-{service["slug"]}')
            )
    
    return urlpatterns

# Export data for use in views
SEO_LOCATION_DATA = {
    'services': CORE_SERVICES,
    'metro_areas': METRO_AREAS,
    'states': US_STATES,
    'counties': MAJOR_COUNTIES
}