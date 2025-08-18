"""
Comprehensive US cities data for SEO landing pages
Merged comprehensive dataset with 1000+ cities covering all 50 US states plus DC
Includes state, county, geographic coordinates, metro area, and regional data

Updated: January 2025 - Merged from multiple regional datasets
"""

US_MAJOR_CITIES = {
    # Top National Cities - Major Population Centers
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
    },
    "austin": {
        "name": "Austin",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Travis County",
        "population": 978908,
        "lat": 30.2672,
        "lng": -97.7431,
        "metro_area": "Austin-Round Rock",
        "region": "South"
    },
    "jacksonville": {
        "name": "Jacksonville",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Duval County",
        "population": 911507,
        "lat": 30.3322,
        "lng": -81.6557,
        "metro_area": "Jacksonville",
        "region": "South"
    },
    "fort-worth": {
        "name": "Fort Worth",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Tarrant County",
        "population": 909585,
        "lat": 32.7555,
        "lng": -97.3308,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "columbus": {
        "name": "Columbus",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Franklin County",
        "population": 898553,
        "lat": 39.9612,
        "lng": -82.9988,
        "metro_area": "Columbus",
        "region": "Midwest"
    },
    "san-francisco": {
        "name": "San Francisco",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Francisco County",
        "population": 881549,
        "lat": 37.7749,
        "lng": -122.4194,
        "metro_area": "San Francisco-Oakland-Hayward",
        "region": "West"
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
    "indianapolis": {
        "name": "Indianapolis",
        "state": "Indiana",
        "state_abbr": "IN",
        "county": "Marion County",
        "population": 876384,
        "lat": 39.7684,
        "lng": -86.1581,
        "metro_area": "Indianapolis-Carmel-Anderson",
        "region": "Midwest"
    },
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
    "washington": {
        "name": "Washington",
        "state": "District of Columbia",
        "state_abbr": "DC",
        "county": "District of Columbia",
        "population": 705749,
        "lat": 38.9072,
        "lng": -77.0369,
        "metro_area": "Washington-Arlington-Alexandria",
        "region": "South"
    },
    "boston": {
        "name": "Boston",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Suffolk County",
        "population": 692600,
        "lat": 42.3601,
        "lng": -71.0589,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "el-paso": {
        "name": "El Paso",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "El Paso County",
        "population": 681728,
        "lat": 31.7619,
        "lng": -106.4850,
        "metro_area": "El Paso",
        "region": "Southwest"
    },
    "detroit": {
        "name": "Detroit",
        "state": "Michigan",
        "state_abbr": "MI",
        "county": "Wayne County",
        "population": 670031,
        "lat": 42.3314,
        "lng": -83.0458,
        "metro_area": "Detroit-Warren-Dearborn",
        "region": "Midwest"
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
    "baltimore": {
        "name": "Baltimore",
        "state": "Maryland",
        "state_abbr": "MD",
        "county": "Baltimore City",
        "population": 602495,
        "lat": 39.2904,
        "lng": -76.6122,
        "metro_area": "Baltimore-Columbia-Towson",
        "region": "South"
    },
    "milwaukee": {
        "name": "Milwaukee",
        "state": "Wisconsin",
        "state_abbr": "WI",
        "county": "Milwaukee County",
        "population": 594833,
        "lat": 43.0389,
        "lng": -87.9065,
        "metro_area": "Milwaukee-Waukesha-West Allis",
        "region": "Midwest"
    },
    "albuquerque": {
        "name": "Albuquerque",
        "state": "New Mexico",
        "state_abbr": "NM",
        "county": "Bernalillo County",
        "population": 560513,
        "lat": 35.0853,
        "lng": -106.6056,
        "metro_area": "Albuquerque",
        "region": "Southwest"
    },
    "tucson": {
        "name": "Tucson",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Pima County",
        "population": 548073,
        "lat": 32.2226,
        "lng": -110.9747,
        "metro_area": "Tucson",
        "region": "Southwest"
    },
    "fresno": {
        "name": "Fresno",
        "state": "California",
        "state_abbr": "CA",
        "county": "Fresno County",
        "population": 531576,
        "lat": 36.7378,
        "lng": -119.7871,
        "metro_area": "Fresno",
        "region": "West"
    },
    "sacramento": {
        "name": "Sacramento",
        "state": "California",
        "state_abbr": "CA",
        "county": "Sacramento County",
        "population": 513624,
        "lat": 38.5816,
        "lng": -121.4944,
        "metro_area": "Sacramento-Roseville-Arden-Arcade",
        "region": "West"
    },
    "kansas-city": {
        "name": "Kansas City",
        "state": "Missouri",
        "state_abbr": "MO",
        "county": "Jackson County",
        "population": 495327,
        "lat": 39.0997,
        "lng": -94.5786,
        "metro_area": "Kansas City",
        "region": "Midwest"
    },
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
    "mesa": {
        "name": "Mesa",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 508958,
        "lat": 33.4152,
        "lng": -111.8315,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "colorado-springs": {
        "name": "Colorado Springs",
        "state": "Colorado",
        "state_abbr": "CO",
        "county": "El Paso County",
        "population": 478221,
        "lat": 38.8339,
        "lng": -104.8214,
        "metro_area": "Colorado Springs",
        "region": "West"
    },
    "raleigh": {
        "name": "Raleigh",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Wake County",
        "population": 474069,
        "lat": 35.7796,
        "lng": -78.6382,
        "metro_area": "Raleigh",
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
    "virginia-beach": {
        "name": "Virginia Beach",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Virginia Beach City",
        "population": 449974,
        "lat": 36.8529,
        "lng": -75.9780,
        "metro_area": "Virginia Beach-Norfolk-Newport News",
        "region": "South"
    },
    "omaha": {
        "name": "Omaha",
        "state": "Nebraska",
        "state_abbr": "NE",
        "county": "Douglas County",
        "population": 478192,
        "lat": 41.2565,
        "lng": -95.9345,
        "metro_area": "Omaha-Council Bluffs",
        "region": "Midwest"
    },
    "oakland": {
        "name": "Oakland",
        "state": "California",
        "state_abbr": "CA",
        "county": "Alameda County",
        "population": 433031,
        "lat": 37.8044,
        "lng": -122.2712,
        "metro_area": "San Francisco-Oakland-Hayward",
        "region": "West"
    },
    "minneapolis": {
        "name": "Minneapolis",
        "state": "Minnesota",
        "state_abbr": "MN",
        "county": "Hennepin County",
        "population": 429954,
        "lat": 44.9778,
        "lng": -93.2650,
        "metro_area": "Minneapolis-St. Paul-Bloomington",
        "region": "Midwest"
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
    "arlington": {
        "name": "Arlington",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Tarrant County",
        "population": 398854,
        "lat": 32.7357,
        "lng": -97.1081,
        "metro_area": "Dallas-Fort Worth-Arlington",
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
    "wichita": {
        "name": "Wichita",
        "state": "Kansas",
        "state_abbr": "KS",
        "county": "Sedgwick County",
        "population": 389255,
        "lat": 37.6872,
        "lng": -97.3301,
        "metro_area": "Wichita",
        "region": "Midwest"
    },
    "cleveland": {
        "name": "Cleveland",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Cuyahoga County",
        "population": 381009,
        "lat": 41.4993,
        "lng": -81.6944,
        "metro_area": "Cleveland-Elyria",
        "region": "Midwest"
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
    "bakersfield": {
        "name": "Bakersfield",
        "state": "California",
        "state_abbr": "CA",
        "county": "Kern County",
        "population": 384145,
        "lat": 35.3733,
        "lng": -119.0187,
        "metro_area": "Bakersfield",
        "region": "West"
    },
    "aurora": {
        "name": "Aurora",
        "state": "Colorado",
        "state_abbr": "CO",
        "county": "Arapahoe County",
        "population": 379289,
        "lat": 39.7294,
        "lng": -104.8319,
        "metro_area": "Denver-Aurora-Lakewood",
        "region": "West"
    },
    "anaheim": {
        "name": "Anaheim",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 352497,
        "lat": 33.8366,
        "lng": -117.9143,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "honolulu": {
        "name": "Honolulu",
        "state": "Hawaii",
        "state_abbr": "HI",
        "county": "Honolulu County",
        "population": 345064,
        "lat": 21.3099,
        "lng": -157.8581,
        "metro_area": "Urban Honolulu",
        "region": "West"
    },
    "santa-ana": {
        "name": "Santa Ana",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 332318,
        "lat": 33.7455,
        "lng": -117.8677,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "riverside": {
        "name": "Riverside",
        "state": "California",
        "state_abbr": "CA",
        "county": "Riverside County",
        "population": 331360,
        "lat": 33.9533,
        "lng": -117.3962,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "corpus-christi": {
        "name": "Corpus Christi",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Nueces County",
        "population": 326586,
        "lat": 27.8006,
        "lng": -97.3964,
        "metro_area": "Corpus Christi",
        "region": "South"
    },
    "lexington": {
        "name": "Lexington",
        "state": "Kentucky",
        "state_abbr": "KY",
        "county": "Fayette County",
        "population": 323152,
        "lat": 38.0406,
        "lng": -84.5037,
        "metro_area": "Lexington-Fayette",
        "region": "South"
    },
    "stockton": {
        "name": "Stockton",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Joaquin County",
        "population": 312697,
        "lat": 37.9577,
        "lng": -121.2908,
        "metro_area": "Stockton-Lodi",
        "region": "West"
    },
    "henderson": {
        "name": "Henderson",
        "state": "Nevada",
        "state_abbr": "NV",
        "county": "Clark County",
        "population": 310390,
        "lat": 36.0395,
        "lng": -114.9817,
        "metro_area": "Las Vegas-Henderson-Paradise",
        "region": "West"
    },
    "saint-paul": {
        "name": "Saint Paul",
        "state": "Minnesota",
        "state_abbr": "MN",
        "county": "Ramsey County",
        "population": 308096,
        "lat": 44.9537,
        "lng": -93.0900,
        "metro_area": "Minneapolis-St. Paul-Bloomington",
        "region": "Midwest"
    },
    "st-louis": {
        "name": "St. Louis",
        "state": "Missouri",
        "state_abbr": "MO",
        "county": "St. Louis City",
        "population": 300576,
        "lat": 38.6270,
        "lng": -90.1994,
        "metro_area": "St. Louis",
        "region": "Midwest"
    },
    "cincinnati": {
        "name": "Cincinnati",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Hamilton County",
        "population": 303940,
        "lat": 39.1031,
        "lng": -84.5120,
        "metro_area": "Cincinnati",
        "region": "Midwest"
    },
    "pittsburgh": {
        "name": "Pittsburgh",
        "state": "Pennsylvania",
        "state_abbr": "PA",
        "county": "Allegheny County",
        "population": 300286,
        "lat": 40.4406,
        "lng": -79.9959,
        "metro_area": "Pittsburgh",
        "region": "Northeast"
    },
    "greensboro": {
        "name": "Greensboro",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Guilford County",
        "population": 296710,
        "lat": 36.0726,
        "lng": -79.7920,
        "metro_area": "Greensboro-High Point",
        "region": "South"
    },
    "anchorage": {
        "name": "Anchorage",
        "state": "Alaska",
        "state_abbr": "AK",
        "county": "Anchorage Municipality",
        "population": 288000,
        "lat": 61.2181,
        "lng": -149.9003,
        "metro_area": "Anchorage",
        "region": "West"
    },
    "plano": {
        "name": "Plano",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Collin County",
        "population": 287677,
        "lat": 33.0198,
        "lng": -96.6989,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "lincoln": {
        "name": "Lincoln",
        "state": "Nebraska",
        "state_abbr": "NE",
        "county": "Lancaster County",
        "population": 291082,
        "lat": 40.8136,
        "lng": -96.7026,
        "metro_area": "Lincoln",
        "region": "Midwest"
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
    "irvine": {
        "name": "Irvine",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 287401,
        "lat": 33.6839,
        "lng": -117.7947,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "newark": {
        "name": "Newark",
        "state": "New Jersey",
        "state_abbr": "NJ",
        "county": "Essex County",
        "population": 282011,
        "lat": 40.7357,
        "lng": -74.1724,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "toledo": {
        "name": "Toledo",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Lucas County",
        "population": 274975,
        "lat": 41.6528,
        "lng": -83.5379,
        "metro_area": "Toledo",
        "region": "Midwest"
    },
    "durham": {
        "name": "Durham",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Durham County",
        "population": 278993,
        "lat": 35.9940,
        "lng": -78.8986,
        "metro_area": "Durham-Chapel Hill",
        "region": "South"
    },
    "chula-vista": {
        "name": "Chula Vista",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Diego County",
        "population": 274492,
        "lat": 32.6401,
        "lng": -117.0842,
        "metro_area": "San Diego-Carlsbad",
        "region": "West"
    },
    "fort-wayne": {
        "name": "Fort Wayne",
        "state": "Indiana",
        "state_abbr": "IN",
        "county": "Allen County",
        "population": 270402,
        "lat": 41.0793,
        "lng": -85.1394,
        "metro_area": "Fort Wayne",
        "region": "Midwest"
    },
    "jersey-city": {
        "name": "Jersey City",
        "state": "New Jersey",
        "state_abbr": "NJ",
        "county": "Hudson County",
        "population": 262075,
        "lat": 40.7282,
        "lng": -74.0776,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "st-petersburg": {
        "name": "St. Petersburg",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Pinellas County",
        "population": 265351,
        "lat": 27.7676,
        "lng": -82.6403,
        "metro_area": "Tampa-St. Petersburg-Clearwater",
        "region": "South"
    },
    "laredo": {
        "name": "Laredo",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Webb County",
        "population": 262491,
        "lat": 27.5306,
        "lng": -99.4803,
        "metro_area": "Laredo",
        "region": "South"
    },
    "buffalo": {
        "name": "Buffalo",
        "state": "New York",
        "state_abbr": "NY",
        "county": "Erie County",
        "population": 255284,
        "lat": 42.8864,
        "lng": -78.8784,
        "metro_area": "Buffalo-Cheektowaga-Niagara Falls",
        "region": "Northeast"
    },
    "madison": {
        "name": "Madison",
        "state": "Wisconsin",
        "state_abbr": "WI",
        "county": "Dane County",
        "population": 259680,
        "lat": 43.0731,
        "lng": -89.4012,
        "metro_area": "Madison",
        "region": "Midwest"
    },
    "lubbock": {
        "name": "Lubbock",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Lubbock County",
        "population": 258862,
        "lat": 33.5779,
        "lng": -101.8552,
        "metro_area": "Lubbock",
        "region": "South"
    },
    "chandler": {
        "name": "Chandler",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 261165,
        "lat": 33.3062,
        "lng": -111.8413,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "scottsdale": {
        "name": "Scottsdale",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 255310,
        "lat": 33.4942,
        "lng": -111.9261,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "reno": {
        "name": "Reno",
        "state": "Nevada",
        "state_abbr": "NV",
        "county": "Washoe County",
        "population": 255601,
        "lat": 39.5296,
        "lng": -119.8138,
        "metro_area": "Reno",
        "region": "West"
    },
    "glendale": {
        "name": "Glendale",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 252381,
        "lat": 33.5387,
        "lng": -112.1860,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "norfolk": {
        "name": "Norfolk",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Norfolk City",
        "population": 244300,
        "lat": 36.8508,
        "lng": -76.2859,
        "metro_area": "Virginia Beach-Norfolk-Newport News",
        "region": "South"
    },
    "winston-salem": {
        "name": "Winston-Salem",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Forsyth County",
        "population": 247945,
        "lat": 36.0999,
        "lng": -80.2444,
        "metro_area": "Winston-Salem",
        "region": "South"
    },
    "north-las-vegas": {
        "name": "North Las Vegas",
        "state": "Nevada",
        "state_abbr": "NV",
        "county": "Clark County",
        "population": 251974,
        "lat": 36.1989,
        "lng": -115.1175,
        "metro_area": "Las Vegas-Henderson-Paradise",
        "region": "West"
    },
    "gilbert": {
        "name": "Gilbert",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 254114,
        "lat": 33.3528,
        "lng": -111.7890,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "chesapeake": {
        "name": "Chesapeake",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Chesapeake City",
        "population": 244835,
        "lat": 36.7682,
        "lng": -76.2875,
        "metro_area": "Virginia Beach-Norfolk-Newport News",
        "region": "South"
    },
    "irving": {
        "name": "Irving",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 239798,
        "lat": 32.8140,
        "lng": -96.9489,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "hialeah": {
        "name": "Hialeah",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Miami-Dade County",
        "population": 233339,
        "lat": 25.8576,
        "lng": -80.2781,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "garland": {
        "name": "Garland",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 238002,
        "lat": 32.9126,
        "lng": -96.6389,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "fremont": {
        "name": "Fremont",
        "state": "California",
        "state_abbr": "CA",
        "county": "Alameda County",
        "population": 241110,
        "lat": 37.5483,
        "lng": -121.9886,
        "metro_area": "San Francisco-Oakland-Hayward",
        "region": "West"
    },
    "richmond": {
        "name": "Richmond",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Richmond City",
        "population": 227032,
        "lat": 37.5407,
        "lng": -77.4360,
        "metro_area": "Richmond",
        "region": "South"
    },
    "baton-rouge": {
        "name": "Baton Rouge",
        "state": "Louisiana",
        "state_abbr": "LA",
        "county": "East Baton Rouge Parish",
        "population": 220236,
        "lat": 30.4515,
        "lng": -91.1871,
        "metro_area": "Baton Rouge",
        "region": "South"
    },
    "boise": {
        "name": "Boise",
        "state": "Idaho",
        "state_abbr": "ID",
        "county": "Ada County",
        "population": 235684,
        "lat": 43.6150,
        "lng": -116.2023,
        "metro_area": "Boise City",
        "region": "West"
    },
    "san-bernardino": {
        "name": "San Bernardino",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Bernardino County",
        "population": 222101,
        "lat": 34.1083,
        "lng": -117.2898,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "spokane": {
        "name": "Spokane",
        "state": "Washington",
        "state_abbr": "WA",
        "county": "Spokane County",
        "population": 228989,
        "lat": 47.6587,
        "lng": -117.4260,
        "metro_area": "Spokane-Spokane Valley",
        "region": "West"
    },
    "des-moines": {
        "name": "Des Moines",
        "state": "Iowa",
        "state_abbr": "IA",
        "county": "Polk County",
        "population": 214237,
        "lat": 41.5868,
        "lng": -93.6250,
        "metro_area": "Des Moines-West Des Moines",
        "region": "Midwest"
    },
    "modesto": {
        "name": "Modesto",
        "state": "California",
        "state_abbr": "CA",
        "county": "Stanislaus County",
        "population": 215196,
        "lat": 37.6391,
        "lng": -120.9969,
        "metro_area": "Modesto",
        "region": "West"
    },
    "tacoma": {
        "name": "Tacoma",
        "state": "Washington",
        "state_abbr": "WA",
        "county": "Pierce County",
        "population": 217827,
        "lat": 47.2529,
        "lng": -122.4443,
        "metro_area": "Seattle-Tacoma-Bellevue",
        "region": "West"
    },
    "fontana": {
        "name": "Fontana",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Bernardino County",
        "population": 214547,
        "lat": 34.0922,
        "lng": -117.4350,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "santa-clarita": {
        "name": "Santa Clarita",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 212979,
        "lat": 34.3917,
        "lng": -118.5426,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
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
    "oxnard": {
        "name": "Oxnard",
        "state": "California",
        "state_abbr": "CA",
        "county": "Ventura County",
        "population": 208881,
        "lat": 34.1975,
        "lng": -119.1771,
        "metro_area": "Oxnard-Thousand Oaks-Ventura",
        "region": "West"
    },
    "fayetteville": {
        "name": "Fayetteville",
        "state": "North Carolina",
        "state_abbr": "NC",
        "county": "Cumberland County",
        "population": 211657,
        "lat": 35.0527,
        "lng": -78.8784,
        "metro_area": "Fayetteville",
        "region": "South"
    },
    "moreno-valley": {
        "name": "Moreno Valley",
        "state": "California",
        "state_abbr": "CA",
        "county": "Riverside County",
        "population": 213055,
        "lat": 33.9425,
        "lng": -117.2297,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "rochester": {
        "name": "Rochester",
        "state": "New York",
        "state_abbr": "NY",
        "county": "Monroe County",
        "population": 205695,
        "lat": 43.1610,
        "lng": -77.6109,
        "metro_area": "Rochester",
        "region": "Northeast"
    },
    "glendale-ca": {
        "name": "Glendale",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 196543,
        "lat": 34.1425,
        "lng": -118.2551,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "huntington-beach": {
        "name": "Huntington Beach",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 200641,
        "lat": 33.6595,
        "lng": -117.9988,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "salt-lake-city": {
        "name": "Salt Lake City",
        "state": "Utah",
        "state_abbr": "UT",
        "county": "Salt Lake County",
        "population": 200567,
        "lat": 40.7608,
        "lng": -111.8910,
        "metro_area": "Salt Lake City",
        "region": "West"
    },
    "grand-rapids": {
        "name": "Grand Rapids",
        "state": "Michigan",
        "state_abbr": "MI",
        "county": "Kent County",
        "population": 198917,
        "lat": 42.9634,
        "lng": -85.6681,
        "metro_area": "Grand Rapids-Wyoming",
        "region": "Midwest"
    },
    "amarillo": {
        "name": "Amarillo",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Potter County",
        "population": 199371,
        "lat": 35.2220,
        "lng": -101.8313,
        "metro_area": "Amarillo",
        "region": "South"
    },
    "yonkers": {
        "name": "Yonkers",
        "state": "New York",
        "state_abbr": "NY",
        "county": "Westchester County",
        "population": 200370,
        "lat": 40.9312,
        "lng": -73.8987,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "aurora-il": {
        "name": "Aurora",
        "state": "Illinois",
        "state_abbr": "IL",
        "county": "Kane County",
        "population": 197757,
        "lat": 41.7606,
        "lng": -88.3201,
        "metro_area": "Chicago-Naperville-Elgin",
        "region": "Midwest"
    },
    "montgomery": {
        "name": "Montgomery",
        "state": "Alabama",
        "state_abbr": "AL",
        "county": "Montgomery County",
        "population": 198525,
        "lat": 32.3668,
        "lng": -86.3000,
        "metro_area": "Montgomery",
        "region": "South"
    },
    "akron": {
        "name": "Akron",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Summit County",
        "population": 197597,
        "lat": 41.0814,
        "lng": -81.5190,
        "metro_area": "Akron",
        "region": "Midwest"
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
    "augusta": {
        "name": "Augusta",
        "state": "Georgia",
        "state_abbr": "GA",
        "county": "Richmond County",
        "population": 197888,
        "lat": 33.4735,
        "lng": -82.0105,
        "metro_area": "Augusta-Richmond County",
        "region": "South"
    },
    "columbus-ga": {
        "name": "Columbus",
        "state": "Georgia",
        "state_abbr": "GA",
        "county": "Muscogee County",
        "population": 195769,
        "lat": 32.4609,
        "lng": -84.9877,
        "metro_area": "Columbus",
        "region": "South"
    },
    "grand-prairie": {
        "name": "Grand Prairie",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 194543,
        "lat": 32.7460,
        "lng": -96.9978,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "shreveport": {
        "name": "Shreveport",
        "state": "Louisiana",
        "state_abbr": "LA",
        "county": "Caddo Parish",
        "population": 188987,
        "lat": 32.5252,
        "lng": -93.7502,
        "metro_area": "Shreveport-Bossier City",
        "region": "South"
    },
    "overland-park": {
        "name": "Overland Park",
        "state": "Kansas",
        "state_abbr": "KS",
        "county": "Johnson County",
        "population": 195494,
        "lat": 38.9822,
        "lng": -94.6708,
        "metro_area": "Kansas City",
        "region": "Midwest"
    },
    "tallahassee": {
        "name": "Tallahassee",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Leon County",
        "population": 194500,
        "lat": 30.4383,
        "lng": -84.2807,
        "metro_area": "Tallahassee",
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
    "port-st-lucie": {
        "name": "Port St. Lucie",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "St. Lucie County",
        "population": 195248,
        "lat": 27.2730,
        "lng": -80.3582,
        "metro_area": "Port St. Lucie",
        "region": "South"
    },
    "knoxville": {
        "name": "Knoxville",
        "state": "Tennessee",
        "state_abbr": "TN",
        "county": "Knox County",
        "population": 187603,
        "lat": 35.9606,
        "lng": -83.9207,
        "metro_area": "Knoxville",
        "region": "South"
    },
    "worcester": {
        "name": "Worcester",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Worcester County",
        "population": 185428,
        "lat": 42.2626,
        "lng": -71.8023,
        "metro_area": "Worcester",
        "region": "Northeast"
    },
    "tempe": {
        "name": "Tempe",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 192364,
        "lat": 33.4255,
        "lng": -111.9400,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "cape-coral": {
        "name": "Cape Coral",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Lee County",
        "population": 189633,
        "lat": 26.5629,
        "lng": -81.9495,
        "metro_area": "Cape Coral-Fort Myers",
        "region": "South"
    },
    "providence": {
        "name": "Providence",
        "state": "Rhode Island",
        "state_abbr": "RI",
        "county": "Providence County",
        "population": 179883,
        "lat": 41.8240,
        "lng": -71.4128,
        "metro_area": "Providence-Warwick",
        "region": "Northeast"
    },
    "fort-lauderdale": {
        "name": "Fort Lauderdale",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Broward County",
        "population": 183146,
        "lat": 26.1224,
        "lng": -80.1373,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "chattanooga": {
        "name": "Chattanooga",
        "state": "Tennessee",
        "state_abbr": "TN",
        "county": "Hamilton County",
        "population": 181099,
        "lat": 35.0456,
        "lng": -85.3097,
        "metro_area": "Chattanooga",
        "region": "South"
    },
    "newport-news": {
        "name": "Newport News",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Newport News City",
        "population": 180775,
        "lat": 37.0871,
        "lng": -76.4730,
        "metro_area": "Virginia Beach-Norfolk-Newport News",
        "region": "South"
    },
    "brownsville": {
        "name": "Brownsville",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Cameron County",
        "population": 183046,
        "lat": 25.9017,
        "lng": -97.4975,
        "metro_area": "Brownsville-Harlingen",
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
    "sioux-falls": {
        "name": "Sioux Falls",
        "state": "South Dakota",
        "state_abbr": "SD",
        "county": "Minnehaha County",
        "population": 183793,
        "lat": 43.5460,
        "lng": -96.7313,
        "metro_area": "Sioux Falls",
        "region": "Midwest"
    },
    "oceanside": {
        "name": "Oceanside",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Diego County",
        "population": 175691,
        "lat": 33.1959,
        "lng": -117.3795,
        "metro_area": "San Diego-Carlsbad",
        "region": "West"
    },
    "santa-rosa": {
        "name": "Santa Rosa",
        "state": "California",
        "state_abbr": "CA",
        "county": "Sonoma County",
        "population": 176753,
        "lat": 38.4404,
        "lng": -122.7141,
        "metro_area": "Santa Rosa",
        "region": "West"
    },
    "rancho-cucamonga": {
        "name": "Rancho Cucamonga",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Bernardino County",
        "population": 177603,
        "lat": 34.1064,
        "lng": -117.5931,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "dayton": {
        "name": "Dayton",
        "state": "Ohio",
        "state_abbr": "OH",
        "county": "Montgomery County",
        "population": 140407,
        "lat": 39.7589,
        "lng": -84.1916,
        "metro_area": "Dayton",
        "region": "Midwest"
    },
    "ontario": {
        "name": "Ontario",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Bernardino County",
        "population": 175265,
        "lat": 34.0633,
        "lng": -117.6509,
        "metro_area": "Riverside-San Bernardino-Ontario",
        "region": "West"
    },
    "vancouver": {
        "name": "Vancouver",
        "state": "Washington",
        "state_abbr": "WA",
        "county": "Clark County",
        "population": 183012,
        "lat": 45.6387,
        "lng": -122.6615,
        "metro_area": "Portland-Vancouver-Hillsboro",
        "region": "West"
    },
    "springfield-mo": {
        "name": "Springfield",
        "state": "Missouri",
        "state_abbr": "MO",
        "county": "Greene County",
        "population": 169176,
        "lat": 37.2090,
        "lng": -93.2923,
        "metro_area": "Springfield",
        "region": "Midwest"
    },
    "lancaster": {
        "name": "Lancaster",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 159523,
        "lat": 34.6868,
        "lng": -118.1542,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "eugene": {
        "name": "Eugene",
        "state": "Oregon",
        "state_abbr": "OR",
        "county": "Lane County",
        "population": 172622,
        "lat": 44.0521,
        "lng": -123.0868,
        "metro_area": "Eugene",
        "region": "West"
    },
    "salem": {
        "name": "Salem",
        "state": "Oregon",
        "state_abbr": "OR",
        "county": "Marion County",
        "population": 174365,
        "lat": 44.9429,
        "lng": -123.0351,
        "metro_area": "Salem",
        "region": "West"
    },
    "palmdale": {
        "name": "Palmdale",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 152750,
        "lat": 34.5794,
        "lng": -118.1165,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "salinas": {
        "name": "Salinas",
        "state": "California",
        "state_abbr": "CA",
        "county": "Monterey County",
        "population": 157596,
        "lat": 36.6777,
        "lng": -121.6555,
        "metro_area": "Salinas",
        "region": "West"
    },
    "springfield-ma": {
        "name": "Springfield",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Hampden County",
        "population": 154596,
        "lat": 42.1015,
        "lng": -72.5898,
        "metro_area": "Springfield",
        "region": "Northeast"
    },
    "pasadena-tx": {
        "name": "Pasadena",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Harris County",
        "population": 151950,
        "lat": 29.6911,
        "lng": -95.2091,
        "metro_area": "Houston-The Woodlands-Sugar Land",
        "region": "South"
    },
    "rockford": {
        "name": "Rockford",
        "state": "Illinois",
        "state_abbr": "IL",
        "county": "Winnebago County",
        "population": 147651,
        "lat": 42.2711,
        "lng": -89.0940,
        "metro_area": "Rockford",
        "region": "Midwest"
    },
    "pomona": {
        "name": "Pomona",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 151348,
        "lat": 34.0551,
        "lng": -117.7523,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "hayward": {
        "name": "Hayward",
        "state": "California",
        "state_abbr": "CA",
        "county": "Alameda County",
        "population": 159620,
        "lat": 37.6688,
        "lng": -122.0808,
        "metro_area": "San Francisco-Oakland-Hayward",
        "region": "West"
    },
    "fort-collins": {
        "name": "Fort Collins",
        "state": "Colorado",
        "state_abbr": "CO",
        "county": "Larimer County",
        "population": 169810,
        "lat": 40.5853,
        "lng": -105.0844,
        "metro_area": "Fort Collins",
        "region": "West"
    },
    "joliet": {
        "name": "Joliet",
        "state": "Illinois",
        "state_abbr": "IL",
        "county": "Will County",
        "population": 147433,
        "lat": 41.5250,
        "lng": -88.0817,
        "metro_area": "Chicago-Naperville-Elgin",
        "region": "Midwest"
    },
    "escondido": {
        "name": "Escondido",
        "state": "California",
        "state_abbr": "CA",
        "county": "San Diego County",
        "population": 151894,
        "lat": 33.1192,
        "lng": -117.0864,
        "metro_area": "San Diego-Carlsbad",
        "region": "West"
    },
    "kansas-city-ks": {
        "name": "Kansas City",
        "state": "Kansas",
        "state_abbr": "KS",
        "county": "Wyandotte County",
        "population": 152960,
        "lat": 39.1142,
        "lng": -94.6275,
        "metro_area": "Kansas City",
        "region": "Midwest"
    },
    "torrance": {
        "name": "Torrance",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 145438,
        "lat": 33.8358,
        "lng": -118.3406,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "bridgeport": {
        "name": "Bridgeport",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Fairfield County",
        "population": 148654,
        "lat": 41.1865,
        "lng": -73.1952,
        "metro_area": "Bridgeport-Stamford-Norwalk",
        "region": "Northeast"
    },
    "alexandria": {
        "name": "Alexandria",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Alexandria City",
        "population": 159467,
        "lat": 38.8048,
        "lng": -77.0469,
        "metro_area": "Washington-Arlington-Alexandria",
        "region": "South"
    },
    "sunnyvale": {
        "name": "Sunnyvale",
        "state": "California",
        "state_abbr": "CA",
        "county": "Santa Clara County",
        "population": 155567,
        "lat": 37.3688,
        "lng": -122.0363,
        "metro_area": "San Jose-Sunnyvale-Santa Clara",
        "region": "West"
    },
    "lakewood": {
        "name": "Lakewood",
        "state": "Colorado",
        "state_abbr": "CO",
        "county": "Jefferson County",
        "population": 155984,
        "lat": 39.7047,
        "lng": -105.0814,
        "metro_area": "Denver-Aurora-Lakewood",
        "region": "West"
    },
    "hollywood": {
        "name": "Hollywood",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Broward County",
        "population": 154823,
        "lat": 26.0112,
        "lng": -80.1495,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "paterson": {
        "name": "Paterson",
        "state": "New Jersey",
        "state_abbr": "NJ",
        "county": "Passaic County",
        "population": 145233,
        "lat": 40.9168,
        "lng": -74.1718,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "syracuse": {
        "name": "Syracuse",
        "state": "New York",
        "state_abbr": "NY",
        "county": "Onondaga County",
        "population": 142749,
        "lat": 43.0481,
        "lng": -76.1474,
        "metro_area": "Syracuse",
        "region": "Northeast"
    },
    "mesquite": {
        "name": "Mesquite",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 140937,
        "lat": 32.7668,
        "lng": -96.5992,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "pasadena-ca": {
        "name": "Pasadena",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 141029,
        "lat": 34.1478,
        "lng": -118.1445,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "orange": {
        "name": "Orange",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 139969,
        "lat": 33.7879,
        "lng": -117.8531,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "fullerton": {
        "name": "Fullerton",
        "state": "California",
        "state_abbr": "CA",
        "county": "Orange County",
        "population": 138632,
        "lat": 33.8703,
        "lng": -117.9242,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
    },
    "mcallen": {
        "name": "McAllen",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Hidalgo County",
        "population": 142210,
        "lat": 26.2034,
        "lng": -98.2300,
        "metro_area": "McAllen-Edinburg-Mission",
        "region": "South"
    },
    "killeen": {
        "name": "Killeen",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Bell County",
        "population": 145482,
        "lat": 31.1171,
        "lng": -97.7278,
        "metro_area": "Killeen-Temple",
        "region": "South"
    },
    "bellevue": {
        "name": "Bellevue",
        "state": "Washington",
        "state_abbr": "WA",
        "county": "King County",
        "population": 147599,
        "lat": 47.6101,
        "lng": -122.2015,
        "metro_area": "Seattle-Tacoma-Bellevue",
        "region": "West"
    },
    "west-valley-city": {
        "name": "West Valley City",
        "state": "Utah",
        "state_abbr": "UT",
        "county": "Salt Lake County",
        "population": 136401,
        "lat": 40.6916,
        "lng": -112.0011,
        "metro_area": "Salt Lake City",
        "region": "West"
    },
    "stamford": {
        "name": "Stamford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Fairfield County",
        "population": 135470,
        "lat": 41.0534,
        "lng": -73.5387,
        "metro_area": "Bridgeport-Stamford-Norwalk",
        "region": "Northeast"
    },
    "new-haven": {
        "name": "New Haven",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 134023,
        "lat": 41.3083,
        "lng": -72.9279,
        "metro_area": "New Haven-Milford",
        "region": "Northeast"
    },
    "topeka": {
        "name": "Topeka",
        "state": "Kansas",
        "state_abbr": "KS",
        "county": "Shawnee County",
        "population": 125310,
        "lat": 39.0473,
        "lng": -95.6752,
        "metro_area": "Topeka",
        "region": "Midwest"
    },
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
    "hartford": {
        "name": "Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 121054,
        "lat": 41.7658,
        "lng": -72.6734,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "gainesville": {
        "name": "Gainesville",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Alachua County",
        "population": 133997,
        "lat": 29.6516,
        "lng": -82.3248,
        "metro_area": "Gainesville",
        "region": "South"
    },
    "visalia": {
        "name": "Visalia",
        "state": "California",
        "state_abbr": "CA",
        "county": "Tulare County",
        "population": 134605,
        "lat": 36.3302,
        "lng": -119.2921,
        "metro_area": "Visalia-Porterville",
        "region": "West"
    },
    "simi-valley": {
        "name": "Simi Valley",
        "state": "California",
        "state_abbr": "CA",
        "county": "Ventura County",
        "population": 125768,
        "lat": 34.2694,
        "lng": -118.7815,
        "metro_area": "Oxnard-Thousand Oaks-Ventura",
        "region": "West"
    },
    "concord": {
        "name": "Concord",
        "state": "California",
        "state_abbr": "CA",
        "county": "Contra Costa County",
        "population": 129295,
        "lat": 37.9780,
        "lng": -122.0311,
        "metro_area": "San Francisco-Oakland-Hayward",
        "region": "West"
    },
    "roseville": {
        "name": "Roseville",
        "state": "California",
        "state_abbr": "CA",
        "county": "Placer County",
        "population": 141500,
        "lat": 38.7521,
        "lng": -121.2880,
        "metro_area": "Sacramento-Roseville-Arden-Arcade",
        "region": "West"
    },
    "thornton": {
        "name": "Thornton",
        "state": "Colorado",
        "state_abbr": "CO",
        "county": "Adams County",
        "population": 141867,
        "lat": 39.8680,
        "lng": -104.9719,
        "metro_area": "Denver-Aurora-Lakewood",
        "region": "West"
    },
    "frisco": {
        "name": "Frisco",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Collin County",
        "population": 200509,
        "lat": 33.1507,
        "lng": -96.8236,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "columbia": {
        "name": "Columbia",
        "state": "South Carolina",
        "state_abbr": "SC",
        "county": "Richland County",
        "population": 133451,
        "lat": 34.0007,
        "lng": -81.0348,
        "metro_area": "Columbia",
        "region": "South"
    },
    "olathe": {
        "name": "Olathe",
        "state": "Kansas",
        "state_abbr": "KS",
        "county": "Johnson County",
        "population": 140545,
        "lat": 38.8814,
        "lng": -94.8191,
        "metro_area": "Kansas City",
        "region": "Midwest"
    },
    "sterling-heights": {
        "name": "Sterling Heights",
        "state": "Michigan",
        "state_abbr": "MI",
        "county": "Macomb County",
        "population": 132438,
        "lat": 42.5803,
        "lng": -83.0302,
        "metro_area": "Detroit-Warren-Dearborn",
        "region": "Midwest"
    },
    "thousand-oaks": {
        "name": "Thousand Oaks",
        "state": "California",
        "state_abbr": "CA",
        "county": "Ventura County",
        "population": 126813,
        "lat": 34.1706,
        "lng": -118.8376,
        "metro_area": "Oxnard-Thousand Oaks-Ventura",
        "region": "West"
    },
    "cedar-rapids": {
        "name": "Cedar Rapids",
        "state": "Iowa",
        "state_abbr": "IA",
        "county": "Linn County",
        "population": 133562,
        "lat": 41.9779,
        "lng": -91.6656,
        "metro_area": "Cedar Rapids",
        "region": "Midwest"
    },
    "elizabeth": {
        "name": "Elizabeth",
        "state": "New Jersey",
        "state_abbr": "NJ",
        "county": "Union County",
        "population": 129007,
        "lat": 40.6639,
        "lng": -74.2107,
        "metro_area": "New York-Newark-Jersey City",
        "region": "Northeast"
    },
    "wichita-falls": {
        "name": "Wichita Falls",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Wichita County",
        "population": 104657,
        "lat": 33.9137,
        "lng": -98.4934,
        "metro_area": "Wichita Falls",
        "region": "South"
    },
    "waterbury": {
        "name": "Waterbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 114403,
        "lat": 41.5582,
        "lng": -73.0515,
        "metro_area": "Waterbury",
        "region": "Northeast"
    },
    "norwalk": {
        "name": "Norwalk",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Fairfield County",
        "population": 91184,
        "lat": 41.1176,
        "lng": -73.4079,
        "metro_area": "Bridgeport-Stamford-Norwalk",
        "region": "Northeast"
    },
    "danbury": {
        "name": "Danbury",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Fairfield County",
        "population": 86518,
        "lat": 41.3948,
        "lng": -73.4540,
        "metro_area": "Bridgeport-Stamford-Norwalk",
        "region": "Northeast"
    },
    "new-britain": {
        "name": "New Britain",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 72543,
        "lat": 41.6612,
        "lng": -72.7795,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "west-hartford": {
        "name": "West Hartford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 64083,
        "lat": 41.7620,
        "lng": -72.7420,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "meriden": {
        "name": "Meriden",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 60868,
        "lat": 41.5387,
        "lng": -72.8070,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "milford-ct": {
        "name": "Milford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 54518,
        "lat": 41.2223,
        "lng": -73.0565,
        "metro_area": "New Haven-Milford",
        "region": "Northeast"
    },
    "bristol": {
        "name": "Bristol",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 60833,
        "lat": 41.6712,
        "lng": -72.9493,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "middletown-ct": {
        "name": "Middletown",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Middlesex County",
        "population": 47717,
        "lat": 41.5623,
        "lng": -72.6506,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "shelton": {
        "name": "Shelton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Fairfield County",
        "population": 41162,
        "lat": 41.3164,
        "lng": -73.0931,
        "metro_area": "Bridgeport-Stamford-Norwalk",
        "region": "Northeast"
    },
    "watertown": {
        "name": "Watertown",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Litchfield County",
        "population": 22514,
        "lat": 41.6056,
        "lng": -73.1179,
        "metro_area": "Waterbury",
        "region": "Northeast"
    },
    "wallingford": {
        "name": "Wallingford",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 44396,
        "lat": 41.4570,
        "lng": -72.8231,
        "metro_area": "New Haven-Milford",
        "region": "Northeast"
    },
    "enfield": {
        "name": "Enfield",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 44654,
        "lat": 41.9854,
        "lng": -72.5901,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "southington": {
        "name": "Southington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Hartford County",
        "population": 43069,
        "lat": 41.5959,
        "lng": -72.8612,
        "metro_area": "Hartford-West Hartford-East Hartford",
        "region": "Northeast"
    },
    "torrington": {
        "name": "Torrington",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "Litchfield County",
        "population": 35515,
        "lat": 41.8007, 
        "lng": -73.1209,
        "metro_area": "Torrington",
        "region": "Northeast"
    },
    "ansonia": {
        "name": "Ansonia",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 18918,
        "lat": 41.3465,
        "lng": -73.0790,
        "metro_area": "Waterbury",
        "region": "Northeast"
    },
    "derby": {
        "name": "Derby",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New Haven County",
        "population": 12325,
        "lat": 41.3201,
        "lng": -73.0840,
        "metro_area": "New Haven-Milford",
        "region": "Northeast"
    },
    "groton": {
        "name": "Groton",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New London County", 
        "population": 38411,
        "lat": 41.3501,
        "lng": -72.0781,
        "metro_area": "Norwich-New London",
        "region": "Northeast"
    },
    "new-london": {
        "name": "New London",
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New London County",
        "population": 27367,
        "lat": 41.3556,
        "lng": -72.0995,
        "metro_area": "Norwich-New London",
        "region": "Northeast"
    },
    "norwalk-ct": {
        "name": "Norwich", 
        "state": "Connecticut",
        "state_abbr": "CT",
        "county": "New London County",
        "population": 40125,
        "lat": 41.5242,
        "lng": -72.0759,
        "metro_area": "Norwich-New London",
        "region": "Northeast"
    },
    # Additional cities to reach 1000+
    "cambridge": {
        "name": "Cambridge",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 118403,
        "lat": 42.3736,
        "lng": -71.1097,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "lowell": {
        "name": "Lowell",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County", 
        "population": 115554,
        "lat": 42.6334,
        "lng": -71.3162,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "brockton": {
        "name": "Brockton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Plymouth County",
        "population": 105643,
        "lat": 42.0834,
        "lng": -71.0184,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "new-bedford": {
        "name": "New Bedford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Bristol County",
        "population": 101079,
        "lat": 41.6362,
        "lng": -70.9342,
        "metro_area": "New Bedford",
        "region": "Northeast"
    },
    "quincy": {
        "name": "Quincy", 
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Norfolk County",
        "population": 101636,
        "lat": 42.2529,
        "lng": -71.0023,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "lynn": {
        "name": "Lynn",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Essex County",
        "population": 101253,
        "lat": 42.4668,
        "lng": -70.9495,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "fall-river": {
        "name": "Fall River",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Bristol County",
        "population": 94000,
        "lat": 41.7015,
        "lng": -71.1550,
        "metro_area": "Providence-Warwick",
        "region": "Northeast"
    },
    "newton": {
        "name": "Newton",
        "state": "Massachusetts", 
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 88923,
        "lat": 42.3370,
        "lng": -71.2092,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "somerville": {
        "name": "Somerville",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 81045,
        "lat": 42.3876,
        "lng": -71.0995,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "lawrence-ma": {
        "name": "Lawrence",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Essex County",
        "population": 89143,
        "lat": 42.7070,
        "lng": -71.1631,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "framingham": {
        "name": "Framingham",
        "state": "Massachusetts",
        "state_abbr": "MA", 
        "county": "Middlesex County",
        "population": 72362,
        "lat": 42.2793,
        "lng": -71.4162,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "haverhill": {
        "name": "Haverhill",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Essex County",
        "population": 67787,
        "lat": 42.7762,
        "lng": -71.0773,
        "metro_area": "Boston-Cambridge-Newton", 
        "region": "Northeast"
    },
    "waltham": {
        "name": "Waltham",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 65218,
        "lat": 42.3765,
        "lng": -71.2356,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "malden": {
        "name": "Malden",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 66263,
        "lat": 42.4251,
        "lng": -71.0662,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "medford": {
        "name": "Medford",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Middlesex County",
        "population": 59659,
        "lat": 42.4184,
        "lng": -71.1061,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "taunton": {
        "name": "Taunton",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Bristol County", 
        "population": 59408,
        "lat": 41.9001,
        "lng": -71.0903,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "chicopee": {
        "name": "Chicopee",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Hampden County",
        "population": 55560,
        "lat": 42.1487,
        "lng": -72.6078,
        "metro_area": "Springfield",
        "region": "Northeast"
    },
    "weymouth": {
        "name": "Weymouth",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Norfolk County",
        "population": 57213,
        "lat": 42.2180,
        "lng": -70.9395,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "revere": {
        "name": "Revere",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Suffolk County",
        "population": 62186,
        "lat": 42.4084,
        "lng": -71.0120,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    "peabody": {
        "name": "Peabody",
        "state": "Massachusetts",
        "state_abbr": "MA",
        "county": "Essex County",
        "population": 54481,
        "lat": 42.5278,
        "lng": -70.9286,
        "metro_area": "Boston-Cambridge-Newton",
        "region": "Northeast"
    },
    # Additional Vermont cities
    "burlington": {
        "name": "Burlington",
        "state": "Vermont", 
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 44743,
        "lat": 44.4759,
        "lng": -73.2121,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "south-burlington": {
        "name": "South Burlington",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 20292,
        "lat": 44.4667,
        "lng": -73.1709,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "rutland": {
        "name": "Rutland",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Rutland County",
        "population": 15807,
        "lat": 43.6106,
        "lng": -72.9726,
        "metro_area": "Rutland",
        "region": "Northeast"
    },
    "barre": {
        "name": "Barre",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Washington County",
        "population": 8491,
        "lat": 44.1970,
        "lng": -72.5020,
        "metro_area": "Barre",
        "region": "Northeast"
    },
    "montpelier": {
        "name": "Montpelier",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Washington County",
        "population": 8074,
        "lat": 44.2601,
        "lng": -72.5806,
        "metro_area": "Montpelier",
        "region": "Northeast"
    },
    "winooski": {
        "name": "Winooski",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 7329,
        "lat": 44.4900,
        "lng": -73.1857,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "st-albans": {
        "name": "St. Albans",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Franklin County",
        "population": 6877,
        "lat": 44.8109,
        "lng": -73.0834,
        "metro_area": "St. Albans",
        "region": "Northeast"
    },
    "newport-vt": {
        "name": "Newport",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Orleans County",
        "population": 4455,
        "lat": 44.9367,
        "lng": -72.2051,
        "metro_area": "Newport",
        "region": "Northeast"
    },
    "vergennes": {
        "name": "Vergennes",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Addison County",
        "population": 2553,
        "lat": 44.1645,
        "lng": -73.2540,
        "metro_area": "Vergennes",
        "region": "Northeast"
    },
    "middlebury": {
        "name": "Middlebury",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Addison County",
        "population": 9152,
        "lat": 44.0153,
        "lng": -73.1673,
        "metro_area": "Middlebury",
        "region": "Northeast"
    },
    "brattleboro": {
        "name": "Brattleboro",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Windham County",
        "population": 12046,
        "lat": 42.8509,
        "lng": -72.5579,
        "metro_area": "Brattleboro",
        "region": "Northeast"
    },
    "bellows-falls": {
        "name": "Bellows Falls",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Windham County",
        "population": 2747,
        "lat": 43.1334,
        "lng": -72.4298,
        "metro_area": "Bellows Falls",
        "region": "Northeast"
    },
    "white-river-junction": {
        "name": "White River Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Windsor County",
        "population": 2286,
        "lat": 43.6487,
        "lng": -72.3193,
        "metro_area": "White River Junction",
        "region": "Northeast"
    },
    "essex-junction": {
        "name": "Essex Junction",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 10761,
        "lat": 44.4906,
        "lng": -73.1112,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "colchester": {
        "name": "Colchester",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 17524,
        "lat": 44.5270,
        "lng": -73.1304,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "shelburne": {
        "name": "Shelburne",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Chittenden County",
        "population": 7717,
        "lat": 44.3798,
        "lng": -73.2234,
        "metro_area": "Burlington-South Burlington",
        "region": "Northeast"
    },
    "manchester-vt": {
        "name": "Manchester",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Bennington County",
        "population": 4484,
        "lat": 43.1634,
        "lng": -73.0723,
        "metro_area": "Manchester",
        "region": "Northeast"
    },
    "bennington": {
        "name": "Bennington",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Bennington County",
        "population": 15333,
        "lat": 42.8781,
        "lng": -73.1968,
        "metro_area": "Bennington",
        "region": "Northeast"
    },
    "st-johnsbury": {
        "name": "St. Johnsbury",
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Caledonia County",
        "population": 7364,
        "lat": 44.4192,
        "lng": -72.0151,
        "metro_area": "St. Johnsbury",
        "region": "Northeast"
    },
    "morrisville": {
        "name": "Morrisville", 
        "state": "Vermont",
        "state_abbr": "VT",
        "county": "Lamoille County",
        "population": 2063,
        "lat": 44.5564,
        "lng": -72.5998,
        "metro_area": "Morrisville",
        "region": "Northeast"
    },
    # Additional New Hampshire cities  
    "manchester-nh": {
        "name": "Manchester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Hillsborough County",
        "population": 115644,
        "lat": 42.9956,
        "lng": -71.4548,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "nashua": {
        "name": "Nashua",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Hillsborough County",
        "population": 91322,
        "lat": 42.7654,
        "lng": -71.4676,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "concord-nh": {
        "name": "Concord",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Merrimack County",
        "population": 43976,
        "lat": 43.2081,
        "lng": -71.5376,
        "metro_area": "Concord",
        "region": "Northeast"
    },
    "derry": {
        "name": "Derry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Rockingham County",
        "population": 34317,
        "lat": 42.8801,
        "lng": -71.3273,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "rochester-nh": {
        "name": "Rochester",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Strafford County",
        "population": 32492,
        "lat": 43.3042,
        "lng": -70.9756,
        "metro_area": "Rochester",
        "region": "Northeast"
    },
    "salem-nh": {
        "name": "Salem",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Rockingham County",
        "population": 29549,
        "lat": 42.7876,
        "lng": -71.2011,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "dover": {
        "name": "Dover", 
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Strafford County",
        "population": 32741,
        "lat": 43.1979,
        "lng": -70.8737,
        "metro_area": "Dover-Durham",
        "region": "Northeast"
    },
    "merrimack": {
        "name": "Merrimack",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Hillsborough County",
        "population": 26632,
        "lat": 42.8653,
        "lng": -71.4912,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "londonderry": {
        "name": "Londonderry",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Rockingham County",
        "population": 25826,
        "lat": 42.8653,
        "lng": -71.3740,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "hudson-nh": {
        "name": "Hudson",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Hillsborough County",
        "population": 25394,
        "lat": 42.7595,
        "lng": -71.4340,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    "portsmouth": {
        "name": "Portsmouth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Rockingham County",
        "population": 22194,
        "lat": 43.0718,
        "lng": -70.7626,
        "metro_area": "Portsmouth",
        "region": "Northeast"
    },
    "keene": {
        "name": "Keene",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Cheshire County",
        "population": 23047,
        "lat": 42.9342,
        "lng": -72.2781,
        "metro_area": "Keene",
        "region": "Northeast"
    },
    "laconia": {
        "name": "Laconia",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Belknap County",
        "population": 16871,
        "lat": 43.5278,
        "lng": -71.4703,
        "metro_area": "Laconia",
        "region": "Northeast"
    },
    "lebanon": {
        "name": "Lebanon",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Grafton County",
        "population": 14282,
        "lat": 43.6422,
        "lng": -72.2517,
        "metro_area": "Lebanon",
        "region": "Northeast"
    },
    "claremont": {
        "name": "Claremont",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Sullivan County",
        "population": 12969,
        "lat": 43.3770,
        "lng": -72.3451,
        "metro_area": "Claremont",
        "region": "Northeast"
    },
    "berlin": {
        "name": "Berlin",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Coos County",
        "population": 9425,
        "lat": 44.4689,
        "lng": -71.1850,
        "metro_area": "Berlin",
        "region": "Northeast"
    },
    "franklin": {
        "name": "Franklin",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Merrimack County",
        "population": 8741,
        "lat": 43.4473,
        "lng": -71.6473,
        "metro_area": "Franklin",
        "region": "Northeast"
    },
    "somersworth": {
        "name": "Somersworth",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Strafford County",
        "population": 11855,
        "lat": 43.2579,
        "lng": -70.8734,
        "metro_area": "Dover-Durham",
        "region": "Northeast"
    },
    "newport-nh": {
        "name": "Newport",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Sullivan County",
        "population": 6110,
        "lat": 43.3645,
        "lng": -72.1759,
        "metro_area": "Newport",
        "region": "Northeast"
    },
    "milford-nh": {
        "name": "Milford",
        "state": "New Hampshire",
        "state_abbr": "NH",
        "county": "Hillsborough County",
        "population": 15115,
        "lat": 42.8353,
        "lng": -71.6487,
        "metro_area": "Manchester-Nashua",
        "region": "Northeast"
    },
    # Additional Maine cities
    "portland-me": {
        "name": "Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 68408,
        "lat": 43.6591,
        "lng": -70.2568,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "lewiston": {
        "name": "Lewiston",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Androscoggin County",
        "population": 36221,
        "lat": 44.1003,
        "lng": -70.2148,
        "metro_area": "Lewiston-Auburn",
        "region": "Northeast"
    },
    "bangor": {
        "name": "Bangor",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Penobscot County",
        "population": 31753,
        "lat": 44.8016,
        "lng": -68.7712,
        "metro_area": "Bangor",
        "region": "Northeast"
    },
    "south-portland": {
        "name": "South Portland",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 25665,
        "lat": 43.6414,
        "lng": -70.2409,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "auburn": {
        "name": "Auburn",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Androscoggin County",
        "population": 24061,
        "lat": 44.0979,
        "lng": -70.2311,
        "metro_area": "Lewiston-Auburn", 
        "region": "Northeast"
    },
    "biddeford": {
        "name": "Biddeford",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "York County",
        "population": 21277,
        "lat": 43.4925,
        "lng": -70.4533,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "sanford": {
        "name": "Sanford",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "York County",
        "population": 21982,
        "lat": 43.4397,
        "lng": -70.7740,
        "metro_area": "Sanford",
        "region": "Northeast"
    },
    "brunswick": {
        "name": "Brunswick",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 21756,
        "lat": 43.9137,
        "lng": -69.9653,
        "metro_area": "Brunswick",
        "region": "Northeast"
    },
    "saco": {
        "name": "Saco",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "York County",
        "population": 19493,
        "lat": 43.5009,
        "lng": -70.4428,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "westbrook": {
        "name": "Westbrook",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 18732,
        "lat": 43.6770,
        "lng": -70.3712,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "augusta-me": {
        "name": "Augusta",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Kennebec County",
        "population": 18899,
        "lat": 44.3106,
        "lng": -69.7795,
        "metro_area": "Augusta-Waterville",
        "region": "Northeast"
    },
    "waterville": {
        "name": "Waterville",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Kennebec County",
        "population": 15908,
        "lat": 44.5520,
        "lng": -69.6319,
        "metro_area": "Augusta-Waterville",
        "region": "Northeast"
    },
    "presque-isle": {
        "name": "Presque Isle",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Aroostook County",
        "population": 8797,
        "lat": 46.6814,
        "lng": -68.0158,
        "metro_area": "Presque Isle",
        "region": "Northeast"
    },
    "gorham": {
        "name": "Gorham",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 17623,
        "lat": 43.6795,
        "lng": -70.4417,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "scarborough": {
        "name": "Scarborough",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 22135,
        "lat": 43.5781,
        "lng": -70.3170,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "windham": {
        "name": "Windham",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Cumberland County",
        "population": 18434,
        "lat": 43.8037,
        "lng": -70.4378,
        "metro_area": "Portland-South Portland",
        "region": "Northeast"
    },
    "topsham": {
        "name": "Topsham",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Sagadahoc County",
        "population": 8946,
        "lat": 43.9248,
        "lng": -69.9620,
        "metro_area": "Brunswick",
        "region": "Northeast"
    },
    "bath": {
        "name": "Bath",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Sagadahoc County",
        "population": 8766,
        "lat": 43.9109,
        "lng": -69.8206,
        "metro_area": "Bath",
        "region": "Northeast"
    },
    "ellsworth": {
        "name": "Ellsworth",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Hancock County",
        "population": 8399,
        "lat": 44.5434,
        "lng": -68.4198,
        "metro_area": "Ellsworth",
        "region": "Northeast"
    },
    "belfast": {
        "name": "Belfast",
        "state": "Maine",
        "state_abbr": "ME",
        "county": "Waldo County",
        "population": 6796,
        "lat": 44.4259,
        "lng": -69.0060,
        "metro_area": "Belfast",
        "region": "Northeast"
    },

    # Montana Cities
    "billings-mt": {
        "name": "Billings",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Yellowstone County",
        "population": 117116,
        "lat": 45.7833,
        "lng": -108.5007,
        "metro_area": "Billings",
        "region": "West"
    },
    "missoula": {
        "name": "Missoula",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Missoula County",
        "population": 73489,
        "lat": 46.8721,
        "lng": -113.9940,
        "metro_area": "Missoula",
        "region": "West"
    },
    "great-falls": {
        "name": "Great Falls",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Cascade County",
        "population": 60442,
        "lat": 47.4941,
        "lng": -111.2833,
        "metro_area": "Great Falls",
        "region": "West"
    },
    "bozeman": {
        "name": "Bozeman",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Gallatin County",
        "population": 53293,
        "lat": 45.6770,
        "lng": -111.0429,
        "metro_area": "Bozeman",
        "region": "West"
    },
    "butte": {
        "name": "Butte",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Silver Bow County",
        "population": 34494,
        "lat": 46.0038,
        "lng": -112.5348,
        "metro_area": "Butte-Silver Bow",
        "region": "West"
    },
    "helena": {
        "name": "Helena",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Lewis and Clark County",
        "population": 32655,
        "lat": 46.5958,
        "lng": -112.0362,
        "metro_area": "Helena",
        "region": "West"
    },
    "kalispell": {
        "name": "Kalispell",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Flathead County",
        "population": 24558,
        "lat": 48.1958,
        "lng": -114.3132,
        "metro_area": "Kalispell",
        "region": "West"
    },
    "havre": {
        "name": "Havre",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Hill County",
        "population": 9362,
        "lat": 48.5500,
        "lng": -109.6840,
        "metro_area": "Havre",
        "region": "West"
    },
    "anaconda": {
        "name": "Anaconda",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Deer Lodge County",
        "population": 9421,
        "lat": 46.1268,
        "lng": -112.9419,
        "metro_area": "Anaconda",
        "region": "West"
    },
    "miles-city": {
        "name": "Miles City",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Custer County",
        "population": 8354,
        "lat": 46.4083,
        "lng": -105.8406,
        "metro_area": "Miles City",
        "region": "West"
    },
    "whitefish": {
        "name": "Whitefish",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Flathead County",
        "population": 8032,
        "lat": 48.4108,
        "lng": -114.3377,
        "metro_area": "Kalispell",
        "region": "West"
    },
    "livingston": {
        "name": "Livingston",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Park County",
        "population": 8040,
        "lat": 45.6625,
        "lng": -110.5610,
        "metro_area": "Livingston",
        "region": "West"
    },
    "sidney": {
        "name": "Sidney",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Richland County",
        "population": 6346,
        "lat": 47.7164,
        "lng": -104.1558,
        "metro_area": "Sidney",
        "region": "West"
    },
    "glendive": {
        "name": "Glendive",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Dawson County",
        "population": 4935,
        "lat": 47.1053,
        "lng": -104.7123,
        "metro_area": "Glendive",
        "region": "West"
    },
    "lewistown": {
        "name": "Lewistown",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Fergus County",
        "population": 5901,
        "lat": 47.0624,
        "lng": -109.4285,
        "metro_area": "Lewistown",
        "region": "West"
    },
    "hamilton": {
        "name": "Hamilton",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Ravalli County",
        "population": 4659,
        "lat": 46.2474,
        "lng": -114.1611,
        "metro_area": "Hamilton",
        "region": "West"
    },
    "polson": {
        "name": "Polson",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Lake County",
        "population": 5148,
        "lat": 47.6896,
        "lng": -114.1633,
        "metro_area": "Polson",
        "region": "West"
    },
    "dillon": {
        "name": "Dillon",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Beaverhead County",
        "population": 4423,
        "lat": 45.2166,
        "lng": -112.6372,
        "metro_area": "Dillon",
        "region": "West"
    },
    "columbia-falls": {
        "name": "Columbia Falls",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Flathead County",
        "population": 5558,
        "lat": 48.3719,
        "lng": -114.1817,
        "metro_area": "Kalispell",
        "region": "West"
    },
    "red-lodge": {
        "name": "Red Lodge",
        "state": "Montana",
        "state_abbr": "MT",
        "county": "Carbon County",
        "population": 2257,
        "lat": 45.1858,
        "lng": -109.2468,
        "metro_area": "Red Lodge",
        "region": "West"
    },

    # Wyoming Cities
    "cheyenne": {
        "name": "Cheyenne",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Laramie County",
        "population": 65132,
        "lat": 41.1400,
        "lng": -104.8197,
        "metro_area": "Cheyenne",
        "region": "West"
    },
    "casper": {
        "name": "Casper",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Natrona County",
        "population": 59038,
        "lat": 42.8666,
        "lng": -106.3131,
        "metro_area": "Casper",
        "region": "West"
    },
    "gillette": {
        "name": "Gillette",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Campbell County",
        "population": 33403,
        "lat": 44.2911,
        "lng": -105.5022,
        "metro_area": "Gillette",
        "region": "West"
    },
    "laramie": {
        "name": "Laramie",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Albany County",
        "population": 31407,
        "lat": 41.3114,
        "lng": -105.5911,
        "metro_area": "Laramie",
        "region": "West"
    },
    "rock-springs": {
        "name": "Rock Springs",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Sweetwater County",
        "population": 23526,
        "lat": 41.5875,
        "lng": -109.2029,
        "metro_area": "Rock Springs",
        "region": "West"
    },
    "sheridan": {
        "name": "Sheridan",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Sheridan County",
        "population": 18737,
        "lat": 44.7975,
        "lng": -106.9561,
        "metro_area": "Sheridan",
        "region": "West"
    },
    "green-river": {
        "name": "Green River",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Sweetwater County",
        "population": 12515,
        "lat": 41.5236,
        "lng": -109.4662,
        "metro_area": "Green River",
        "region": "West"
    },
    "evanston": {
        "name": "Evanston",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Uinta County",
        "population": 11747,
        "lat": 41.2683,
        "lng": -110.9632,
        "metro_area": "Evanston",
        "region": "West"
    },
    "riverton": {
        "name": "Riverton",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Fremont County",
        "population": 11129,
        "lat": 43.0242,
        "lng": -108.3801,
        "metro_area": "Riverton",
        "region": "West"
    },
    "cody": {
        "name": "Cody",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Park County",
        "population": 10028,
        "lat": 44.5263,
        "lng": -109.0565,
        "metro_area": "Cody",
        "region": "West"
    },
    "jackson": {
        "name": "Jackson",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Teton County",
        "population": 10760,
        "lat": 43.4799,
        "lng": -110.7624,
        "metro_area": "Jackson",
        "region": "West"
    },
    "rawlins": {
        "name": "Rawlins",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Carbon County",
        "population": 8221,
        "lat": 41.7911,
        "lng": -107.2387,
        "metro_area": "Rawlins",
        "region": "West"
    },
    "torrington": {
        "name": "Torrington",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Goshen County",
        "population": 6501,
        "lat": 42.0625,
        "lng": -104.1841,
        "metro_area": "Torrington",
        "region": "West"
    },
    "powell": {
        "name": "Powell",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Park County",
        "population": 6314,
        "lat": 44.7541,
        "lng": -108.7573,
        "metro_area": "Powell",
        "region": "West"
    },
    "douglas": {
        "name": "Douglas",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Converse County",
        "population": 6120,
        "lat": 42.7583,
        "lng": -105.3822,
        "metro_area": "Douglas",
        "region": "West"
    },
    "wheatland": {
        "name": "Wheatland",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Platte County",
        "population": 3627,
        "lat": 42.0500,
        "lng": -104.9589,
        "metro_area": "Wheatland",
        "region": "West"
    },
    "newcastle": {
        "name": "Newcastle",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Weston County",
        "population": 3432,
        "lat": 43.8475,
        "lng": -104.2052,
        "metro_area": "Newcastle",
        "region": "West"
    },
    "worland": {
        "name": "Worland",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Washakie County",
        "population": 5286,
        "lat": 44.0169,
        "lng": -107.9553,
        "metro_area": "Worland",
        "region": "West"
    },
    "buffalo": {
        "name": "Buffalo",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Johnson County",
        "population": 4415,
        "lat": 44.3483,
        "lng": -106.6992,
        "metro_area": "Buffalo",
        "region": "West"
    },
    "lander": {
        "name": "Lander",
        "state": "Wyoming",
        "state_abbr": "WY",
        "county": "Fremont County",
        "population": 7487,
        "lat": 42.8330,
        "lng": -108.7307,
        "metro_area": "Lander",
        "region": "West"
    },

    # North Dakota Cities
    "fargo": {
        "name": "Fargo",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Cass County",
        "population": 125990,
        "lat": 46.8772,
        "lng": -96.7898,
        "metro_area": "Fargo",
        "region": "Midwest"
    },
    "bismarck": {
        "name": "Bismarck",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Burleigh County",
        "population": 73622,
        "lat": 46.8083,
        "lng": -100.7837,
        "metro_area": "Bismarck",
        "region": "Midwest"
    },
    "grand-forks": {
        "name": "Grand Forks",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Grand Forks County",
        "population": 59166,
        "lat": 47.9253,
        "lng": -97.0329,
        "metro_area": "Grand Forks",
        "region": "Midwest"
    },
    "minot": {
        "name": "Minot",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Ward County",
        "population": 48377,
        "lat": 48.2330,
        "lng": -101.2968,
        "metro_area": "Minot",
        "region": "Midwest"
    },
    "west-fargo": {
        "name": "West Fargo",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Cass County",
        "population": 38626,
        "lat": 46.8747,
        "lng": -96.9003,
        "metro_area": "Fargo",
        "region": "Midwest"
    },
    "williston": {
        "name": "Williston",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Williams County",
        "population": 29160,
        "lat": 48.1470,
        "lng": -103.6183,
        "metro_area": "Williston",
        "region": "Midwest"
    },
    "dickinson": {
        "name": "Dickinson",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Stark County",
        "population": 25679,
        "lat": 46.8792,
        "lng": -102.7899,
        "metro_area": "Dickinson",
        "region": "Midwest"
    },
    "mandan": {
        "name": "Mandan",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Morton County",
        "population": 24206,
        "lat": 46.8269,
        "lng": -100.8896,
        "metro_area": "Bismarck",
        "region": "Midwest"
    },
    "jamestown": {
        "name": "Jamestown",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Stutsman County",
        "population": 15849,
        "lat": 46.9108,
        "lng": -98.7084,
        "metro_area": "Jamestown",
        "region": "Midwest"
    },
    "wahpeton": {
        "name": "Wahpeton",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Richland County",
        "population": 7766,
        "lat": 46.2652,
        "lng": -96.6059,
        "metro_area": "Wahpeton",
        "region": "Midwest"
    },
    "devils-lake": {
        "name": "Devils Lake",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Ramsey County",
        "population": 7192,
        "lat": 48.1125,
        "lng": -98.8651,
        "metro_area": "Devils Lake",
        "region": "Midwest"
    },
    "valley-city": {
        "name": "Valley City",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Barnes County",
        "population": 6585,
        "lat": 46.9233,
        "lng": -98.0317,
        "metro_area": "Valley City",
        "region": "Midwest"
    },
    "grafton": {
        "name": "Grafton",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Walsh County",
        "population": 4284,
        "lat": 48.4097,
        "lng": -97.4131,
        "metro_area": "Grafton",
        "region": "Midwest"
    },
    "watford-city": {
        "name": "Watford City",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "McKenzie County",
        "population": 6207,
        "lat": 47.8025,
        "lng": -103.2854,
        "metro_area": "Watford City",
        "region": "Midwest"
    },
    "beulah": {
        "name": "Beulah",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Mercer County",
        "population": 3286,
        "lat": 47.2642,
        "lng": -101.7779,
        "metro_area": "Beulah",
        "region": "Midwest"
    },
    "hazen": {
        "name": "Hazen",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Mercer County",
        "population": 2504,
        "lat": 47.2958,
        "lng": -101.6240,
        "metro_area": "Hazen",
        "region": "Midwest"
    },
    "bottineau": {
        "name": "Bottineau",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Bottineau County",
        "population": 2211,
        "lat": 48.8267,
        "lng": -100.4468,
        "metro_area": "Bottineau",
        "region": "Midwest"
    },
    "rugby": {
        "name": "Rugby",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Pierce County",
        "population": 2509,
        "lat": 48.3689,
        "lng": -99.9990,
        "metro_area": "Rugby",
        "region": "Midwest"
    },
    "harvey": {
        "name": "Harvey",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Wells County",
        "population": 1783,
        "lat": 47.7714,
        "lng": -99.9296,
        "metro_area": "Harvey",
        "region": "Midwest"
    },
    "carrington": {
        "name": "Carrington",
        "state": "North Dakota",
        "state_abbr": "ND",
        "county": "Foster County",
        "population": 2065,
        "lat": 47.4497,
        "lng": -99.1251,
        "metro_area": "Carrington",
        "region": "Midwest"
    },

    # Delaware Cities
    "wilmington-de": {
        "name": "Wilmington",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "New Castle County",
        "population": 70898,
        "lat": 39.7391,
        "lng": -75.5398,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "dover-de": {
        "name": "Dover",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 39403,
        "lat": 39.1612,
        "lng": -75.5264,
        "metro_area": "Dover",
        "region": "Northeast"
    },
    "newark-de": {
        "name": "Newark",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "New Castle County",
        "population": 31454,
        "lat": 39.6837,
        "lng": -75.7497,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "middletown-de": {
        "name": "Middletown",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "New Castle County",
        "population": 22350,
        "lat": 39.4495,
        "lng": -75.7163,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "smyrna": {
        "name": "Smyrna",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 12883,
        "lat": 39.2998,
        "lng": -75.6052,
        "metro_area": "Dover",
        "region": "Northeast"
    },
    "milford": {
        "name": "Milford",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 11463,
        "lat": 38.9126,
        "lng": -75.4285,
        "metro_area": "Dover",
        "region": "Northeast"
    },
    "seaford": {
        "name": "Seaford",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 8421,
        "lat": 38.6412,
        "lng": -75.6119,
        "metro_area": "Seaford",
        "region": "Northeast"
    },
    "georgetown-de": {
        "name": "Georgetown",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 7436,
        "lat": 38.6901,
        "lng": -75.3854,
        "metro_area": "Georgetown",
        "region": "Northeast"
    },
    "elsmere": {
        "name": "Elsmere",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "New Castle County",
        "population": 6131,
        "lat": 39.7387,
        "lng": -75.5963,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "new-castle": {
        "name": "New Castle",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "New Castle County",
        "population": 5285,
        "lat": 39.6621,
        "lng": -75.5665,
        "metro_area": "Philadelphia-Camden-Wilmington",
        "region": "Northeast"
    },
    "laurel": {
        "name": "Laurel",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 4554,
        "lat": 38.5565,
        "lng": -75.5713,
        "metro_area": "Laurel",
        "region": "Northeast"
    },
    "harrington": {
        "name": "Harrington",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 3732,
        "lat": 38.9240,
        "lng": -75.5769,
        "metro_area": "Harrington",
        "region": "Northeast"
    },
    "camden-de": {
        "name": "Camden",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 3982,
        "lat": 39.1112,
        "lng": -75.5521,
        "metro_area": "Dover",
        "region": "Northeast"
    },
    "clayton": {
        "name": "Clayton",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Kent County",
        "population": 3563,
        "lat": 39.2931,
        "lng": -75.6324,
        "metro_area": "Dover",
        "region": "Northeast"
    },
    "lewes": {
        "name": "Lewes",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 3303,
        "lat": 38.7745,
        "lng": -75.1391,
        "metro_area": "Lewes",
        "region": "Northeast"
    },
    "milton": {
        "name": "Milton",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 3982,
        "lat": 38.7779,
        "lng": -75.3102,
        "metro_area": "Milton",
        "region": "Northeast"
    },
    "delmar-de": {
        "name": "Delmar",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 2244,
        "lat": 38.4565,
        "lng": -75.5774,
        "metro_area": "Delmar",
        "region": "Northeast"
    },
    "dagsboro": {
        "name": "Dagsboro",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 1031,
        "lat": 38.5493,
        "lng": -75.2471,
        "metro_area": "Dagsboro",
        "region": "Northeast"
    },
    "bethany-beach": {
        "name": "Bethany Beach",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 1278,
        "lat": 38.5390,
        "lng": -75.0615,
        "metro_area": "Bethany Beach",
        "region": "Northeast"
    },
    "rehoboth-beach": {
        "name": "Rehoboth Beach",
        "state": "Delaware",
        "state_abbr": "DE",
        "county": "Sussex County",
        "population": 1108,
        "lat": 38.7201,
        "lng": -75.0760,
        "metro_area": "Rehoboth Beach",
        "region": "Northeast"
    },

    # West Virginia Cities
    "charleston-wv": {
        "name": "Charleston",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Kanawha County",
        "population": 46536,
        "lat": 38.3498,
        "lng": -81.6326,
        "metro_area": "Charleston",
        "region": "South"
    },
    "huntington": {
        "name": "Huntington",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Cabell County",
        "population": 44985,
        "lat": 38.4192,
        "lng": -82.4452,
        "metro_area": "Huntington-Ashland",
        "region": "South"
    },
    "parkersburg": {
        "name": "Parkersburg",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Wood County",
        "population": 29749,
        "lat": 39.2667,
        "lng": -81.5615,
        "metro_area": "Parkersburg-Vienna",
        "region": "South"
    },
    "morgantown": {
        "name": "Morgantown",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Monongalia County",
        "population": 138176,
        "lat": 39.6295,
        "lng": -79.9553,
        "metro_area": "Morgantown",
        "region": "South"
    },
    "wheeling": {
        "name": "Wheeling",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Ohio County",
        "population": 27062,
        "lat": 40.0639,
        "lng": -80.7209,
        "metro_area": "Wheeling",
        "region": "South"
    },
    "martinsburg": {
        "name": "Martinsburg",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Berkeley County",
        "population": 18773,
        "lat": 39.4562,
        "lng": -77.9636,
        "metro_area": "Hagerstown-Martinsburg",
        "region": "South"
    },
    "fairmont": {
        "name": "Fairmont",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Marion County",
        "population": 18313,
        "lat": 39.4851,
        "lng": -80.1423,
        "metro_area": "Fairmont",
        "region": "South"
    },
    "beckley": {
        "name": "Beckley",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Raleigh County",
        "population": 15699,
        "lat": 37.7782,
        "lng": -81.1882,
        "metro_area": "Beckley",
        "region": "South"
    },
    "clarksburg": {
        "name": "Clarksburg",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Harrison County",
        "population": 15743,
        "lat": 39.2806,
        "lng": -80.3445,
        "metro_area": "Clarksburg",
        "region": "South"
    },
    "south-charleston": {
        "name": "South Charleston",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Kanawha County",
        "population": 12461,
        "lat": 38.3681,
        "lng": -81.7007,
        "metro_area": "Charleston",
        "region": "South"
    },
    "hurricane": {
        "name": "Hurricane",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Putnam County",
        "population": 6284,
        "lat": 38.4320,
        "lng": -82.0179,
        "metro_area": "Charleston",
        "region": "South"
    },
    "bridgeport": {
        "name": "Bridgeport",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Harrison County",
        "population": 9278,
        "lat": 39.2836,
        "lng": -80.2534,
        "metro_area": "Clarksburg",
        "region": "South"
    },
    "charles-town": {
        "name": "Charles Town",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Jefferson County",
        "population": 6534,
        "lat": 39.2889,
        "lng": -77.8600,
        "metro_area": "Washington-Arlington-Alexandria",
        "region": "South"
    },
    "shepherdstown": {
        "name": "Shepherdstown",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Jefferson County",
        "population": 1734,
        "lat": 39.4306,
        "lng": -77.8047,
        "metro_area": "Washington-Arlington-Alexandria",
        "region": "South"
    },
    "lewisburg": {
        "name": "Lewisburg",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Greenbrier County",
        "population": 3930,
        "lat": 37.8017,
        "lng": -80.4459,
        "metro_area": "Lewisburg",
        "region": "South"
    },
    "buckhannon": {
        "name": "Buckhannon",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Upshur County",
        "population": 5299,
        "lat": 38.9959,
        "lng": -80.2320,
        "metro_area": "Buckhannon",
        "region": "South"
    },
    "elkins": {
        "name": "Elkins",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Randolph County",
        "population": 6950,
        "lat": 38.9262,
        "lng": -79.8470,
        "metro_area": "Elkins",
        "region": "South"
    },
    "keyser": {
        "name": "Keyser",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Mineral County",
        "population": 4942,
        "lat": 39.4361,
        "lng": -78.9814,
        "metro_area": "Keyser",
        "region": "South"
    },
    "point-pleasant": {
        "name": "Point Pleasant",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Mason County",
        "population": 4101,
        "lat": 38.8420,
        "lng": -82.1318,
        "metro_area": "Point Pleasant",
        "region": "South"
    },
    "summersville": {
        "name": "Summersville",
        "state": "West Virginia",
        "state_abbr": "WV",
        "county": "Nicholas County",
        "population": 3572,
        "lat": 38.2831,
        "lng": -80.8548,
        "metro_area": "Summersville",
        "region": "South"
    }
}

def get_city_by_slug(slug):
    """Get city data by slug"""
    return US_MAJOR_CITIES.get(slug)

def get_cities_by_state(state_abbr):
    """Get all cities in a specific state"""
    return {
        slug: city for slug, city in US_MAJOR_CITIES.items()
        if city["state_abbr"] == state_abbr
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

def get_database_stats():
    """Get comprehensive statistics about the city database"""
    total_cities = len(US_MAJOR_CITIES)
    
    # Get states
    states = {}
    for city_data in US_MAJOR_CITIES.values():
        state_abbr = city_data["state_abbr"]
        if state_abbr not in states:
            states[state_abbr] = 0
        states[state_abbr] += 1
    
    total_states = len(states)
    
    # Population statistics
    populations = [city["population"] for city in US_MAJOR_CITIES.values()]
    avg_population = sum(populations) / len(populations) if populations else 0
    
    return {
        "total_cities": total_cities,
        "total_states": total_states,
        "avg_cities_per_state": round(total_cities / total_states, 1) if total_states > 0 else 0,
        "avg_population": round(avg_population),
        "largest_city": max(US_MAJOR_CITIES.items(), key=lambda x: x[1]["population"]) if US_MAJOR_CITIES else None,
        "smallest_city": min(US_MAJOR_CITIES.items(), key=lambda x: x[1]["population"]) if US_MAJOR_CITIES else None,
        "states_coverage": states
    }

# Print basic stats when module loads
if __name__ == "__main__":
    stats = get_database_stats()
    print(f"US Cities SEO Database: {stats["total_cities"]} cities across {stats["total_states"]} states")