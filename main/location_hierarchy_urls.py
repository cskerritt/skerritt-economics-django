"""
Location hierarchy URLs for states and cities under /locations/states/ and /locations/cities/
"""

from django.urls import path
from .location_hierarchy_views import (
    StateLocationView,
    CityLocationView,
    CityServiceLocationView
)

# US States for location pages
US_STATES = [
    {"slug": "alabama", "name": "Alabama", "abbr": "AL"},
    {"slug": "alaska", "name": "Alaska", "abbr": "AK"},
    {"slug": "arizona", "name": "Arizona", "abbr": "AZ"},
    {"slug": "arkansas", "name": "Arkansas", "abbr": "AR"},
    {"slug": "california", "name": "California", "abbr": "CA"},
    {"slug": "colorado", "name": "Colorado", "abbr": "CO"},
    {"slug": "connecticut", "name": "Connecticut", "abbr": "CT"},
    {"slug": "delaware", "name": "Delaware", "abbr": "DE"},
    {"slug": "florida", "name": "Florida", "abbr": "FL"},
    {"slug": "georgia", "name": "Georgia", "abbr": "GA"},
    {"slug": "hawaii", "name": "Hawaii", "abbr": "HI"},
    {"slug": "idaho", "name": "Idaho", "abbr": "ID"},
    {"slug": "illinois", "name": "Illinois", "abbr": "IL"},
    {"slug": "indiana", "name": "Indiana", "abbr": "IN"},
    {"slug": "iowa", "name": "Iowa", "abbr": "IA"},
    {"slug": "kansas", "name": "Kansas", "abbr": "KS"},
    {"slug": "kentucky", "name": "Kentucky", "abbr": "KY"},
    {"slug": "louisiana", "name": "Louisiana", "abbr": "LA"},
    {"slug": "maine", "name": "Maine", "abbr": "ME"},
    {"slug": "maryland", "name": "Maryland", "abbr": "MD"},
    {"slug": "massachusetts", "name": "Massachusetts", "abbr": "MA"},
    {"slug": "michigan", "name": "Michigan", "abbr": "MI"},
    {"slug": "minnesota", "name": "Minnesota", "abbr": "MN"},
    {"slug": "mississippi", "name": "Mississippi", "abbr": "MS"},
    {"slug": "missouri", "name": "Missouri", "abbr": "MO"},
    {"slug": "montana", "name": "Montana", "abbr": "MT"},
    {"slug": "nebraska", "name": "Nebraska", "abbr": "NE"},
    {"slug": "nevada", "name": "Nevada", "abbr": "NV"},
    {"slug": "new-hampshire", "name": "New Hampshire", "abbr": "NH"},
    {"slug": "new-jersey", "name": "New Jersey", "abbr": "NJ"},
    {"slug": "new-mexico", "name": "New Mexico", "abbr": "NM"},
    {"slug": "new-york", "name": "New York", "abbr": "NY"},
    {"slug": "north-carolina", "name": "North Carolina", "abbr": "NC"},
    {"slug": "north-dakota", "name": "North Dakota", "abbr": "ND"},
    {"slug": "ohio", "name": "Ohio", "abbr": "OH"},
    {"slug": "oklahoma", "name": "Oklahoma", "abbr": "OK"},
    {"slug": "oregon", "name": "Oregon", "abbr": "OR"},
    {"slug": "pennsylvania", "name": "Pennsylvania", "abbr": "PA"},
    {"slug": "rhode-island", "name": "Rhode Island", "abbr": "RI"},
    {"slug": "south-carolina", "name": "South Carolina", "abbr": "SC"},
    {"slug": "south-dakota", "name": "South Dakota", "abbr": "SD"},
    {"slug": "tennessee", "name": "Tennessee", "abbr": "TN"},
    {"slug": "texas", "name": "Texas", "abbr": "TX"},
    {"slug": "utah", "name": "Utah", "abbr": "UT"},
    {"slug": "vermont", "name": "Vermont", "abbr": "VT"},
    {"slug": "virginia", "name": "Virginia", "abbr": "VA"},
    {"slug": "washington", "name": "Washington", "abbr": "WA"},
    {"slug": "west-virginia", "name": "West Virginia", "abbr": "WV"},
    {"slug": "wisconsin", "name": "Wisconsin", "abbr": "WI"},
    {"slug": "wyoming", "name": "Wyoming", "abbr": "WY"},
]

