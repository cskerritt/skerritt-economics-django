"""
Comprehensive US Cities Data for SEO Landing Pages
Merged from multiple regional datasets to provide complete nationwide coverage
Includes top 20+ cities by population for all 50 US states plus DC
Over 1000+ cities total with state, county, geographic coordinates, and metro area data

Data Sources:
- Original us_cities_seo_data.py (top national cities)
- western_states_cities_data.py (Western US states)  
- midwest_central_cities_data.py (Midwest and Central states)
- northeast_cities_data.py (Northeast states)

Updated: January 2025
"""

# Import data from regional files
import sys
import os

# Add the project root to Python path to import the regional data files
sys.path.append("/Users/chrisskerritt/skerritt_economics_django")

try:
    from western_states_cities_data import WESTERN_STATES_CITIES
    from midwest_central_cities_data import MIDWEST_CENTRAL_CITIES  
    from northeast_cities_data import NORTHEAST_CITIES
except ImportError as e:
    print(f"Warning: Could not import regional data files: {e}")
    WESTERN_STATES_CITIES = {}
    MIDWEST_CENTRAL_CITIES = {}
    NORTHEAST_CITIES = {}

# Base comprehensive city data dictionary - merging all sources
US_MAJOR_CITIES = {
    # Top National Cities (from original file)
    "new-york": {
        "name": "New York",
        "state": "New York",
        "state_abbr": "NY",
        "county": "New York County",
        "population": 8336817,
        "lat": 40.7128,
        "lng": -74.0060,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "los-angeles": {
        "name": "Los Angeles",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 3979576,
        "lat": 34.0522,
        "lng": -118.2437,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "chicago": {
        "name": "Chicago",
        "state": "Illinois",
        "state_abbr": "IL",
        "county": "Cook County",
        "population": 2693976,
        "lat": 41.8781,
        "lng": -87.6298,
        "metro_area": "Chicago-Naperville-Elgin",
        "region": "Midwest"
    },
    "houston": {
        "name": "Houston",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Harris County",
        "population": 2320268,
        "lat": 29.7604,
        "lng": -95.3698,
        "metro_area": "Houston-The Woodlands-Sugar Land",
        "region": "South"
    },
    "phoenix": {
        "name": "Phoenix",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 1680992,
        "lat": 33.4484,
        "lng": -112.0740,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "philadelphia": {
        "name": "Philadelphia",
        "state": "Pennsylvania",
        "state_abbr": "PA",
        "county": "Philadelphia County",
        "population": 1584064,
        "lat": 39.9526,
        "lng": -75.1652,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "san-antonio": {
        "name": "San Antonio",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Bexar County",
        "population": 1547253,
        "lat": 29.4241,
        "lng": -98.4936,
        "metro_area": "San Antonio-New Braunfels",
        "region": "South"
    },
    "san-diego": {
        "name": "San Diego",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Diego County",
        "population": 1423851,
        "lat": 32.7157,
        "lng": -117.1611,
        "metro_area": "San Diego-Carlsbad",
        "region": "West"
    },
    "dallas": {
        "name": "Dallas",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 1343573,
        "lat": 32.7767,
        "lng": -96.7970,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "san-jose": {
        "name": "San Jose",
        "state": "California",
        "state_abbr": "CA",
        "county": "Santa Clara County",
        "population": 1021795,
        "lat": 37.3382,
        "lng": -121.8863,
        "metro_area": "San Jose-Sunnyvale-Santa Clara",
        "region": "West"
    }
}

def merge_regional_data():
    """Merge all regional city data into the main dictionary"""
    global US_MAJOR_CITIES
    
    # Track duplicates for logging
    duplicates = []
    cities_added = 0
    
    # Merge Western States data
    for city_slug, city_data in WESTERN_STATES_CITIES.items():
        if city_slug not in US_MAJOR_CITIES:
            US_MAJOR_CITIES[city_slug] = city_data
            cities_added += 1
        else:
            duplicates.append(f"{city_slug} (Western)")
    
    # Merge Midwest/Central data  
    for state_slug, state_data in MIDWEST_CENTRAL_CITIES.items():
        if "cities" in state_data:
            for city in state_data["cities"]:
                city_slug = city["slug"]
                # Convert to standard format
                city_data = {
                    "name": city["name"],
                    "state": state_data["name"], 
                    "state_abbr": state_data["state_abbr"],
                    "county": city["county"],
                    "population": city["population"],
                    "lat": city["lat"],
                    "lng": city["lng"],
                    "metro_area": city["metro_area"],
                    "region": city["region"]
                }
                if city_slug not in US_MAJOR_CITIES:
                    US_MAJOR_CITIES[city_slug] = city_data
                    cities_added += 1
                else:
                    duplicates.append(f"{city_slug} (Midwest)")
    
    # Merge Northeast data
    for city_slug, city_data in NORTHEAST_CITIES.items():
        if city_slug not in US_MAJOR_CITIES:
            US_MAJOR_CITIES[city_slug] = city_data
            cities_added += 1
        else:
            duplicates.append(f"{city_slug} (Northeast)")
    
    print(f"Merged {cities_added} new cities")
    if duplicates:
        print(f"Found {len(duplicates)} duplicates (kept original): {", ".join(duplicates[:10])}")
        if len(duplicates) > 10:
            print(f"... and {len(duplicates) - 10} more")

# Add missing states with major cities
ADDITIONAL_CITIES = {
    # ALASKA (missing from other files)
    "anchorage": {
        "name": "Anchorage",
        "state": "Alaska", 
        "state_abbr": "AK",
        "county": "Anchorage Municipality",
        "population": 291538,
        "lat": 61.2181,
        "lng": -149.9003,
        "metro_area": "Anchorage",
        "region": "Alaska"
    },
    "juneau": {
        "name": "Juneau",
        "state": "Alaska",
        "state_abbr": "AK", 
        "county": "Juneau Borough",
        "population": 32255,
        "lat": 58.3019,
        "lng": -134.4197,
        "metro_area": "Juneau",
        "region": "Alaska"
    },
    "fairbanks": {
        "name": "Fairbanks",
        "state": "Alaska",
        "state_abbr": "AK",
        "county": "Fairbanks North Star Borough", 
        "population": 31427,
        "lat": 64.8378,
        "lng": -147.7164,
        "metro_area": "Fairbanks",
        "region": "Alaska"
    },
    "ketchikan": {
        "name": "Ketchikan",
        "state": "Alaska",
        "state_abbr": "AK",
        "county": "Ketchikan Gateway Borough",
        "population": 8192,
        "lat": 55.3422,
        "lng": -131.6464,
        "metro_area": "Ketchikan",
        "region": "Alaska"
    },
    "sitka": {
        "name": "Sitka", 
        "state": "Alaska",
        "state_abbr": "AK",
        "county": "Sitka Borough",
        "population": 8458,
        "lat": 57.0531,
        "lng": -135.3300,
        "metro_area": "Sitka",
        "region": "Alaska"
    },

    # HAWAII (missing from other files)
    "honolulu": {
        "name": "Honolulu",
        "state": "Hawaii",
        "state_abbr": "HI",
        "county": "Honolulu County",
        "population": 345064,
        "lat": 21.3099,
        "lng": -157.8581,
        "metro_area": "Urban Honolulu",
        "region": "Pacific"
    },
    "pearl-city": {
        "name": "Pearl City",
        "state": "Hawaii",
        "state_abbr": "HI",
        "county": "Honolulu County",
        "population": 47698,
        "lat": 21.3972,
        "lng": -157.9750,
        "metro_area": "Urban Honolulu",
        "region": "Pacific"
    },
    "hilo": {
        "name": "Hilo",
        "state": "Hawaii", 
        "state_abbr": "HI",
        "county": "Hawaii County",
        "population": 45248,
        "lat": 19.7297,
        "lng": -155.0900,
        "metro_area": "Hilo",
        "region": "Pacific"
    },
    "kailua-kona": {
        "name": "Kailua-Kona",
        "state": "Hawaii",
        "state_abbr": "HI", 
        "county": "Hawaii County",
        "population": 23431,
        "lat": 19.6389,
        "lng": -155.9969,
        "metro_area": "Kailua-Kona", 
        "region": "Pacific"
    },
    "kailua": {
        "name": "Kailua",
        "state": "Hawaii",
        "state_abbr": "HI",
        "county": "Honolulu County", 
        "population": 38635,
        "lat": 21.4022,
        "lng": -157.7394,
        "metro_area": "Urban Honolulu",
        "region": "Pacific"
    },

    # Additional Southern Cities (enhance coverage)
    "atlanta": {
        "name": "Atlanta",
        "state": "Georgia",
        "state_abbr": "GA",
        "county": "Fulton County",
        "population": 498715,
        "lat": 33.7490,
        "lng": -84.3880,
        "metro_area": "Atlanta-Sandy Springs-Roswell",
        "region": "South"
    },
    "savannah": {
        "name": "Savannah",
        "state": "Georgia",
        "state_abbr": "GA",
        "county": "Chatham County",
        "population": 145862,
        "lat": 32.0835,
        "lng": -81.0998,
        "metro_area": "Savannah",
        "region": "South"
    },
    "miami": {
        "name": "Miami",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Miami-Dade County",
        "population": 467963,
        "lat": 25.7617,
        "lng": -80.1918,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "orlando": {
        "name": "Orlando",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Orange County",
        "population": 287442,
        "lat": 28.5383,
        "lng": -81.3792,
        "metro_area": "Orlando-Kissimmee-Sanford",
        "region": "South"
    },
    "tampa": {
        "name": "Tampa",
        "state": "Florida", 
        "state_abbr": "FL",
        "county": "Hillsborough County",
        "population": 399700,
        "lat": 27.9506,
        "lng": -82.4572,
        "metro_area": "Tampa-St. Petersburg-Clearwater",
        "region": "South"
    },
    
    # Additional cities from missing states
    "charleston-sc": {
        "name": "Charleston",
        "state": "South Carolina",
        "state_abbr": "SC",
        "county": "Charleston County",
        "population": 137566,
        "lat": 32.7765,
        "lng": -79.9311,
        "metro_area": "Charleston-North Charleston",
        "region": "South"
    },
    "charlotte": {
        "name": "Charlotte",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Mecklenburg County",
        "population": 885708,
        "lat": 35.2271,
        "lng": -80.8431,
        "metro_area": "Charlotte-Concord-Gastonia", 
        "region": "South"
    },
    "nashville": {
        "name": "Nashville",
        "state": "Tennessee",
        "state_abbr": "TN",
        "county": "Davidson County",
        "population": 670820,
        "lat": 36.1627,
        "lng": -86.7816,
        "metro_area": "Nashville-Davidson-Murfreesboro-Franklin",
        "region": "South"
    },
    "memphis": {
        "name": "Memphis",
        "state": "Tennessee",
        "state_abbr": "TN",
        "county": "Shelby County",
        "population": 651073,
        "lat": 35.1495,
        "lng": -90.0490,
        "metro_area": "Memphis",
        "region": "South"
    },
    "louisville": {
        "name": "Louisville",
        "state": "Kentucky",
        "state_abbr": "KY",
        "county": "Jefferson County",
        "population": 617638,
        "lat": 38.2527,
        "lng": -85.7585,
        "metro_area": "Louisville-Jefferson County",
        "region": "South"
    },
    "new-orleans": {
        "name": "New Orleans",
        "state": "Louisiana",
        "state_abbr": "LA",
        "county": "Orleans Parish",
        "population": 390144,
        "lat": 29.9511,
        "lng": -90.0715,
        "metro_area": "New Orleans-Metairie",
        "region": "South"
    },
    "oklahoma-city": {
        "name": "Oklahoma City",
        "state": "Oklahoma",
        "state_abbr": "OK",
        "county": "Oklahoma County",
        "population": 649021,
        "lat": 35.4676,
        "lng": -97.5164,
        "metro_area": "Oklahoma City",
        "region": "South"
    },
    "tulsa": {
        "name": "Tulsa",
        "state": "Oklahoma",
        "state_abbr": "OK",
        "county": "Tulsa County",
        "population": 401800,
        "lat": 36.1540,
        "lng": -95.9928,
        "metro_area": "Tulsa",
        "region": "South"
    },
    "little-rock": {
        "name": "Little Rock",
        "state": "Arkansas",
        "state_abbr": "AR",
        "county": "Pulaski County",
        "population": 197312,
        "lat": 34.7465,
        "lng": -92.2896,
        "metro_area": "Little Rock-North Little Rock-Conway",
        "region": "South"
    },
    "jackson": {
        "name": "Jackson",
        "state": "Mississippi",
        "state_abbr": "MS",
        "county": "Hinds County",
        "population": 160628,
        "lat": 32.2988,
        "lng": -90.1848,
        "metro_area": "Jackson",
        "region": "South"
    },
    "birmingham": {
        "name": "Birmingham",
        "state": "Alabama",
        "state_abbr": "AL",
        "county": "Jefferson County",
        "population": 209403,
        "lat": 33.5186,
        "lng": -86.8104,
        "metro_area": "Birmingham-Hoover",
        "region": "South"
    },
    "huntsville": {
        "name": "Huntsville",
        "state": "Alabama",
        "state_abbr": "AL",
        "county": "Madison County",
        "population": 200574,
        "lat": 34.7304,
        "lng": -86.5861,
        "metro_area": "Huntsville",
        "region": "South"
    },
    "mobile": {
        "name": "Mobile",
        "state": "Alabama",
        "state_abbr": "AL",
        "county": "Mobile County",
        "population": 188720,
        "lat": 30.6954,
        "lng": -88.0399,
        "metro_area": "Mobile",
        "region": "South"
    },
    
    # Add more cities to ensure comprehensive coverage
    "seattle": {
        "name": "Seattle", 
        "state": "Washington",
        "state_abbr": "WA",
        "county": "King County",
        "population": 753675,
        "lat": 47.6062,
        "lng": -122.3321,
        "metro_area": "Seattle-Tacoma-Bellevue",
        "region": "West"
    },
    "portland": {
        "name": "Portland",
        "state": "Oregon", 
        "state_abbr": "OR",
        "county": "Multnomah County",
        "population": 654741,
        "lat": 45.5152,
        "lng": -122.6784,
        "metro_area": "Portland-Vancouver-Hillsboro",
        "region": "West"
    },
    "denver": {
        "name": "Denver",
        "state": "Colorado",
        "state_abbr": "CO", 
        "county": "Denver County",
        "population": 727211,
        "lat": 39.7392,
        "lng": -104.9903,
        "metro_area": "Denver-Aurora-Lakewood",
        "region": "West"
    },
    "las-vegas": {
        "name": "Las Vegas",
        "state": "Nevada",
        "state_abbr": "NV",
        "county": "Clark County",
        "population": 648224,
        "lat": 36.1699,
        "lng": -115.1398,
        "metro_area": "Las Vegas-Henderson-Paradise",
        "region": "West"
    }
}

# Merge the data
merge_regional_data()

# Add additional cities to fill gaps
for city_slug, city_data in ADDITIONAL_CITIES.items():
    if city_slug not in US_MAJOR_CITIES:
        US_MAJOR_CITIES[city_slug] = city_data

def get_city_by_slug(slug):
    """Get city data by slug"""
    return US_MAJOR_CITIES.get(slug)

def get_cities_by_state(state_abbr):
    """Get all cities in a specific state"""
    return {
        slug: city for slug, city in US_MAJOR_CITIES.items()
        if city["state_abbr"] == state_abbr
    }

def get_cities_by_state_name(state_name):
    """Get all cities in a specific state by name"""
    return {
        slug: city for slug, city in US_MAJOR_CITIES.items()
        if city["state"].lower() == state_name.lower()
    }

def get_nearby_cities(city_slug, limit=6):
    """Get nearby cities based on geographic proximity"""
    city = US_MAJOR_CITIES.get(city_slug)
    if not city:
        return []
    
    # For simplicity, return cities in same state or metro area
    nearby = []
    
    # First, add cities in same metro area
    for slug, other_city in US_MAJOR_CITIES.items():
        if slug != city_slug and other_city.get("metro_area") == city.get("metro_area"):
            nearby.append({
                "slug": slug,
                "name": other_city["name"],
                "state_abbr": other_city["state_abbr"]
            })
            if len(nearby) >= limit:
                return nearby[:limit]
    
    # Then add cities in same state
    for slug, other_city in US_MAJOR_CITIES.items():
        if slug != city_slug and other_city["state_abbr"] == city["state_abbr"]:
            if not any(n["slug"] == slug for n in nearby):
                nearby.append({
                    "slug": slug,
                    "name": other_city["name"],
                    "state_abbr": other_city["state_abbr"]
                })
                if len(nearby) >= limit:
                    return nearby[:limit]
    
    return nearby[:limit]

def get_top_cities_by_population(limit=50):
    """Get top cities by population"""
    sorted_cities = sorted(
        US_MAJOR_CITIES.items(),
        key=lambda x: x[1]["population"],
        reverse=True
    )
    return dict(sorted_cities[:limit])

def get_cities_by_region(region):
    """Get all cities in a specific region"""
    return {
        slug: city for slug, city in US_MAJOR_CITIES.items()
        if city.get("region", "").lower() == region.lower()
    }

def get_states_list():
    """Get list of all states with cities in the database"""
    states = {}
    for city_data in US_MAJOR_CITIES.values():
        state_abbr = city_data["state_abbr"]
        state_name = city_data["state"]
        if state_abbr not in states:
            states[state_abbr] = {
                "name": state_name,
                "abbr": state_abbr,
                "city_count": 0
            }
        states[state_abbr]["city_count"] += 1
    
    return dict(sorted(states.items()))

def get_database_stats():
    """Get comprehensive statistics about the city database"""
    total_cities = len(US_MAJOR_CITIES)
    states = get_states_list()
    total_states = len(states)
    
    # Population statistics
    populations = [city["population"] for city in US_MAJOR_CITIES.values()]
    avg_population = sum(populations) / len(populations) if populations else 0
    
    # Regional breakdown
    regions = {}
    for city in US_MAJOR_CITIES.values():
        region = city.get("region", "Unknown")
        regions[region] = regions.get(region, 0) + 1
    
    return {
        "total_cities": total_cities,
        "total_states": total_states,
        "avg_cities_per_state": round(total_cities / total_states, 1) if total_states > 0 else 0,
        "avg_population": round(avg_population),
        "largest_city": max(US_MAJOR_CITIES.items(), key=lambda x: x[1]["population"]) if US_MAJOR_CITIES else None,
        "smallest_city": min(US_MAJOR_CITIES.items(), key=lambda x: x[1]["population"]) if US_MAJOR_CITIES else None,
        "regional_breakdown": regions,
        "states_coverage": states
    }

# Print statistics when module is imported
if __name__ == "__main__":
    stats = get_database_stats()
    print(f"\n=== US Cities SEO Database Statistics ===")
    print(f"Total Cities: {stats["total_cities"]}")
    print(f"States Covered: {stats["total_states"]}/50")  
    print(f"Average Cities per State: {stats["avg_cities_per_state"]}")
    print(f"Average Population: {stats["avg_population"]:,}")
    if stats["largest_city"]:
        print(f"Largest City: {stats["largest_city"][1]["name"]}, {stats["largest_city"][1]["state_abbr"]} ({stats["largest_city"][1]["population"]:,})")
    if stats["smallest_city"]:
        print(f"Smallest City: {stats["smallest_city"][1]["name"]}, {stats["smallest_city"][1]["state_abbr"]} ({stats["smallest_city"][1]["population"]:,})")
    
    print(f"\nRegional Coverage:")
    for region, count in sorted(stats["regional_breakdown"].items()):
        print(f"  {region}: {count} cities")
    
    print(f"\nState Coverage Summary:")
    under_20 = [state for state, data in stats["states_coverage"].items() if data["city_count"] < 20]
    if under_20:
        print(f"States with <20 cities: {", ".join(under_20)}")
    else:
        print("All states have 20+ cities ✓")
        
    print(f"===========================================\n")