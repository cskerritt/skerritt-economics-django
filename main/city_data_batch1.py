"""
Comprehensive city data for US states
"""

CITY_DATA = {
    "alabama": {
        "name": "Alabama",
        "abbr": "AL",
        "cities": [
            {"name": "Birmingham", "slug": "birmingham", "county": "Jefferson County", "lat": 33.5186, "lng": -86.8104},
            {"name": "Montgomery", "slug": "montgomery", "county": "Montgomery County", "lat": 32.3792, "lng": -86.3077},
            {"name": "Huntsville", "slug": "huntsville", "county": "Madison County", "lat": 34.7304, "lng": -86.5861},
            {"name": "Mobile", "slug": "mobile", "county": "Mobile County", "lat": 30.6954, "lng": -88.0399},
            {"name": "Tuscaloosa", "slug": "tuscaloosa", "county": "Tuscaloosa County", "lat": 33.2098, "lng": -87.5692},
            {"name": "Hoover", "slug": "hoover", "county": "Jefferson County", "lat": 33.4054, "lng": -86.8114},
            {"name": "Dothan", "slug": "dothan", "county": "Houston County", "lat": 31.2232, "lng": -85.3905},
            {"name": "Auburn", "slug": "auburn", "county": "Lee County", "lat": 32.6099, "lng": -85.4808},
            {"name": "Decatur", "slug": "decatur", "county": "Morgan County", "lat": 34.6059, "lng": -86.9833},
            {"name": "Madison", "slug": "madison", "county": "Madison County", "lat": 34.6993, "lng": -86.7483},
            {"name": "Florence", "slug": "florence", "county": "Lauderdale County", "lat": 34.7998, "lng": -87.6773},
            {"name": "Gadsden", "slug": "gadsden", "county": "Etowah County", "lat": 34.0143, "lng": -86.0066},
            {"name": "Vestavia Hills", "slug": "vestavia-hills", "county": "Jefferson County", "lat": 33.4487, "lng": -86.7872},
            {"name": "Prattville", "slug": "prattville", "county": "Autauga County", "lat": 32.464, "lng": -86.4597},
            {"name": "Phenix City", "slug": "phenix-city", "county": "Russell County", "lat": 32.4709, "lng": -85.0008},
        ]
    },
    "alaska": {
        "name": "Alaska",
        "abbr": "AK",
        "cities": [
            {"name": "Anchorage", "slug": "anchorage", "county": "Anchorage Municipality", "lat": 61.2181, "lng": -149.9003},
            {"name": "Fairbanks", "slug": "fairbanks", "county": "Fairbanks North Star Borough", "lat": 64.8378, "lng": -147.7164},
            {"name": "Juneau", "slug": "juneau", "county": "Juneau Borough", "lat": 58.3019, "lng": -134.4197},
            {"name": "Sitka", "slug": "sitka", "county": "Sitka Borough", "lat": 57.0531, "lng": -135.33},
            {"name": "Ketchikan", "slug": "ketchikan", "county": "Ketchikan Gateway Borough", "lat": 55.3422, "lng": -131.6461},
            {"name": "Wasilla", "slug": "wasilla", "county": "Matanuska-Susitna Borough", "lat": 61.5814, "lng": -149.4394},
            {"name": "Kenai", "slug": "kenai", "county": "Kenai Peninsula Borough", "lat": 60.5544, "lng": -151.2583},
            {"name": "Kodiak", "slug": "kodiak", "county": "Kodiak Island Borough", "lat": 57.79, "lng": -152.4072},
            {"name": "Bethel", "slug": "bethel", "county": "Bethel Census Area", "lat": 60.7922, "lng": -161.7558},
            {"name": "Palmer", "slug": "palmer", "county": "Matanuska-Susitna Borough", "lat": 61.5997, "lng": -149.1156},
            {"name": "Homer", "slug": "homer", "county": "Kenai Peninsula Borough", "lat": 59.6425, "lng": -151.5483},
            {"name": "Soldotna", "slug": "soldotna", "county": "Kenai Peninsula Borough", "lat": 60.4903, "lng": -151.0583},
            {"name": "Knik-Fairview", "slug": "knik-fairview", "county": "Matanuska-Susitna Borough", "lat": 61.5158, "lng": -149.5997},
            {"name": "College", "slug": "college", "county": "Fairbanks North Star Borough", "lat": 64.8567, "lng": -147.8028},
            {"name": "Badger", "slug": "badger", "county": "Fairbanks North Star Borough", "lat": 64.8, "lng": -147.5333},
        ]
    },
    "arizona": {
        "name": "Arizona",
        "abbr": "AZ",
        "cities": [
            {"name": "Phoenix", "slug": "phoenix", "county": "Maricopa County", "lat": 33.4484, "lng": -112.074},
            {"name": "Tucson", "slug": "tucson", "county": "Pima County", "lat": 32.2226, "lng": -110.9747},
            {"name": "Mesa", "slug": "mesa", "county": "Maricopa County", "lat": 33.4152, "lng": -111.8315},
            {"name": "Chandler", "slug": "chandler", "county": "Maricopa County", "lat": 33.3062, "lng": -111.8413},
            {"name": "Scottsdale", "slug": "scottsdale", "county": "Maricopa County", "lat": 33.4942, "lng": -111.9261},
            {"name": "Glendale", "slug": "glendale", "county": "Maricopa County", "lat": 33.5387, "lng": -112.186},
            {"name": "Gilbert", "slug": "gilbert", "county": "Maricopa County", "lat": 33.3528, "lng": -111.789},
            {"name": "Tempe", "slug": "tempe", "county": "Maricopa County", "lat": 33.4255, "lng": -111.94},
            {"name": "Peoria", "slug": "peoria", "county": "Maricopa County", "lat": 33.5806, "lng": -112.2374},
            {"name": "Surprise", "slug": "surprise", "county": "Maricopa County", "lat": 33.6292, "lng": -112.368},
            {"name": "Yuma", "slug": "yuma", "county": "Yuma County", "lat": 32.6927, "lng": -114.6277},
            {"name": "Avondale", "slug": "avondale", "county": "Maricopa County", "lat": 33.4356, "lng": -112.3496},
            {"name": "Flagstaff", "slug": "flagstaff", "county": "Coconino County", "lat": 35.1983, "lng": -111.6513},
            {"name": "Goodyear", "slug": "goodyear", "county": "Maricopa County", "lat": 33.4353, "lng": -112.3576},
            {"name": "Lake Havasu City", "slug": "lake-havasu-city", "county": "Mohave County", "lat": 34.4839, "lng": -114.3227},
        ]
    },
}

# Statistics:
# States: 3
# Total Cities: 45
# Services per City: 4
# Total Landing Pages: 180
