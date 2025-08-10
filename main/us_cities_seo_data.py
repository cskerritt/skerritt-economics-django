"""
Comprehensive US cities data for SEO landing pages
Includes top 200+ cities by population with state, county, and geographic data
"""

US_MAJOR_CITIES = {
    # Format: "city-slug": {
    #     "name": "City Name",
    #     "state": "State Name",
    #     "state_abbr": "ST",
    #     "county": "County Name",
    #     "population": population_number,
    #     "lat": latitude,
    #     "lng": longitude,
    #     "metro_area": "Metro Area Name",
    #     "region": "Geographic Region"
    # }
    
    # Top 50 US Cities by Population
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
    "long-beach": {
        "name": "Long Beach",
        "state": "California",
        "state_abbr": "CA",
        "county": "Los Angeles County",
        "population": 462628,
        "lat": 33.7701,
        "lng": -118.1937,
        "metro_area": "Los Angeles-Long Beach-Anaheim",
        "region": "West"
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
    
    # Additional major cities
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
    "pembroke-pines": {
        "name": "Pembroke Pines",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Broward County",
        "population": 171178,
        "lat": 26.0032,
        "lng": -80.2237,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
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
    "murfreesboro": {
        "name": "Murfreesboro",
        "state": "Tennessee",
        "state_abbr": "TN",
        "county": "Rutherford County",
        "population": 146900,
        "lat": 35.8456,
        "lng": -86.3903,
        "metro_area": "Nashville-Davidson-Murfreesboro-Franklin",
        "region": "South"
    },
    "miramar": {
        "name": "Miramar",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Broward County",
        "population": 140328,
        "lat": 25.9860,
        "lng": -80.2322,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "warren": {
        "name": "Warren",
        "state": "Michigan",
        "state_abbr": "MI",
        "county": "Macomb County",
        "population": 133943,
        "lat": 42.5144,
        "lng": -83.0147,
        "metro_area": "Detroit-Warren-Dearborn",
        "region": "Midwest"
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
    "hampton": {
        "name": "Hampton",
        "state": "Virginia",
        "state_abbr": "VA",
        "county": "Hampton City",
        "population": 134510,
        "lat": 37.0299,
        "lng": -76.3452,
        "metro_area": "Virginia Beach-Norfolk-Newport News",
        "region": "South"
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
    "coral-springs": {
        "name": "Coral Springs",
        "state": "Florida",
        "state_abbr": "FL",
        "county": "Broward County",
        "population": 133507,
        "lat": 26.2712,
        "lng": -80.2706,
        "metro_area": "Miami-Fort Lauderdale-West Palm Beach",
        "region": "South"
    },
    "denton": {
        "name": "Denton",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Denton County",
        "population": 138541,
        "lat": 33.2148,
        "lng": -97.1331,
        "metro_area": "Dallas-Fort Worth-Arlington",
        "region": "South"
    },
    "midland": {
        "name": "Midland",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Midland County",
        "population": 136872,
        "lat": 31.9973,
        "lng": -102.0779,
        "metro_area": "Midland",
        "region": "South"
    },
    "waco": {
        "name": "Waco",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "McLennan County",
        "population": 138444,
        "lat": 31.5493,
        "lng": -97.1467,
        "metro_area": "Waco",
        "region": "South"
    },
    "carrollton": {
        "name": "Carrollton",
        "state": "Texas",
        "state_abbr": "TX",
        "county": "Dallas County",
        "population": 133351,
        "lat": 32.9537,
        "lng": -96.8903,
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
    "peoria": {
        "name": "Peoria",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 175961,
        "lat": 33.5806,
        "lng": -112.2374,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "surprise": {
        "name": "Surprise",
        "state": "Arizona",
        "state_abbr": "AZ",
        "county": "Maricopa County",
        "population": 141664,
        "lat": 33.6292,
        "lng": -112.3679,
        "metro_area": "Phoenix-Mesa-Scottsdale",
        "region": "Southwest"
    },
    "lafayette": {
        "name": "Lafayette",
        "state": "Louisiana",
        "state_abbr": "LA",
        "county": "Lafayette Parish",
        "population": 126185,
        "lat": 30.2241,
        "lng": -92.0198,
        "metro_area": "Lafayette",
        "region": "South"
    },
    "kent": {
        "name": "Kent",
        "state": "Washington",
        "state_abbr": "WA",
        "county": "King County",
        "population": 129618,
        "lat": 47.3809,
        "lng": -122.2348,
        "metro_area": "Seattle-Tacoma-Bellevue",
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
    "charleston": {
        "name": "Charleston",
        "state": "South Carolina",
        "state_abbr": "SC",
        "county": "Charleston County",
        "population": 137566,
        "lat": 32.7765,
        "lng": -79.9311,
        "metro_area": "Charleston-North Charleston",
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
        if city['state_abbr'] == state_abbr
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
        if slug != city_slug and other_city.get('metro_area') == city.get('metro_area'):
            nearby.append({
                'slug': slug,
                'name': other_city['name'],
                'state_abbr': other_city['state_abbr']
            })
            if len(nearby) >= limit:
                return nearby[:limit]
    
    # Then add cities in same state
    for slug, other_city in US_MAJOR_CITIES.items():
        if slug != city_slug and other_city['state_abbr'] == city['state_abbr']:
            if not any(n['slug'] == slug for n in nearby):
                nearby.append({
                    'slug': slug,
                    'name': other_city['name'],
                    'state_abbr': other_city['state_abbr']
                })
                if len(nearby) >= limit:
                    return nearby[:limit]
    
    return nearby[:limit]

def get_top_cities_by_population(limit=50):
    """Get top cities by population"""
    sorted_cities = sorted(
        US_MAJOR_CITIES.items(),
        key=lambda x: x[1]['population'],
        reverse=True
    )
    return dict(sorted_cities[:limit])