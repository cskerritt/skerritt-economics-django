"""
Service area URLs with city-state format for vocational expert, forensic economist, 
life care planner, and business valuation services
"""

from django.urls import path
from .service_area_views import (
    ServiceAreaVocationalExpertView,
    ServiceAreaForensicEconomistView,
    ServiceAreaLifeCarePlannerView,
    ServiceAreaBusinessValuationView
)

# Major cities for each service
MAJOR_CITIES = [
    {'city': 'springfield', 'state': 'mo', 'city_name': 'Springfield', 'state_name': 'Missouri'},
    {'city': 'augusta', 'state': 'me', 'city_name': 'Augusta', 'state_name': 'Maine'},
    {'city': 'newcastle', 'state': 'wy', 'city_name': 'Newcastle', 'state_name': 'Wyoming'},
    {'city': 'washington', 'state': 'dc', 'city_name': 'Washington', 'state_name': 'District of Columbia'},
    {'city': 'boston', 'state': 'ma', 'city_name': 'Boston', 'state_name': 'Massachusetts'},
    {'city': 'new-york', 'state': 'ny', 'city_name': 'New York', 'state_name': 'New York'},
    {'city': 'los-angeles', 'state': 'ca', 'city_name': 'Los Angeles', 'state_name': 'California'},
    {'city': 'chicago', 'state': 'il', 'city_name': 'Chicago', 'state_name': 'Illinois'},
    {'city': 'houston', 'state': 'tx', 'city_name': 'Houston', 'state_name': 'Texas'},
    {'city': 'phoenix', 'state': 'az', 'city_name': 'Phoenix', 'state_name': 'Arizona'},
    {'city': 'philadelphia', 'state': 'pa', 'city_name': 'Philadelphia', 'state_name': 'Pennsylvania'},
    {'city': 'san-antonio', 'state': 'tx', 'city_name': 'San Antonio', 'state_name': 'Texas'},
    {'city': 'san-diego', 'state': 'ca', 'city_name': 'San Diego', 'state_name': 'California'},
    {'city': 'dallas', 'state': 'tx', 'city_name': 'Dallas', 'state_name': 'Texas'},
    {'city': 'miami', 'state': 'fl', 'city_name': 'Miami', 'state_name': 'Florida'},
    {'city': 'atlanta', 'state': 'ga', 'city_name': 'Atlanta', 'state_name': 'Georgia'},
    {'city': 'seattle', 'state': 'wa', 'city_name': 'Seattle', 'state_name': 'Washington'},
    {'city': 'denver', 'state': 'co', 'city_name': 'Denver', 'state_name': 'Colorado'},
    {'city': 'detroit', 'state': 'mi', 'city_name': 'Detroit', 'state_name': 'Michigan'},
    {'city': 'minneapolis', 'state': 'mn', 'city_name': 'Minneapolis', 'state_name': 'Minnesota'},
    {'city': 'tampa', 'state': 'fl', 'city_name': 'Tampa', 'state_name': 'Florida'},
    {'city': 'orlando', 'state': 'fl', 'city_name': 'Orlando', 'state_name': 'Florida'},
    {'city': 'charlotte', 'state': 'nc', 'city_name': 'Charlotte', 'state_name': 'North Carolina'},
    {'city': 'st-louis', 'state': 'mo', 'city_name': 'St. Louis', 'state_name': 'Missouri'},
    {'city': 'portland', 'state': 'or', 'city_name': 'Portland', 'state_name': 'Oregon'},
    {'city': 'sacramento', 'state': 'ca', 'city_name': 'Sacramento', 'state_name': 'California'},
    {'city': 'las-vegas', 'state': 'nv', 'city_name': 'Las Vegas', 'state_name': 'Nevada'},
    {'city': 'kansas-city', 'state': 'mo', 'city_name': 'Kansas City', 'state_name': 'Missouri'},
    {'city': 'milwaukee', 'state': 'wi', 'city_name': 'Milwaukee', 'state_name': 'Wisconsin'},
    {'city': 'cleveland', 'state': 'oh', 'city_name': 'Cleveland', 'state_name': 'Ohio'},
    {'city': 'columbus', 'state': 'oh', 'city_name': 'Columbus', 'state_name': 'Ohio'},
    {'city': 'indianapolis', 'state': 'in', 'city_name': 'Indianapolis', 'state_name': 'Indiana'},
    {'city': 'san-francisco', 'state': 'ca', 'city_name': 'San Francisco', 'state_name': 'California'},
    {'city': 'nashville', 'state': 'tn', 'city_name': 'Nashville', 'state_name': 'Tennessee'},
    {'city': 'memphis', 'state': 'tn', 'city_name': 'Memphis', 'state_name': 'Tennessee'},
    {'city': 'baltimore', 'state': 'md', 'city_name': 'Baltimore', 'state_name': 'Maryland'},
    {'city': 'louisville', 'state': 'ky', 'city_name': 'Louisville', 'state_name': 'Kentucky'},
    {'city': 'new-orleans', 'state': 'la', 'city_name': 'New Orleans', 'state_name': 'Louisiana'},
    {'city': 'salt-lake-city', 'state': 'ut', 'city_name': 'Salt Lake City', 'state_name': 'Utah'},
    {'city': 'richmond', 'state': 'va', 'city_name': 'Richmond', 'state_name': 'Virginia'},
    {'city': 'birmingham', 'state': 'al', 'city_name': 'Birmingham', 'state_name': 'Alabama'},
    {'city': 'rochester', 'state': 'ny', 'city_name': 'Rochester', 'state_name': 'New York'},
    {'city': 'providence', 'state': 'ri', 'city_name': 'Providence', 'state_name': 'Rhode Island'},
    {'city': 'omaha', 'state': 'ne', 'city_name': 'Omaha', 'state_name': 'Nebraska'},
    {'city': 'raleigh', 'state': 'nc', 'city_name': 'Raleigh', 'state_name': 'North Carolina'},
    {'city': 'hartford', 'state': 'ct', 'city_name': 'Hartford', 'state_name': 'Connecticut'},
    {'city': 'bridgeport', 'state': 'ct', 'city_name': 'Bridgeport', 'state_name': 'Connecticut'},
    {'city': 'buffalo', 'state': 'ny', 'city_name': 'Buffalo', 'state_name': 'New York'},
    {'city': 'albany', 'state': 'ny', 'city_name': 'Albany', 'state_name': 'New York'},
    {'city': 'salem', 'state': 'nh', 'city_name': 'Salem', 'state_name': 'New Hampshire'},
    {'city': 'charleston', 'state': 'wv', 'city_name': 'Charleston', 'state_name': 'West Virginia'},
    {'city': 'winooski', 'state': 'vt', 'city_name': 'Winooski', 'state_name': 'Vermont'},
]