# Sample cities for location pages
SAMPLE_CITIES = [
    {"slug": "burlington-vt", "name": "Burlington", "state": "Vermont", "state_slug": "vermont"},
    {"slug": "boston-ma", "name": "Boston", "state": "Massachusetts", "state_slug": "massachusetts"},
    {"slug": "new-york-ny", "name": "New York", "state": "New York", "state_slug": "new-york"},
    {"slug": "los-angeles-ca", "name": "Los Angeles", "state": "California", "state_slug": "california"},
    {"slug": "chicago-il", "name": "Chicago", "state": "Illinois", "state_slug": "illinois"},
    {"slug": "houston-tx", "name": "Houston", "state": "Texas", "state_slug": "texas"},
    {"slug": "phoenix-az", "name": "Phoenix", "state": "Arizona", "state_slug": "arizona"},
    {"slug": "philadelphia-pa", "name": "Philadelphia", "state": "Pennsylvania", "state_slug": "pennsylvania"},
    {"slug": "san-antonio-tx", "name": "San Antonio", "state": "Texas", "state_slug": "texas"},
    {"slug": "san-diego-ca", "name": "San Diego", "state": "California", "state_slug": "california"},
    {"slug": "dallas-tx", "name": "Dallas", "state": "Texas", "state_slug": "texas"},
    {"slug": "miami-fl", "name": "Miami", "state": "Florida", "state_slug": "florida"},
    {"slug": "atlanta-ga", "name": "Atlanta", "state": "Georgia", "state_slug": "georgia"},
    {"slug": "seattle-wa", "name": "Seattle", "state": "Washington", "state_slug": "washington"},
    {"slug": "denver-co", "name": "Denver", "state": "Colorado", "state_slug": "colorado"},
    {"slug": "detroit-mi", "name": "Detroit", "state": "Michigan", "state_slug": "michigan"},
    {"slug": "minneapolis-mn", "name": "Minneapolis", "state": "Minnesota", "state_slug": "minnesota"},
    {"slug": "tampa-fl", "name": "Tampa", "state": "Florida", "state_slug": "florida"},
    {"slug": "orlando-fl", "name": "Orlando", "state": "Florida", "state_slug": "florida"},
    {"slug": "charlotte-nc", "name": "Charlotte", "state": "North Carolina", "state_slug": "north-carolina"},
    {"slug": "portland-or", "name": "Portland", "state": "Oregon", "state_slug": "oregon"},
    {"slug": "las-vegas-nv", "name": "Las Vegas", "state": "Nevada", "state_slug": "nevada"},
    {"slug": "milwaukee-wi", "name": "Milwaukee", "state": "Wisconsin", "state_slug": "wisconsin"},
    {"slug": "cleveland-oh", "name": "Cleveland", "state": "Ohio", "state_slug": "ohio"},
    {"slug": "columbus-oh", "name": "Columbus", "state": "Ohio", "state_slug": "ohio"},
    {"slug": "indianapolis-in", "name": "Indianapolis", "state": "Indiana", "state_slug": "indiana"},
    {"slug": "san-francisco-ca", "name": "San Francisco", "state": "California", "state_slug": "california"},
    {"slug": "nashville-tn", "name": "Nashville", "state": "Tennessee", "state_slug": "tennessee"},
    {"slug": "memphis-tn", "name": "Memphis", "state": "Tennessee", "state_slug": "tennessee"},
    {"slug": "baltimore-md", "name": "Baltimore", "state": "Maryland", "state_slug": "maryland"},
    {"slug": "providence-ri", "name": "Providence", "state": "Rhode Island", "state_slug": "rhode-island"},
    {"slug": "hartford-ct", "name": "Hartford", "state": "Connecticut", "state_slug": "connecticut"},
]

# Services for city location pages
SERVICES = [
    {"slug": "life-care-planner", "name": "Life Care Planner"},
    {"slug": "forensic-economist", "name": "Forensic Economist"},
    {"slug": "vocational-expert", "name": "Vocational Expert"},
    {"slug": "business-valuation", "name": "Business Valuation"},
]

location_hierarchy_urlpatterns = []

# State location pages under /locations/states/
for state in US_STATES:
    location_hierarchy_urlpatterns.append(
        path(
            f"locations/states/{state['slug']}/",
            StateLocationView.as_view(),
            name=f"location_state_{state['slug']}",
            kwargs={
                "state_slug": state["slug"],
                "state_name": state["name"],
                "state_abbr": state["abbr"]
            }
        )
    )

# City location pages under /locations/cities/
for city in SAMPLE_CITIES:
    # General city page - standardized with trailing slash
    location_hierarchy_urlpatterns.append(
        path(
            f"locations/cities/{city['slug']}/",
            CityLocationView.as_view(),
            name=f"location_city_{city['slug']}",
            kwargs={
                "city_slug": city["slug"],
                "city_name": city["name"],
                "state_name": city["state"],
                "state_slug": city["state_slug"]
            }
        )
    )
    
    # Service-specific city pages - standardized with trailing slash
    for service in SERVICES:
        location_hierarchy_urlpatterns.append(
            path(
                f"locations/cities/{city['slug']}-{service["slug"]}/",
                CityServiceLocationView.as_view(),
                name=f"location_city_{city['slug']}_{service["slug"].replace("-", "_")}",
                kwargs={
                    "city_slug": city["slug"],
                    "city_name": city["name"],
                    "state_name": city["state"],
                    "state_slug": city["state_slug"],
                    "service_slug": service["slug"],
                    "service_name": service["name"]
                }
            )
        )