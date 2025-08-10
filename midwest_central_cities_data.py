"""
Comprehensive City Data for Midwest and Central States
Created for Skerritt Economics Django Website SEO Coverage
Top 20 cities for 12 states: Illinois, Michigan, Ohio, Indiana, Wisconsin, Minnesota, Iowa, Missouri, Kansas, Nebraska, North Dakota, South Dakota
"""

MIDWEST_CENTRAL_CITIES = {
    # Illinois - Top 20 cities
    "illinois": {
        "name": "Illinois",
        "state_abbr": "IL",
        "cities": [
            {"name": "Chicago", "slug": "chicago", "county": "Cook County", "lat": 41.8781, "lng": -87.6298, "population": 2664452, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Aurora", "slug": "aurora", "county": "Kane County", "lat": 41.7606, "lng": -88.3201, "population": 177563, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Naperville", "slug": "naperville", "county": "DuPage County", "lat": 41.7508, "lng": -88.1535, "population": 153124, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Joliet", "slug": "joliet", "county": "Will County", "lat": 41.5250, "lng": -88.0817, "population": 151837, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Rockford", "slug": "rockford", "county": "Winnebago County", "lat": 42.2711, "lng": -89.0940, "population": 146120, "metro_area": "Rockford", "region": "Midwest"},
            {"name": "Elgin", "slug": "elgin", "county": "Kane County", "lat": 42.0370, "lng": -88.2826, "population": 114797, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Peoria", "slug": "peoria", "county": "Peoria County", "lat": 40.6936, "lng": -89.5890, "population": 113150, "metro_area": "Peoria", "region": "Midwest"},
            {"name": "Springfield", "slug": "springfield", "county": "Sangamon County", "lat": 39.7817, "lng": -89.6501, "population": 112544, "metro_area": "Springfield", "region": "Midwest"},
            {"name": "Waukegan", "slug": "waukegan", "county": "Lake County", "lat": 42.3636, "lng": -87.8448, "population": 89321, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Cicero", "slug": "cicero", "county": "Cook County", "lat": 41.8456, "lng": -87.7539, "population": 85616, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Evanston", "slug": "evanston", "county": "Cook County", "lat": 42.0451, "lng": -87.6877, "population": 78110, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Schaumburg", "slug": "schaumburg", "county": "Cook County", "lat": 42.0334, "lng": -88.0834, "population": 78723, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Bolingbrook", "slug": "bolingbrook", "county": "Will County", "lat": 41.6986, "lng": -88.0684, "population": 75201, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Palatine", "slug": "palatine", "county": "Cook County", "lat": 42.1103, "lng": -88.0342, "population": 67908, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Skokie", "slug": "skokie", "county": "Cook County", "lat": 42.0334, "lng": -87.7334, "population": 67824, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Des Plaines", "slug": "des-plaines", "county": "Cook County", "lat": 42.0334, "lng": -87.8834, "population": 58768, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Orland Park", "slug": "orland-park", "county": "Cook County", "lat": 41.6303, "lng": -87.8540, "population": 58703, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Tinley Park", "slug": "tinley-park", "county": "Cook County", "lat": 41.5731, "lng": -87.7856, "population": 55971, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Oak Lawn", "slug": "oak-lawn", "county": "Cook County", "lat": 41.7197, "lng": -87.7479, "population": 55245, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Berwyn", "slug": "berwyn", "county": "Cook County", "lat": 41.8505, "lng": -87.7937, "population": 54016, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"}
        ]
    },

    # Michigan - Top 20 cities
    "michigan": {
        "name": "Michigan",
        "state_abbr": "MI",
        "cities": [
            {"name": "Detroit", "slug": "detroit", "county": "Wayne County", "lat": 42.3314, "lng": -83.0458, "population": 645700, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Grand Rapids", "slug": "grand-rapids", "county": "Kent County", "lat": 42.9634, "lng": -85.6681, "population": 200117, "metro_area": "Grand Rapids-Kentwood", "region": "Midwest"},
            {"name": "Warren", "slug": "warren", "county": "Macomb County", "lat": 42.5145, "lng": -83.0146, "population": 137686, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Sterling Heights", "slug": "sterling-heights", "county": "Macomb County", "lat": 42.5803, "lng": -83.0302, "population": 132342, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Ann Arbor", "slug": "ann-arbor", "county": "Washtenaw County", "lat": 42.2808, "lng": -83.7430, "population": 117070, "metro_area": "Ann Arbor", "region": "Midwest"},
            {"name": "Lansing", "slug": "lansing", "county": "Ingham County", "lat": 42.3223, "lng": -84.5361, "population": 115056, "metro_area": "Lansing-East Lansing", "region": "Midwest"},
            {"name": "Dearborn", "slug": "dearborn", "county": "Wayne County", "lat": 42.3223, "lng": -83.1763, "population": 108420, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Livonia", "slug": "livonia", "county": "Wayne County", "lat": 42.3684, "lng": -83.3527, "population": 93971, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Troy", "slug": "troy", "county": "Oakland County", "lat": 42.6064, "lng": -83.1498, "population": 87294, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Westland", "slug": "westland", "county": "Wayne County", "lat": 42.3242, "lng": -83.4002, "population": 84037, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Farmington Hills", "slug": "farmington-hills", "county": "Oakland County", "lat": 42.4989, "lng": -83.3677, "population": 83986, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Kalamazoo", "slug": "kalamazoo", "county": "Kalamazoo County", "lat": 42.2917, "lng": -85.5872, "population": 75092, "metro_area": "Kalamazoo-Portage", "region": "Midwest"},
            {"name": "Wyoming", "slug": "wyoming", "county": "Kent County", "lat": 42.9134, "lng": -85.7053, "population": 76501, "metro_area": "Grand Rapids-Kentwood", "region": "Midwest"},
            {"name": "Southfield", "slug": "southfield", "county": "Oakland County", "lat": 42.4734, "lng": -83.2219, "population": 76618, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Rochester Hills", "slug": "rochester-hills", "county": "Oakland County", "lat": 42.6583, "lng": -83.1499, "population": 76300, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Taylor", "slug": "taylor", "county": "Wayne County", "lat": 42.2409, "lng": -83.2696, "population": 70811, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Pontiac", "slug": "pontiac", "county": "Oakland County", "lat": 42.6389, "lng": -83.2910, "population": 61606, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "St. Clair Shores", "slug": "st-clair-shores", "county": "Macomb County", "lat": 42.4967, "lng": -82.8885, "population": 59749, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Royal Oak", "slug": "royal-oak", "county": "Oakland County", "lat": 42.4895, "lng": -83.1446, "population": 59256, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"},
            {"name": "Novi", "slug": "novi", "county": "Oakland County", "lat": 42.4759, "lng": -83.4755, "population": 66243, "metro_area": "Detroit-Warren-Dearborn", "region": "Midwest"}
        ]
    },

    # Ohio - Top 20 cities
    "ohio": {
        "name": "Ohio",
        "state_abbr": "OH",
        "cities": [
            {"name": "Columbus", "slug": "columbus", "county": "Franklin County", "lat": 39.9612, "lng": -82.9988, "population": 913175, "metro_area": "Columbus", "region": "Midwest"},
            {"name": "Cleveland", "slug": "cleveland", "county": "Cuyahoga County", "lat": 41.4995, "lng": -81.6954, "population": 362656, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Cincinnati", "slug": "cincinnati", "county": "Hamilton County", "lat": 39.1612, "lng": -84.4569, "population": 311097, "metro_area": "Cincinnati", "region": "Midwest"},
            {"name": "Toledo", "slug": "toledo", "county": "Lucas County", "lat": 41.6528, "lng": -83.5379, "population": 265304, "metro_area": "Toledo", "region": "Midwest"},
            {"name": "Akron", "slug": "akron", "county": "Summit County", "lat": 41.0814, "lng": -81.5190, "population": 188701, "metro_area": "Akron", "region": "Midwest"},
            {"name": "Dayton", "slug": "dayton", "county": "Montgomery County", "lat": 39.7589, "lng": -84.1916, "population": 135944, "metro_area": "Dayton-Kettering", "region": "Midwest"},
            {"name": "Parma", "slug": "parma", "county": "Cuyahoga County", "lat": 41.4047, "lng": -81.7229, "population": 81146, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Canton", "slug": "canton", "county": "Stark County", "lat": 40.7989, "lng": -81.3784, "population": 70872, "metro_area": "Canton-Massillon", "region": "Midwest"},
            {"name": "Youngstown", "slug": "youngstown", "county": "Mahoning County", "lat": 41.0998, "lng": -80.6495, "population": 60068, "metro_area": "Youngstown-Warren-Boardman", "region": "Midwest"},
            {"name": "Lorain", "slug": "lorain", "county": "Lorain County", "lat": 41.4528, "lng": -82.1824, "population": 65211, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Hamilton", "slug": "hamilton", "county": "Butler County", "lat": 39.3995, "lng": -84.5613, "population": 62407, "metro_area": "Cincinnati", "region": "Midwest"},
            {"name": "Springfield", "slug": "springfield", "county": "Clark County", "lat": 39.9242, "lng": -83.8088, "population": 58662, "metro_area": "Springfield", "region": "Midwest"},
            {"name": "Kettering", "slug": "kettering", "county": "Montgomery County", "lat": 39.6895, "lng": -84.1688, "population": 57862, "metro_area": "Dayton-Kettering", "region": "Midwest"},
            {"name": "Elyria", "slug": "elyria", "county": "Lorain County", "lat": 41.3684, "lng": -82.1076, "population": 52656, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Lakewood", "slug": "lakewood", "county": "Cuyahoga County", "lat": 41.4820, "lng": -81.7982, "population": 50942, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Cuyahoga Falls", "slug": "cuyahoga-falls", "county": "Summit County", "lat": 41.1340, "lng": -81.4846, "population": 51114, "metro_area": "Akron", "region": "Midwest"},
            {"name": "Euclid", "slug": "euclid", "county": "Cuyahoga County", "lat": 41.5931, "lng": -81.5268, "population": 49692, "metro_area": "Cleveland-Elyria", "region": "Midwest"},
            {"name": "Middletown", "slug": "middletown", "county": "Butler County", "lat": 39.5151, "lng": -84.3982, "population": 50987, "metro_area": "Cincinnati", "region": "Midwest"},
            {"name": "Mansfield", "slug": "mansfield", "county": "Richland County", "lat": 40.7584, "lng": -82.5154, "population": 46454, "metro_area": "Mansfield", "region": "Midwest"},
            {"name": "Beavercreek", "slug": "beavercreek", "county": "Greene County", "lat": 39.7092, "lng": -84.0633, "population": 47741, "metro_area": "Dayton-Kettering", "region": "Midwest"}
        ]
    },

    # Indiana - Top 20 cities
    "indiana": {
        "name": "Indiana",
        "state_abbr": "IN",
        "cities": [
            {"name": "Indianapolis", "slug": "indianapolis", "county": "Marion County", "lat": 39.7684, "lng": -86.1581, "population": 888578, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Fort Wayne", "slug": "fort-wayne", "county": "Allen County", "lat": 41.0793, "lng": -85.1394, "population": 269994, "metro_area": "Fort Wayne", "region": "Midwest"},
            {"name": "Evansville", "slug": "evansville", "county": "Vanderburgh County", "lat": 37.9716, "lng": -87.5710, "population": 115332, "metro_area": "Evansville", "region": "Midwest"},
            {"name": "South Bend", "slug": "south-bend", "county": "St. Joseph County", "lat": 41.6764, "lng": -86.2520, "population": 103395, "metro_area": "South Bend-Mishawaka", "region": "Midwest"},
            {"name": "Carmel", "slug": "carmel", "county": "Hamilton County", "lat": 39.9784, "lng": -86.1180, "population": 103136, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Fishers", "slug": "fishers", "county": "Hamilton County", "lat": 39.9568, "lng": -85.9685, "population": 104094, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Bloomington", "slug": "bloomington", "county": "Monroe County", "lat": 39.1653, "lng": -86.5264, "population": 79168, "metro_area": "Bloomington", "region": "Midwest"},
            {"name": "Hammond", "slug": "hammond", "county": "Lake County", "lat": 41.5834, "lng": -87.5001, "population": 77879, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Gary", "slug": "gary", "county": "Lake County", "lat": 41.5937, "lng": -87.3464, "population": 67652, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Lafayette", "slug": "lafayette", "county": "Tippecanoe County", "lat": 40.4167, "lng": -86.8753, "population": 71372, "metro_area": "Lafayette-West Lafayette", "region": "Midwest"},
            {"name": "Muncie", "slug": "muncie", "county": "Delaware County", "lat": 40.1934, "lng": -85.3863, "population": 65194, "metro_area": "Muncie", "region": "Midwest"},
            {"name": "Terre Haute", "slug": "terre-haute", "county": "Vigo County", "lat": 39.4667, "lng": -87.4139, "population": 58389, "metro_area": "Terre Haute", "region": "Midwest"},
            {"name": "Noblesville", "slug": "noblesville", "county": "Hamilton County", "lat": 40.0456, "lng": -86.0086, "population": 69604, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Anderson", "slug": "anderson", "county": "Madison County", "lat": 40.1053, "lng": -85.6803, "population": 54476, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Greenwood", "slug": "greenwood", "county": "Johnson County", "lat": 39.6136, "lng": -86.1064, "population": 63830, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Elkhart", "slug": "elkhart", "county": "Elkhart County", "lat": 41.6819, "lng": -85.9767, "population": 53923, "metro_area": "Elkhart-Goshen", "region": "Midwest"},
            {"name": "Mishawaka", "slug": "mishawaka", "county": "St. Joseph County", "lat": 41.6620, "lng": -86.1586, "population": 51063, "metro_area": "South Bend-Mishawaka", "region": "Midwest"},
            {"name": "Lawrence", "slug": "lawrence", "county": "Marion County", "lat": 39.8386, "lng": -85.9975, "population": 49370, "metro_area": "Indianapolis-Carmel-Anderson", "region": "Midwest"},
            {"name": "Jeffersonville", "slug": "jeffersonville", "county": "Clark County", "lat": 38.2775, "lng": -85.7372, "population": 49447, "metro_area": "Louisville-Jefferson County", "region": "Midwest"},
            {"name": "Columbus", "slug": "columbus", "county": "Bartholomew County", "lat": 39.2014, "lng": -85.9214, "population": 50474, "metro_area": "Columbus", "region": "Midwest"}
        ]
    },

    # Wisconsin - Top 20 cities
    "wisconsin": {
        "name": "Wisconsin",
        "state_abbr": "WI",
        "cities": [
            {"name": "Milwaukee", "slug": "milwaukee", "county": "Milwaukee County", "lat": 43.0389, "lng": -87.9065, "population": 561385, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Madison", "slug": "madison", "county": "Dane County", "lat": 43.0731, "lng": -89.4012, "population": 280305, "metro_area": "Madison", "region": "Midwest"},
            {"name": "Green Bay", "slug": "green-bay", "county": "Brown County", "lat": 44.5133, "lng": -88.0133, "population": 105744, "metro_area": "Green Bay", "region": "Midwest"},
            {"name": "Kenosha", "slug": "kenosha", "county": "Kenosha County", "lat": 42.5847, "lng": -87.8212, "population": 98211, "metro_area": "Chicago-Naperville-Elgin", "region": "Midwest"},
            {"name": "Racine", "slug": "racine", "county": "Racine County", "lat": 42.7261, "lng": -87.7829, "population": 76602, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Appleton", "slug": "appleton", "county": "Outagamie County", "lat": 44.2619, "lng": -88.4154, "population": 75092, "metro_area": "Appleton", "region": "Midwest"},
            {"name": "Waukesha", "slug": "waukesha", "county": "Waukesha County", "lat": 43.0117, "lng": -88.2315, "population": 72419, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Eau Claire", "slug": "eau-claire", "county": "Eau Claire County", "lat": 44.8113, "lng": -91.4985, "population": 69421, "metro_area": "Eau Claire", "region": "Midwest"},
            {"name": "Oshkosh", "slug": "oshkosh", "county": "Winnebago County", "lat": 44.0247, "lng": -88.5426, "population": 66653, "metro_area": "Oshkosh-Neenah", "region": "Midwest"},
            {"name": "Janesville", "slug": "janesville", "county": "Rock County", "lat": 42.6828, "lng": -89.0187, "population": 65615, "metro_area": "Janesville-Beloit", "region": "Midwest"},
            {"name": "West Allis", "slug": "west-allis", "county": "Milwaukee County", "lat": 43.0167, "lng": -88.0070, "population": 58698, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "La Crosse", "slug": "la-crosse", "county": "La Crosse County", "lat": 43.8014, "lng": -91.2396, "population": 52680, "metro_area": "La Crosse-Onalaska", "region": "Midwest"},
            {"name": "Sheboygan", "slug": "sheboygan", "county": "Sheboygan County", "lat": 43.7508, "lng": -87.7145, "population": 48153, "metro_area": "Sheboygan", "region": "Midwest"},
            {"name": "Wauwatosa", "slug": "wauwatosa", "county": "Milwaukee County", "lat": 43.0494, "lng": -88.0078, "population": 48387, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Fond du Lac", "slug": "fond-du-lac", "county": "Fond du Lac County", "lat": 43.7730, "lng": -88.4487, "population": 42944, "metro_area": "Fond du Lac", "region": "Midwest"},
            {"name": "New Berlin", "slug": "new-berlin", "county": "Waukesha County", "lat": 42.9764, "lng": -88.1084, "population": 40451, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Wausau", "slug": "wausau", "county": "Marathon County", "lat": 44.9591, "lng": -89.6301, "population": 39994, "metro_area": "Wausau-Weston", "region": "Midwest"},
            {"name": "Brookfield", "slug": "brookfield", "county": "Waukesha County", "lat": 43.0642, "lng": -88.1065, "population": 38649, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Greenfield", "slug": "greenfield", "county": "Milwaukee County", "lat": 42.9614, "lng": -88.0126, "population": 37159, "metro_area": "Milwaukee-Waukesha", "region": "Midwest"},
            {"name": "Beloit", "slug": "beloit", "county": "Rock County", "lat": 42.5084, "lng": -89.0318, "population": 36804, "metro_area": "Janesville-Beloit", "region": "Midwest"}
        ]
    },

    # Minnesota - Top 20 cities
    "minnesota": {
        "name": "Minnesota",
        "state_abbr": "MN",
        "cities": [
            {"name": "Minneapolis", "slug": "minneapolis", "county": "Hennepin County", "lat": 44.9778, "lng": -93.2650, "population": 433633, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "St. Paul", "slug": "st-paul", "county": "Ramsey County", "lat": 44.9537, "lng": -93.0900, "population": 310997, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Rochester", "slug": "rochester", "county": "Olmsted County", "lat": 44.0121, "lng": -92.4802, "population": 122969, "metro_area": "Rochester", "region": "Midwest"},
            {"name": "Bloomington", "slug": "bloomington", "county": "Hennepin County", "lat": 44.8408, "lng": -93.2982, "population": 91537, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Duluth", "slug": "duluth", "county": "St. Louis County", "lat": 46.7867, "lng": -92.1005, "population": 87680, "metro_area": "Duluth", "region": "Midwest"},
            {"name": "Brooklyn Park", "slug": "brooklyn-park", "county": "Hennepin County", "lat": 45.0941, "lng": -93.3563, "population": 88618, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Plymouth", "slug": "plymouth", "county": "Hennepin County", "lat": 45.0105, "lng": -93.4555, "population": 83116, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Woodbury", "slug": "woodbury", "county": "Washington County", "lat": 44.9239, "lng": -92.9594, "population": 77730, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Lakeville", "slug": "lakeville", "county": "Dakota County", "lat": 44.6496, "lng": -93.2427, "population": 72581, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Blaine", "slug": "blaine", "county": "Anoka County", "lat": 45.1608, "lng": -93.2349, "population": 71139, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Burnsville", "slug": "burnsville", "county": "Dakota County", "lat": 44.7677, "lng": -93.2777, "population": 64317, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Eden Prairie", "slug": "eden-prairie", "county": "Hennepin County", "lat": 44.8547, "lng": -93.4708, "population": 64198, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Coon Rapids", "slug": "coon-rapids", "county": "Anoka County", "lat": 45.1732, "lng": -93.3030, "population": 63599, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Apple Valley", "slug": "apple-valley", "county": "Dakota County", "lat": 44.7319, "lng": -93.2177, "population": 56374, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Minnetonka", "slug": "minnetonka", "county": "Hennepin County", "lat": 44.9211, "lng": -93.4687, "population": 54967, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Eagan", "slug": "eagan", "county": "Dakota County", "lat": 44.8041, "lng": -93.166, "population": 68855, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "Edina", "slug": "edina", "county": "Hennepin County", "lat": 44.8897, "lng": -93.3499, "population": 53494, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"},
            {"name": "St. Cloud", "slug": "st-cloud", "county": "Stearns County", "lat": 45.5608, "lng": -94.1622, "population": 69226, "metro_area": "St. Cloud", "region": "Midwest"},
            {"name": "Mankato", "slug": "mankato", "county": "Blue Earth County", "lat": 44.1636, "lng": -93.9993, "population": 44488, "metro_area": "Mankato", "region": "Midwest"},
            {"name": "Maplewood", "slug": "maplewood", "county": "Ramsey County", "lat": 44.9530, "lng": -92.9952, "population": 42088, "metro_area": "Minneapolis-St. Paul-Bloomington", "region": "Midwest"}
        ]
    },

    # Iowa - Top 20 cities
    "iowa": {
        "name": "Iowa",
        "state_abbr": "IA",
        "cities": [
            {"name": "Des Moines", "slug": "des-moines", "county": "Polk County", "lat": 41.5868, "lng": -93.6250, "population": 210381, "metro_area": "Des Moines-West Des Moines", "region": "Midwest"},
            {"name": "Cedar Rapids", "slug": "cedar-rapids", "county": "Linn County", "lat": 41.9778, "lng": -91.6656, "population": 135958, "metro_area": "Cedar Rapids", "region": "Midwest"},
            {"name": "Davenport", "slug": "davenport", "county": "Scott County", "lat": 41.5236, "lng": -90.5776, "population": 100354, "metro_area": "Davenport-Moline-Rock Island", "region": "Midwest"},
            {"name": "Sioux City", "slug": "sioux-city", "county": "Woodbury County", "lat": 42.4999, "lng": -96.4003, "population": 85727, "metro_area": "Sioux City", "region": "Midwest"},
            {"name": "Iowa City", "slug": "iowa-city", "county": "Johnson County", "lat": 41.6611, "lng": -91.5302, "population": 75678, "metro_area": "Iowa City", "region": "Midwest"},
            {"name": "Ankeny", "slug": "ankeny", "county": "Polk County", "lat": 41.7297, "lng": -93.6058, "population": 68634, "metro_area": "Des Moines-West Des Moines", "region": "Midwest"},
            {"name": "West Des Moines", "slug": "west-des-moines", "county": "Polk County", "lat": 41.5772, "lng": -93.7114, "population": 68723, "metro_area": "Des Moines-West Des Moines", "region": "Midwest"},
            {"name": "Waterloo", "slug": "waterloo", "county": "Black Hawk County", "lat": 42.4928, "lng": -92.3426, "population": 66467, "metro_area": "Waterloo-Cedar Falls", "region": "Midwest"},
            {"name": "Ames", "slug": "ames", "county": "Story County", "lat": 42.0308, "lng": -93.6319, "population": 66427, "metro_area": "Ames", "region": "Midwest"},
            {"name": "Council Bluffs", "slug": "council-bluffs", "county": "Pottawattamie County", "lat": 41.2619, "lng": -95.8608, "population": 62261, "metro_area": "Omaha-Council Bluffs", "region": "Midwest"},
            {"name": "Dubuque", "slug": "dubuque", "county": "Dubuque County", "lat": 42.5006, "lng": -90.6648, "population": 59667, "metro_area": "Dubuque", "region": "Midwest"},
            {"name": "Cedar Falls", "slug": "cedar-falls", "county": "Black Hawk County", "lat": 42.5347, "lng": -92.4453, "population": 40713, "metro_area": "Waterloo-Cedar Falls", "region": "Midwest"},
            {"name": "Marion", "slug": "marion", "county": "Linn County", "lat": 42.0347, "lng": -91.5970, "population": 41535, "metro_area": "Cedar Rapids", "region": "Midwest"},
            {"name": "Bettendorf", "slug": "bettendorf", "county": "Scott County", "lat": 41.5236, "lng": -90.5151, "population": 39102, "metro_area": "Davenport-Moline-Rock Island", "region": "Midwest"},
            {"name": "Marshalltown", "slug": "marshalltown", "county": "Marshall County", "lat": 42.0497, "lng": -92.9079, "population": 27552, "metro_area": "Marshalltown", "region": "Midwest"},
            {"name": "Mason City", "slug": "mason-city", "county": "Cerro Gordo County", "lat": 43.1536, "lng": -93.2016, "population": 27333, "metro_area": "Mason City", "region": "Midwest"},
            {"name": "Burlington", "slug": "burlington", "county": "Des Moines County", "lat": 40.8077, "lng": -91.1129, "population": 23982, "metro_area": "Burlington", "region": "Midwest"},
            {"name": "Fort Dodge", "slug": "fort-dodge", "county": "Webster County", "lat": 42.4975, "lng": -94.1681, "population": 24168, "metro_area": "Fort Dodge", "region": "Midwest"},
            {"name": "Ottumwa", "slug": "ottumwa", "county": "Wapello County", "lat": 41.0197, "lng": -92.4113, "population": 24505, "metro_area": "Ottumwa", "region": "Midwest"},
            {"name": "Urbandale", "slug": "urbandale", "county": "Polk County", "lat": 41.6266, "lng": -93.7119, "population": 45588, "metro_area": "Des Moines-West Des Moines", "region": "Midwest"}
        ]
    },

    # Missouri - Top 20 cities
    "missouri": {
        "name": "Missouri",
        "state_abbr": "MO",
        "cities": [
            {"name": "Kansas City", "slug": "kansas-city", "county": "Jackson County", "lat": 39.0997, "lng": -94.5786, "population": 510704, "metro_area": "Kansas City", "region": "Midwest"},
            {"name": "St. Louis", "slug": "st-louis", "county": "Independent City", "lat": 38.6270, "lng": -90.1994, "population": 281754, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Springfield", "slug": "springfield", "county": "Greene County", "lat": 37.2089, "lng": -93.2923, "population": 170188, "metro_area": "Springfield", "region": "Midwest"},
            {"name": "Columbia", "slug": "columbia", "county": "Boone County", "lat": 38.9517, "lng": -92.3341, "population": 129330, "metro_area": "Columbia", "region": "Midwest"},
            {"name": "Independence", "slug": "independence", "county": "Jackson County", "lat": 39.0911, "lng": -94.4155, "population": 120922, "metro_area": "Kansas City", "region": "Midwest"},
            {"name": "Lee's Summit", "slug": "lees-summit", "county": "Jackson County", "lat": 38.9108, "lng": -94.3822, "population": 101108, "metro_area": "Kansas City", "region": "Midwest"},
            {"name": "O'Fallon", "slug": "ofallon", "county": "St. Charles County", "lat": 38.8106, "lng": -90.6999, "population": 91316, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "St. Joseph", "slug": "st-joseph", "county": "Buchanan County", "lat": 39.7391, "lng": -94.8469, "population": 72473, "metro_area": "St. Joseph", "region": "Midwest"},
            {"name": "St. Charles", "slug": "st-charles", "county": "St. Charles County", "lat": 38.7881, "lng": -90.4974, "population": 71654, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "St. Peters", "slug": "st-peters", "county": "St. Charles County", "lat": 38.7967, "lng": -90.6299, "population": 57732, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Blue Springs", "slug": "blue-springs", "county": "Jackson County", "lat": 39.0169, "lng": -94.2816, "population": 58604, "metro_area": "Kansas City", "region": "Midwest"},
            {"name": "Florissant", "slug": "florissant", "county": "St. Louis County", "lat": 38.7892, "lng": -90.3223, "population": 50497, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Joplin", "slug": "joplin", "county": "Jasper County", "lat": 37.0842, "lng": -94.5133, "population": 51762, "metro_area": "Joplin", "region": "Midwest"},
            {"name": "Chesterfield", "slug": "chesterfield", "county": "St. Louis County", "lat": 38.6631, "lng": -90.5770, "population": 49999, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Cape Girardeau", "slug": "cape-girardeau", "county": "Cape Girardeau County", "lat": 37.3058, "lng": -89.5181, "population": 39853, "metro_area": "Cape Girardeau", "region": "Midwest"},
            {"name": "Oakville", "slug": "oakville", "county": "St. Louis County", "lat": 38.5489, "lng": -90.3101, "population": 36143, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Wildwood", "slug": "wildwood", "county": "St. Louis County", "lat": 38.5906, "lng": -90.6579, "population": 35476, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "University City", "slug": "university-city", "county": "St. Louis County", "lat": 38.6667, "lng": -90.3151, "population": 34371, "metro_area": "St. Louis", "region": "Midwest"},
            {"name": "Jefferson City", "slug": "jefferson-city", "county": "Cole County", "lat": 38.5767, "lng": -92.1735, "population": 43228, "metro_area": "Jefferson City", "region": "Midwest"},
            {"name": "Raytown", "slug": "raytown", "county": "Jackson County", "lat": 38.9942, "lng": -94.4636, "population": 30601, "metro_area": "Kansas City", "region": "Midwest"}
        ]
    },

    # Kansas - Top 20 cities
    "kansas": {
        "name": "Kansas",
        "state_abbr": "KS",
        "cities": [
            {"name": "Wichita", "slug": "wichita", "county": "Sedgwick County", "lat": 37.6872, "lng": -97.3301, "population": 397532, "metro_area": "Wichita", "region": "Central"},
            {"name": "Overland Park", "slug": "overland-park", "county": "Johnson County", "lat": 38.9822, "lng": -94.6708, "population": 197238, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Kansas City", "slug": "kansas-city", "county": "Wyandotte County", "lat": 39.1142, "lng": -94.6275, "population": 152933, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Olathe", "slug": "olathe", "county": "Johnson County", "lat": 38.8814, "lng": -94.8191, "population": 147461, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Topeka", "slug": "topeka", "county": "Shawnee County", "lat": 39.0473, "lng": -95.6890, "population": 126587, "metro_area": "Topeka", "region": "Central"},
            {"name": "Lawrence", "slug": "lawrence", "county": "Douglas County", "lat": 38.9717, "lng": -95.2353, "population": 98193, "metro_area": "Lawrence", "region": "Central"},
            {"name": "Shawnee", "slug": "shawnee", "county": "Johnson County", "lat": 39.0228, "lng": -94.7202, "population": 67311, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Manhattan", "slug": "manhattan", "county": "Riley County", "lat": 39.1836, "lng": -96.5717, "population": 54100, "metro_area": "Manhattan", "region": "Central"},
            {"name": "Lenexa", "slug": "lenexa", "county": "Johnson County", "lat": 38.9536, "lng": -94.7336, "population": 57434, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Salina", "slug": "salina", "county": "Saline County", "lat": 38.8403, "lng": -97.6114, "population": 46889, "metro_area": "Salina", "region": "Central"},
            {"name": "Hutchinson", "slug": "hutchinson", "county": "Reno County", "lat": 38.0608, "lng": -97.9297, "population": 40006, "metro_area": "Hutchinson", "region": "Central"},
            {"name": "Leavenworth", "slug": "leavenworth", "county": "Leavenworth County", "lat": 39.3111, "lng": -94.9225, "population": 37351, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Leawood", "slug": "leawood", "county": "Johnson County", "lat": 38.9667, "lng": -94.6169, "population": 35811, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Dodge City", "slug": "dodge-city", "county": "Ford County", "lat": 37.7528, "lng": -100.0171, "population": 27788, "metro_area": "Dodge City", "region": "Central"},
            {"name": "Garden City", "slug": "garden-city", "county": "Finney County", "lat": 37.9717, "lng": -100.8729, "population": 28151, "metro_area": "Garden City", "region": "Central"},
            {"name": "Emporia", "slug": "emporia", "county": "Lyon County", "lat": 38.4039, "lng": -96.1817, "population": 24139, "metro_area": "Emporia", "region": "Central"},
            {"name": "Junction City", "slug": "junction-city", "county": "Geary County", "lat": 39.0292, "lng": -96.8317, "population": 22932, "metro_area": "Manhattan", "region": "Central"},
            {"name": "Derby", "slug": "derby", "county": "Sedgwick County", "lat": 37.5451, "lng": -97.2689, "population": 25625, "metro_area": "Wichita", "region": "Central"},
            {"name": "Prairie Village", "slug": "prairie-village", "county": "Johnson County", "lat": 38.9917, "lng": -94.6358, "population": 22957, "metro_area": "Kansas City", "region": "Central"},
            {"name": "Hays", "slug": "hays", "county": "Ellis County", "lat": 38.8792, "lng": -99.3267, "population": 21116, "metro_area": "Hays", "region": "Central"}
        ]
    },

    # Nebraska - Top 20 cities
    "nebraska": {
        "name": "Nebraska",
        "state_abbr": "NE",
        "cities": [
            {"name": "Omaha", "slug": "omaha", "county": "Douglas County", "lat": 41.2565, "lng": -95.9345, "population": 483335, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "Lincoln", "slug": "lincoln", "county": "Lancaster County", "lat": 40.8136, "lng": -96.7026, "population": 294757, "metro_area": "Lincoln", "region": "Central"},
            {"name": "Bellevue", "slug": "bellevue", "county": "Sarpy County", "lat": 41.1369, "lng": -95.9169, "population": 63922, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "Grand Island", "slug": "grand-island", "county": "Hall County", "lat": 40.9250, "lng": -98.3420, "population": 52622, "metro_area": "Grand Island", "region": "Central"},
            {"name": "Kearney", "slug": "kearney", "county": "Buffalo County", "lat": 40.6994, "lng": -99.0817, "population": 34362, "metro_area": "Kearney", "region": "Central"},
            {"name": "Fremont", "slug": "fremont", "county": "Dodge County", "lat": 41.4331, "lng": -96.4981, "population": 27141, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "Hastings", "slug": "hastings", "county": "Adams County", "lat": 40.5861, "lng": -98.3887, "population": 25152, "metro_area": "Hastings", "region": "Central"},
            {"name": "North Platte", "slug": "north-platte", "county": "Lincoln County", "lat": 41.1400, "lng": -100.7601, "population": 23390, "metro_area": "North Platte", "region": "Central"},
            {"name": "Norfolk", "slug": "norfolk", "county": "Madison County", "lat": 42.0281, "lng": -97.4170, "population": 24210, "metro_area": "Norfolk", "region": "Central"},
            {"name": "Columbus", "slug": "columbus", "county": "Platte County", "lat": 41.4294, "lng": -97.3686, "population": 24028, "metro_area": "Columbus", "region": "Central"},
            {"name": "Papillion", "slug": "papillion", "county": "Sarpy County", "lat": 41.1544, "lng": -96.0428, "population": 25579, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "La Vista", "slug": "la-vista", "county": "Sarpy County", "lat": 41.1833, "lng": -96.0331, "population": 17081, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "Scottsbluff", "slug": "scottsbluff", "county": "Scotts Bluff County", "lat": 41.8669, "lng": -103.6672, "population": 14436, "metro_area": "Scottsbluff", "region": "Central"},
            {"name": "South Sioux City", "slug": "south-sioux-city", "county": "Dakota County", "lat": 42.4583, "lng": -96.4142, "population": 12867, "metro_area": "Sioux City", "region": "Central"},
            {"name": "Beatrice", "slug": "beatrice", "county": "Gage County", "lat": 40.2681, "lng": -96.7472, "population": 12459, "metro_area": "Beatrice", "region": "Central"},
            {"name": "Chalco", "slug": "chalco", "county": "Sarpy County", "lat": 41.2144, "lng": -96.1219, "population": 11064, "metro_area": "Omaha-Council Bluffs", "region": "Central"},
            {"name": "York", "slug": "york", "county": "York County", "lat": 40.8672, "lng": -97.5920, "population": 7918, "metro_area": "York", "region": "Central"},
            {"name": "McCook", "slug": "mccook", "county": "Red Willow County", "lat": 40.2058, "lng": -100.6251, "population": 7631, "metro_area": "McCook", "region": "Central"},
            {"name": "Nebraska City", "slug": "nebraska-city", "county": "Otoe County", "lat": 40.6775, "lng": -95.8597, "population": 7222, "metro_area": "Nebraska City", "region": "Central"},
            {"name": "Alliance", "slug": "alliance", "county": "Box Butte County", "lat": 42.1017, "lng": -102.8704, "population": 8491, "metro_area": "Alliance", "region": "Central"}
        ]
    },

    # North Dakota - Top 20 cities
    "north-dakota": {
        "name": "North Dakota",
        "state_abbr": "ND",
        "cities": [
            {"name": "Fargo", "slug": "fargo", "county": "Cass County", "lat": 46.8772, "lng": -96.7898, "population": 137989, "metro_area": "Fargo", "region": "Central"},
            {"name": "Bismarck", "slug": "bismarck", "county": "Burleigh County", "lat": 46.8083, "lng": -100.7837, "population": 75092, "metro_area": "Bismarck", "region": "Central"},
            {"name": "Grand Forks", "slug": "grand-forks", "county": "Grand Forks County", "lat": 47.9253, "lng": -97.0329, "population": 58206, "metro_area": "Grand Forks", "region": "Central"},
            {"name": "Minot", "slug": "minot", "county": "Ward County", "lat": 48.2330, "lng": -101.2957, "population": 47373, "metro_area": "Minot", "region": "Central"},
            {"name": "West Fargo", "slug": "west-fargo", "county": "Cass County", "lat": 46.8747, "lng": -96.9003, "population": 40400, "metro_area": "Fargo", "region": "Central"},
            {"name": "Williston", "slug": "williston", "county": "Williams County", "lat": 48.1470, "lng": -103.6183, "population": 29160, "metro_area": "Williston", "region": "Central"},
            {"name": "Dickinson", "slug": "dickinson", "county": "Stark County", "lat": 46.8792, "lng": -102.7896, "population": 25679, "metro_area": "Dickinson", "region": "Central"},
            {"name": "Mandan", "slug": "mandan", "county": "Morton County", "lat": 46.8267, "lng": -100.8896, "population": 24206, "metro_area": "Bismarck", "region": "Central"},
            {"name": "Jamestown", "slug": "jamestown", "county": "Stutsman County", "lat": 46.9108, "lng": -98.7084, "population": 15849, "metro_area": "Jamestown", "region": "Central"},
            {"name": "Wahpeton", "slug": "wahpeton", "county": "Richland County", "lat": 46.2652, "lng": -96.6059, "population": 7984, "metro_area": "Wahpeton", "region": "Central"},
            {"name": "Devils Lake", "slug": "devils-lake", "county": "Ramsey County", "lat": 48.1128, "lng": -98.8648, "population": 7192, "metro_area": "Devils Lake", "region": "Central"},
            {"name": "Valley City", "slug": "valley-city", "county": "Barnes County", "lat": 46.9233, "lng": -98.0037, "population": 6314, "metro_area": "Valley City", "region": "Central"},
            {"name": "Grafton", "slug": "grafton", "county": "Walsh County", "lat": 48.4069, "lng": -97.4112, "population": 4284, "metro_area": "Grafton", "region": "Central"},
            {"name": "Watford City", "slug": "watford-city", "county": "McKenzie County", "lat": 47.8014, "lng": -103.2832, "population": 6207, "metro_area": "Watford City", "region": "Central"},
            {"name": "Harvey", "slug": "harvey", "county": "Wells County", "lat": 47.7719, "lng": -99.9354, "population": 1783, "metro_area": "Harvey", "region": "Central"},
            {"name": "Beulah", "slug": "beulah", "county": "Mercer County", "lat": 47.2642, "lng": -101.7787, "population": 3094, "metro_area": "Beulah", "region": "Central"},
            {"name": "Rugby", "slug": "rugby", "county": "Pierce County", "lat": 48.3689, "lng": -99.9987, "population": 2509, "metro_area": "Rugby", "region": "Central"},
            {"name": "Horace", "slug": "horace", "county": "Cass County", "lat": 46.7608, "lng": -96.9061, "population": 3085, "metro_area": "Fargo", "region": "Central"},
            {"name": "New Town", "slug": "new-town", "county": "Mountrail County", "lat": 47.9889, "lng": -102.4918, "population": 2715, "metro_area": "New Town", "region": "Central"},
            {"name": "Carrington", "slug": "carrington", "county": "Foster County", "lat": 47.4492, "lng": -99.1262, "population": 1854, "metro_area": "Carrington", "region": "Central"}
        ]
    },

    # South Dakota - Top 20 cities
    "south-dakota": {
        "name": "South Dakota",
        "state_abbr": "SD",
        "cities": [
            {"name": "Sioux Falls", "slug": "sioux-falls", "county": "Minnehaha County", "lat": 43.5446, "lng": -96.7311, "population": 215058, "metro_area": "Sioux Falls", "region": "Central"},
            {"name": "Rapid City", "slug": "rapid-city", "county": "Pennington County", "lat": 44.0805, "lng": -103.2310, "population": 79404, "metro_area": "Rapid City", "region": "Central"},
            {"name": "Aberdeen", "slug": "aberdeen", "county": "Brown County", "lat": 45.4647, "lng": -98.4865, "population": 28110, "metro_area": "Aberdeen", "region": "Central"},
            {"name": "Brookings", "slug": "brookings", "county": "Brookings County", "lat": 44.3114, "lng": -96.7984, "population": 24312, "metro_area": "Brookings", "region": "Central"},
            {"name": "Watertown", "slug": "watertown", "county": "Codington County", "lat": 44.8997, "lng": -97.1148, "population": 23230, "metro_area": "Watertown", "region": "Central"},
            {"name": "Mitchell", "slug": "mitchell", "county": "Davison County", "lat": 43.7094, "lng": -98.0298, "population": 15660, "metro_area": "Mitchell", "region": "Central"},
            {"name": "Yankton", "slug": "yankton", "county": "Yankton County", "lat": 42.8711, "lng": -97.3973, "population": 14454, "metro_area": "Yankton", "region": "Central"},
            {"name": "Pierre", "slug": "pierre", "county": "Hughes County", "lat": 44.3683, "lng": -100.3510, "population": 14091, "metro_area": "Pierre", "region": "Central"},
            {"name": "Huron", "slug": "huron", "county": "Beadle County", "lat": 44.3633, "lng": -98.2142, "population": 13000, "metro_area": "Huron", "region": "Central"},
            {"name": "Spearfish", "slug": "spearfish", "county": "Lawrence County", "lat": 44.4906, "lng": -103.8593, "population": 12193, "metro_area": "Rapid City", "region": "Central"},
            {"name": "Vermillion", "slug": "vermillion", "county": "Clay County", "lat": 42.7794, "lng": -96.9289, "population": 11695, "metro_area": "Vermillion", "region": "Central"},
            {"name": "Brandon", "slug": "brandon", "county": "Minnehaha County", "lat": 43.5878, "lng": -96.5814, "population": 11048, "metro_area": "Sioux Falls", "region": "Central"},
            {"name": "Hot Springs", "slug": "hot-springs", "county": "Fall River County", "lat": 43.4319, "lng": -103.4740, "population": 3633, "metro_area": "Hot Springs", "region": "Central"},
            {"name": "Lead", "slug": "lead", "county": "Lawrence County", "lat": 44.3522, "lng": -103.7649, "population": 3016, "metro_area": "Rapid City", "region": "Central"},
            {"name": "Sturgis", "slug": "sturgis", "county": "Meade County", "lat": 44.4097, "lng": -103.5088, "population": 7020, "metro_area": "Rapid City", "region": "Central"},
            {"name": "Belle Fourche", "slug": "belle-fourche", "county": "Butte County", "lat": 44.6714, "lng": -103.8521, "population": 5594, "metro_area": "Belle Fourche", "region": "Central"},
            {"name": "Madison", "slug": "madison", "county": "Lake County", "lat": 44.0061, "lng": -97.1134, "population": 6191, "metro_area": "Madison", "region": "Central"},
            {"name": "Winner", "slug": "winner", "county": "Tripp County", "lat": 43.3764, "lng": -99.8593, "population": 2897, "metro_area": "Winner", "region": "Central"},
            {"name": "Deadwood", "slug": "deadwood", "county": "Lawrence County", "lat": 44.3769, "lng": -103.7291, "population": 1271, "metro_area": "Rapid City", "region": "Central"},
            {"name": "Milbank", "slug": "milbank", "county": "Grant County", "lat": 45.2172, "lng": -96.6267, "population": 3149, "metro_area": "Milbank", "region": "Central"}
        ]
    }
}

# Helper functions to get data
def get_state_cities(state_slug):
    """Get all cities for a specific state"""
    return MIDWEST_CENTRAL_CITIES.get(state_slug, {}).get('cities', [])

def get_city_data(state_slug, city_slug):
    """Get specific city data"""
    state_data = MIDWEST_CENTRAL_CITIES.get(state_slug)
    if not state_data:
        return None
    
    for city in state_data['cities']:
        if city['slug'] == city_slug:
            return city
    return None

def get_all_cities():
    """Get all cities from all Midwest/Central states"""
    all_cities = []
    for state_slug, state_data in MIDWEST_CENTRAL_CITIES.items():
        for city in state_data['cities']:
            city_with_state = city.copy()
            city_with_state['state'] = state_slug
            city_with_state['state_name'] = state_data['name']
            city_with_state['state_abbr'] = state_data['state_abbr']
            all_cities.append(city_with_state)
    return all_cities

# Statistics
TOTAL_STATES = len(MIDWEST_CENTRAL_CITIES)
TOTAL_CITIES = sum(len(state['cities']) for state in MIDWEST_CENTRAL_CITIES.values())

print(f"Midwest/Central Dataset Statistics:")
print(f"States: {TOTAL_STATES}")
print(f"Total Cities: {TOTAL_CITIES}")
print(f"Average Cities per State: {TOTAL_CITIES / TOTAL_STATES:.1f}")