service_area_urlpatterns = []

# Generate URLs for each service and city combination
for city_data in MAJOR_CITIES:
    city = city_data['city']
    state = city_data['state']
    
    # Vocational Expert URLs
    service_area_urlpatterns.append(
        path(
            f'vocational-expert/{city}-{state}/',
            ServiceAreaVocationalExpertView.as_view(),
            name=f'vocational_expert_{city}_{state}',
            kwargs={
                'city': city,
                'state': state,
                'city_name': city_data['city_name'],
                'state_name': city_data['state_name']
            }
        )
    )
    
    # Forensic Economist URLs
    service_area_urlpatterns.append(
        path(
            f'forensic-economist/{city}-{state}/',
            ServiceAreaForensicEconomistView.as_view(),
            name=f'forensic_economist_{city}_{state}',
            kwargs={
                'city': city,
                'state': state,
                'city_name': city_data['city_name'],
                'state_name': city_data['state_name']
            }
        )
    )
    
    # Life Care Planner URLs
    service_area_urlpatterns.append(
        path(
            f'life-care-planner/{city}-{state}/',
            ServiceAreaLifeCarePlannerView.as_view(),
            name=f'life_care_planner_{city}_{state}',
            kwargs={
                'city': city,
                'state': state,
                'city_name': city_data['city_name'],
                'state_name': city_data['state_name']
            }
        )
    )
    
    # Business Valuation URLs
    service_area_urlpatterns.append(
        path(
            f'business-valuation/{city}-{state}/',
            ServiceAreaBusinessValuationView.as_view(),
            name=f'business_valuation_{city}_{state}',
            kwargs={
                'city': city,
                'state': state,
                'city_name': city_data['city_name'],
                'state_name': city_data['state_name']
            }
        )
    )