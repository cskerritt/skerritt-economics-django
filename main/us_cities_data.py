"""
US Cities Data - Top 15 cities per state for landing pages
"""

US_STATES = {
    "AL": {"name": "Alabama", "cities": ["Birmingham", "Montgomery", "Huntsville", "Mobile", "Tuscaloosa", "Hoover", "Dothan", "Auburn", "Decatur", "Madison", "Florence", "Gadsden", "Prattville", "Vestavia Hills", "Phenix City"]},
    "AK": {"name": "Alaska", "cities": ["Anchorage", "Fairbanks", "Juneau", "Sitka", "Ketchikan", "Wasilla", "Kenai", "Kodiak", "Bethel", "Palmer", "Homer", "Unalaska", "Barrow", "Soldotna", "Valdez"]},
    "AZ": {"name": "Arizona", "cities": ["Phoenix", "Tucson", "Mesa", "Chandler", "Scottsdale", "Glendale", "Gilbert", "Tempe", "Peoria", "Surprise", "Yuma", "Avondale", "Goodyear", "Flagstaff", "Buckeye"]},
    "AR": {"name": "Arkansas", "cities": ["Little Rock", "Fort Smith", "Fayetteville", "Springdale", "Jonesboro", "North Little Rock", "Conway", "Rogers", "Pine Bluff", "Bentonville", "Hot Springs", "Benton", "Texarkana", "Sherwood", "Jacksonville"]},
    "CA": {"name": "California", "cities": ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno", "Sacramento", "Long Beach", "Oakland", "Bakersfield", "Anaheim", "Santa Ana", "Riverside", "Stockton", "Irvine", "Chula Vista"]},
    "CO": {"name": "Colorado", "cities": ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Lakewood", "Thornton", "Arvada", "Westminster", "Pueblo", "Centennial", "Boulder", "Greeley", "Longmont", "Loveland", "Grand Junction"]},
    "CT": {"name": "Connecticut", "cities": ["Bridgeport", "New Haven", "Hartford", "Stamford", "Waterbury", "Norwalk", "Danbury", "New Britain", "Bristol", "Meriden", "Milford", "West Haven", "Middletown", "Norwich", "Shelton"]},
    "DE": {"name": "Delaware", "cities": ["Wilmington", "Dover", "Newark", "Middletown", "Smyrna", "Milford", "Seaford", "Georgetown", "Elsmere", "New Castle", "Millsboro", "Laurel", "Harrington", "Camden", "Clayton"]},
    "FL": {"name": "Florida", "cities": ["Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg", "Hialeah", "Tallahassee", "Fort Lauderdale", "Port St. Lucie", "Cape Coral", "Pembroke Pines", "Hollywood", "Miramar", "Gainesville", "Coral Springs"]},
    "GA": {"name": "Georgia", "cities": ["Atlanta", "Augusta", "Columbus", "Macon", "Savannah", "Athens", "Sandy Springs", "Roswell", "Albany", "Johns Creek", "Warner Robins", "Alpharetta", "Marietta", "Valdosta", "Smyrna"]},
    "HI": {"name": "Hawaii", "cities": ["Honolulu", "Pearl City", "Hilo", "Kailua", "Waipahu", "Kaneohe", "Mililani", "Kahului", "Ewa Beach", "Kihei", "Mililani Mauka", "Makakilo", "Wahiawa", "Wailuku", "Kapolei"]},
    "ID": {"name": "Idaho", "cities": ["Boise", "Meridian", "Nampa", "Idaho Falls", "Pocatello", "Caldwell", "Coeur d'Alene", "Twin Falls", "Lewiston", "Post Falls", "Rexburg", "Moscow", "Eagle", "Kuna", "Ammon"]},
    "IL": {"name": "Illinois", "cities": ["Chicago", "Aurora", "Rockford", "Joliet", "Naperville", "Springfield", "Peoria", "Elgin", "Waukegan", "Cicero", "Champaign", "Bloomington", "Arlington Heights", "Evanston", "Decatur"]},
    "IN": {"name": "Indiana", "cities": ["Indianapolis", "Fort Wayne", "Evansville", "South Bend", "Carmel", "Fishers", "Bloomington", "Hammond", "Gary", "Lafayette", "Muncie", "Terre Haute", "Kokomo", "Anderson", "Noblesville"]},
    "IA": {"name": "Iowa", "cities": ["Des Moines", "Cedar Rapids", "Davenport", "Sioux City", "Waterloo", "Iowa City", "Council Bluffs", "Ames", "Dubuque", "West Des Moines", "Ankeny", "Urbandale", "Cedar Falls", "Marion", "Bettendorf"]},
    "KS": {"name": "Kansas", "cities": ["Wichita", "Overland Park", "Kansas City", "Olathe", "Topeka", "Lawrence", "Shawnee", "Manhattan", "Lenexa", "Salina", "Hutchinson", "Leavenworth", "Leawood", "Dodge City", "Garden City"]},
    "KY": {"name": "Kentucky", "cities": ["Louisville", "Lexington", "Bowling Green", "Owensboro", "Covington", "Hopkinsville", "Richmond", "Florence", "Georgetown", "Henderson", "Elizabethtown", "Nicholasville", "Jeffersontown", "Frankfort", "Paducah"]},
    "LA": {"name": "Louisiana", "cities": ["New Orleans", "Baton Rouge", "Shreveport", "Lafayette", "Lake Charles", "Kenner", "Bossier City", "Monroe", "Alexandria", "Houma", "New Iberia", "Laplace", "Slidell", "Prairieville", "Central"]},
    "ME": {"name": "Maine", "cities": ["Portland", "Lewiston", "Bangor", "South Portland", "Auburn", "Biddeford", "Sanford", "Saco", "Augusta", "Westbrook", "Waterville", "Presque Isle", "Brewer", "Bath", "Caribou"]},
    "MD": {"name": "Maryland", "cities": ["Baltimore", "Frederick", "Rockville", "Gaithersburg", "Bowie", "Hagerstown", "Annapolis", "College Park", "Salisbury", "Laurel", "Greenbelt", "Cumberland", "Westminster", "Hyattsville", "Takoma Park"]},
    "MA": {"name": "Massachusetts", "cities": ["Boston", "Worcester", "Springfield", "Cambridge", "Lowell", "Brockton", "Quincy", "Lynn", "New Bedford", "Newton", "Fall River", "Somerville", "Lawrence", "Framingham", "Haverhill"]},
    "MI": {"name": "Michigan", "cities": ["Detroit", "Grand Rapids", "Warren", "Sterling Heights", "Ann Arbor", "Lansing", "Flint", "Dearborn", "Livonia", "Troy", "Westland", "Farmington Hills", "Kalamazoo", "Wyoming", "Southfield"]},
    "MN": {"name": "Minnesota", "cities": ["Minneapolis", "St. Paul", "Rochester", "Duluth", "Bloomington", "Brooklyn Park", "Plymouth", "St. Cloud", "Eagan", "Woodbury", "Maple Grove", "Eden Prairie", "Coon Rapids", "Burnsville", "Blaine"]},
    "MS": {"name": "Mississippi", "cities": ["Jackson", "Gulfport", "Southaven", "Biloxi", "Hattiesburg", "Meridian", "Tupelo", "Greenville", "Olive Branch", "Horn Lake", "Clinton", "Pearl", "Madison", "Starkville", "Ridgeland"]},
    "MO": {"name": "Missouri", "cities": ["Kansas City", "St. Louis", "Springfield", "Columbia", "Independence", "Lee's Summit", "O'Fallon", "St. Joseph", "St. Charles", "St. Peters", "Blue Springs", "Florissant", "Joplin", "Chesterfield", "Jefferson City"]},
    "MT": {"name": "Montana", "cities": ["Billings", "Missoula", "Great Falls", "Bozeman", "Butte", "Helena", "Kalispell", "Havre", "Anaconda", "Miles City", "Belgrade", "Livingston", "Laurel", "Whitefish", "Lewistown"]},
    "NE": {"name": "Nebraska", "cities": ["Omaha", "Lincoln", "Bellevue", "Grand Island", "Kearney", "Fremont", "Hastings", "Norfolk", "North Platte", "Columbus", "Papillion", "La Vista", "Scottsbluff", "South Sioux City", "Beatrice"]},
    "NV": {"name": "Nevada", "cities": ["Las Vegas", "Henderson", "Reno", "North Las Vegas", "Sparks", "Carson City", "Fernley", "Elko", "Mesquite", "Boulder City", "Fallon", "Winnemucca", "West Wendover", "Ely", "Yerington"]},
    "NH": {"name": "New Hampshire", "cities": ["Manchester", "Nashua", "Concord", "Derry", "Dover", "Rochester", "Salem", "Merrimack", "Hudson", "Londonderry", "Keene", "Bedford", "Portsmouth", "Goffstown", "Laconia"]},
    "NJ": {"name": "New Jersey", "cities": ["Newark", "Jersey City", "Paterson", "Elizabeth", "Edison", "Woodbridge", "Lakewood", "Toms River", "Hamilton", "Trenton", "Clifton", "Camden", "Brick", "Cherry Hill", "Passaic"]},
    "NM": {"name": "New Mexico", "cities": ["Albuquerque", "Las Cruces", "Rio Rancho", "Santa Fe", "Roswell", "Farmington", "Clovis", "Hobbs", "Alamogordo", "Carlsbad", "Gallup", "Los Alamos", "Deming", "Chaparral", "Artesia"]},
    "NY": {"name": "New York", "cities": ["New York City", "Buffalo", "Rochester", "Yonkers", "Syracuse", "Albany", "New Rochelle", "Mount Vernon", "Schenectady", "Utica", "White Plains", "Hempstead", "Troy", "Niagara Falls", "Binghamton"]},
    "NC": {"name": "North Carolina", "cities": ["Charlotte", "Raleigh", "Greensboro", "Durham", "Winston-Salem", "Fayetteville", "Cary", "Wilmington", "High Point", "Concord", "Greenville", "Asheville", "Gastonia", "Jacksonville", "Chapel Hill"]},
    "ND": {"name": "North Dakota", "cities": ["Fargo", "Bismarck", "Grand Forks", "Minot", "West Fargo", "Dickinson", "Mandan", "Williston", "Jamestown", "Wahpeton", "Devils Lake", "Valley City", "Grafton", "Lincoln", "Beulah"]},
    "OH": {"name": "Ohio", "cities": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron", "Dayton", "Parma", "Canton", "Youngstown", "Lorain", "Hamilton", "Springfield", "Kettering", "Elyria", "Lakewood"]},
    "OK": {"name": "Oklahoma", "cities": ["Oklahoma City", "Tulsa", "Norman", "Broken Arrow", "Lawton", "Edmond", "Moore", "Midwest City", "Enid", "Stillwater", "Muskogee", "Bartlesville", "Owasso", "Shawnee", "Ponca City"]},
    "OR": {"name": "Oregon", "cities": ["Portland", "Eugene", "Salem", "Gresham", "Hillsboro", "Beaverton", "Bend", "Medford", "Springfield", "Corvallis", "Albany", "Tigard", "Lake Oswego", "Keizer", "Grants Pass"]},
    "PA": {"name": "Pennsylvania", "cities": ["Philadelphia", "Pittsburgh", "Allentown", "Erie", "Reading", "Scranton", "Bethlehem", "Lancaster", "Harrisburg", "Altoona", "York", "State College", "Wilkes-Barre", "Chester", "Williamsport"]},
    "RI": {"name": "Rhode Island", "cities": ["Providence", "Warwick", "Cranston", "Pawtucket", "East Providence", "Woonsocket", "Newport", "Central Falls", "Westerly", "Valley Falls", "Bristol", "Smithfield", "Lincoln", "North Providence", "West Warwick"]},
    "SC": {"name": "South Carolina", "cities": ["Columbia", "Charleston", "North Charleston", "Mount Pleasant", "Rock Hill", "Greenville", "Summerville", "Sumter", "Goose Creek", "Hilton Head Island", "Florence", "Spartanburg", "Myrtle Beach", "Aiken", "Anderson"]},
    "SD": {"name": "South Dakota", "cities": ["Sioux Falls", "Rapid City", "Aberdeen", "Brookings", "Watertown", "Mitchell", "Yankton", "Pierre", "Huron", "Vermillion", "Spearfish", "Brandon", "Box Elder", "Madison", "Sturgis"]},
    "TN": {"name": "Tennessee", "cities": ["Nashville", "Memphis", "Knoxville", "Chattanooga", "Clarksville", "Murfreesboro", "Jackson", "Franklin", "Johnson City", "Bartlett", "Hendersonville", "Kingsport", "Smyrna", "Cleveland", "Brentwood"]},
    "TX": {"name": "Texas", "cities": ["Houston", "San Antonio", "Dallas", "Austin", "Fort Worth", "El Paso", "Arlington", "Corpus Christi", "Plano", "Laredo", "Lubbock", "Garland", "Irving", "Amarillo", "Grand Prairie"]},
    "UT": {"name": "Utah", "cities": ["Salt Lake City", "West Valley City", "Provo", "West Jordan", "Orem", "Sandy", "Ogden", "St. George", "Layton", "Taylorsville", "South Jordan", "Lehi", "Logan", "Murray", "Draper"]},
    "VT": {"name": "Vermont", "cities": ["Burlington", "South Burlington", "Rutland", "Barre", "Montpelier", "St. Johnsbury", "Brattleboro", "Bennington", "Essex Junction", "Milton", "St. Albans", "Morristown", "Lyndonville", "Middlebury", "Swanton"]},
    "VA": {"name": "Virginia", "cities": ["Virginia Beach", "Norfolk", "Chesapeake", "Richmond", "Newport News", "Alexandria", "Hampton", "Roanoke", "Portsmouth", "Suffolk", "Lynchburg", "Harrisonburg", "Charlottesville", "Danville", "Manassas"]},
    "WA": {"name": "Washington", "cities": ["Seattle", "Spokane", "Tacoma", "Vancouver", "Bellevue", "Kent", "Everett", "Renton", "Yakima", "Federal Way", "Spokane Valley", "Bellingham", "Kennewick", "Auburn", "Pasco"]},
    "WV": {"name": "West Virginia", "cities": ["Charleston", "Huntington", "Morgantown", "Parkersburg", "Wheeling", "Weirton", "Fairmont", "Beckley", "Martinsburg", "Clarksburg", "South Charleston", "St. Albans", "Vienna", "Bluefield", "Moundsville"]},
    "WI": {"name": "Wisconsin", "cities": ["Milwaukee", "Madison", "Green Bay", "Kenosha", "Racine", "Appleton", "Waukesha", "Eau Claire", "Oshkosh", "Janesville", "West Allis", "La Crosse", "Sheboygan", "Wauwatosa", "Fond du Lac"]},
    "WY": {"name": "Wyoming", "cities": ["Cheyenne", "Casper", "Laramie", "Gillette", "Rock Springs", "Sheridan", "Green River", "Evanston", "Riverton", "Jackson", "Cody", "Rawlins", "Lander", "Torrington", "Powell"]},
}

# Expanded Practice Areas for Forensic Economic Damages
PRACTICE_AREAS = [
    # Personal Injury
    {"slug": "personal-injury", "name": "Personal Injury", "description": "Economic damages in personal injury cases"},
    {"slug": "wrongful-death", "name": "Wrongful Death", "description": "Economic loss calculations for wrongful death cases"},
    {"slug": "catastrophic-injury", "name": "Catastrophic Injury", "description": "Life care planning and future cost projections"},
    {"slug": "traumatic-brain-injury", "name": "Traumatic Brain Injury", "description": "Economic impact of TBI cases"},
    {"slug": "spinal-cord-injury", "name": "Spinal Cord Injury", "description": "Lifetime care costs and lost earnings"},
    
    # Medical
    {"slug": "medical-malpractice", "name": "Medical Malpractice", "description": "Economic damages from medical negligence"},
    {"slug": "birth-injury", "name": "Birth Injury", "description": "Lifetime economic impact of birth injuries"},
    {"slug": "nursing-home-abuse", "name": "Nursing Home Abuse", "description": "Economic damages in elder abuse cases"},
    {"slug": "pharmaceutical-liability", "name": "Pharmaceutical Liability", "description": "Economic losses from defective drugs"},
    {"slug": "medical-device-failure", "name": "Medical Device Failure", "description": "Economic impact of defective medical devices"},
    
    # Employment
    {"slug": "employment-discrimination", "name": "Employment Discrimination", "description": "Lost earnings from workplace discrimination"},
    {"slug": "wrongful-termination", "name": "Wrongful Termination", "description": "Economic losses from wrongful termination"},
    {"slug": "sexual-harassment", "name": "Sexual Harassment", "description": "Economic damages in harassment cases"},
    {"slug": "wage-hour-disputes", "name": "Wage & Hour Disputes", "description": "Unpaid wages and overtime calculations"},
    {"slug": "breach-of-contract", "name": "Breach of Employment Contract", "description": "Economic losses from contract violations"},
    
    # Business
    {"slug": "business-interruption", "name": "Business Interruption", "description": "Lost profits from business disruption"},
    {"slug": "commercial-disputes", "name": "Commercial Disputes", "description": "Economic damages in business litigation"},
    {"slug": "intellectual-property", "name": "Intellectual Property", "description": "Economic damages from IP infringement"},
    {"slug": "partnership-disputes", "name": "Partnership Disputes", "description": "Business valuation in partner conflicts"},
    {"slug": "shareholder-disputes", "name": "Shareholder Disputes", "description": "Valuation for shareholder litigation"},
    {"slug": "unfair-competition", "name": "Unfair Competition", "description": "Economic losses from unfair business practices"},
    {"slug": "trade-secret-theft", "name": "Trade Secret Theft", "description": "Economic impact of trade secret misappropriation"},
    
    # Property
    {"slug": "construction-defects", "name": "Construction Defects", "description": "Economic losses from construction failures"},
    {"slug": "premises-liability", "name": "Premises Liability", "description": "Economic damages from property injuries"},
    {"slug": "environmental-damages", "name": "Environmental Damages", "description": "Economic impact of environmental harm"},
    {"slug": "eminent-domain", "name": "Eminent Domain", "description": "Just compensation valuations"},
    
    # Family Law
    {"slug": "divorce-valuation", "name": "Divorce Business Valuation", "description": "Business valuations for marital dissolution"},
    {"slug": "alimony-calculations", "name": "Alimony Calculations", "description": "Income analysis for support determinations"},
    {"slug": "marital-asset-valuation", "name": "Marital Asset Valuation", "description": "Valuation of marital estate assets"},
    
    # Product Liability
    {"slug": "product-liability", "name": "Product Liability", "description": "Economic damages from defective products"},
    {"slug": "automotive-defects", "name": "Automotive Defects", "description": "Economic losses from vehicle defects"},
    {"slug": "toxic-torts", "name": "Toxic Torts", "description": "Economic impact of toxic exposure"},
    {"slug": "mass-torts", "name": "Mass Torts", "description": "Economic analysis for mass tort litigation"},
    
    # Insurance
    {"slug": "bad-faith-insurance", "name": "Bad Faith Insurance", "description": "Economic damages from insurance bad faith"},
    {"slug": "insurance-coverage", "name": "Insurance Coverage Disputes", "description": "Economic loss quantification for coverage disputes"},
    {"slug": "disability-claims", "name": "Disability Claims", "description": "Economic analysis for disability benefits"},
    
    # Other
    {"slug": "civil-rights", "name": "Civil Rights Violations", "description": "Economic damages in civil rights cases"},
    {"slug": "class-action", "name": "Class Action Damages", "description": "Economic analysis for class action suits"},
    {"slug": "probate-litigation", "name": "Probate Litigation", "description": "Estate and trust valuations"},
    {"slug": "professional-malpractice", "name": "Professional Malpractice", "description": "Economic losses from professional negligence"},
]

def get_city_slug(city, state_abbr):
    """Generate URL-friendly slug for city"""
    city_clean = city.lower().replace(" ", "-").replace(".", "").replace("'", "")
    return f"{city_clean}-{state_abbr.lower()}"

def get_all_city_urls():
    """Generate all city URLs for sitemap"""
    urls = []
    services = ["forensic-economist", "business-valuation"]
    
    for state_abbr, state_data in US_STATES.items():
        for city in state_data["cities"]:
            city_slug = get_city_slug(city, state_abbr)
            for service in services:
                urls.append(f"/locations/{service}/{city_slug}.html")
    
    return urls