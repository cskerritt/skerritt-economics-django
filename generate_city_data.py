#!/usr/bin/env python
"""
Generate comprehensive city data for all 50 US states
"""

# Complete city data for all 50 states with top 10 cities each
ALL_STATES_DATA = {
    'alabama': {'name': 'Alabama', 'abbr': 'AL', 'cities': ['Birmingham', 'Montgomery', 'Huntsville', 'Mobile', 'Tuscaloosa', 'Hoover', 'Dothan', 'Auburn', 'Decatur', 'Madison']},
    'alaska': {'name': 'Alaska', 'abbr': 'AK', 'cities': ['Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan', 'Wasilla', 'Kenai', 'Kodiak', 'Bethel', 'Palmer']},
    'arizona': {'name': 'Arizona', 'abbr': 'AZ', 'cities': ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Scottsdale', 'Glendale', 'Gilbert', 'Tempe', 'Peoria', 'Surprise']},
    'arkansas': {'name': 'Arkansas', 'abbr': 'AR', 'cities': ['Little Rock', 'Fort Smith', 'Fayetteville', 'Springdale', 'Jonesboro', 'North Little Rock', 'Conway', 'Rogers', 'Pine Bluff', 'Bentonville']},
    'california': {'name': 'California', 'abbr': 'CA', 'cities': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim']},
    'colorado': {'name': 'Colorado', 'abbr': 'CO', 'cities': ['Denver', 'Colorado Springs', 'Aurora', 'Fort Collins', 'Lakewood', 'Thornton', 'Arvada', 'Westminster', 'Pueblo', 'Centennial']},
    'connecticut': {'name': 'Connecticut', 'abbr': 'CT', 'cities': ['Bridgeport', 'New Haven', 'Stamford', 'Hartford', 'Waterbury', 'Norwalk', 'Danbury', 'New Britain', 'Bristol', 'Meriden']},
    'delaware': {'name': 'Delaware', 'abbr': 'DE', 'cities': ['Wilmington', 'Dover', 'Newark', 'Middletown', 'Smyrna', 'Milford', 'Seaford', 'Georgetown', 'Elsmere', 'New Castle']},
    'florida': {'name': 'Florida', 'abbr': 'FL', 'cities': ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St Petersburg', 'Hialeah', 'Tallahassee', 'Fort Lauderdale', 'Port St Lucie', 'Cape Coral']},
    'georgia': {'name': 'Georgia', 'abbr': 'GA', 'cities': ['Atlanta', 'Augusta', 'Columbus', 'Macon', 'Savannah', 'Athens', 'Sandy Springs', 'Roswell', 'Albany', 'Johns Creek']},
    'hawaii': {'name': 'Hawaii', 'abbr': 'HI', 'cities': ['Honolulu', 'Pearl City', 'Hilo', 'Kailua', 'Waipahu', 'Kaneohe', 'Kahului', 'Ewa Beach', 'Mililani', 'Kihei']},
    'idaho': {'name': 'Idaho', 'abbr': 'ID', 'cities': ['Boise', 'Meridian', 'Nampa', 'Idaho Falls', 'Pocatello', 'Caldwell', 'Coeur d\'Alene', 'Twin Falls', 'Lewiston', 'Post Falls']},
    'illinois': {'name': 'Illinois', 'abbr': 'IL', 'cities': ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville', 'Springfield', 'Peoria', 'Elgin', 'Waukegan', 'Cicero']},
    'indiana': {'name': 'Indiana', 'abbr': 'IN', 'cities': ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend', 'Carmel', 'Fishers', 'Bloomington', 'Hammond', 'Gary', 'Lafayette']},
    'iowa': {'name': 'Iowa', 'abbr': 'IA', 'cities': ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City', 'Waterloo', 'Council Bluffs', 'Ames', 'Dubuque', 'West Des Moines']},
    'kansas': {'name': 'Kansas', 'abbr': 'KS', 'cities': ['Wichita', 'Overland Park', 'Kansas City', 'Olathe', 'Topeka', 'Lawrence', 'Shawnee', 'Manhattan', 'Lenexa', 'Salina']},
    'kentucky': {'name': 'Kentucky', 'abbr': 'KY', 'cities': ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington', 'Richmond', 'Georgetown', 'Florence', 'Hopkinsville', 'Nicholasville']},
    'louisiana': {'name': 'Louisiana', 'abbr': 'LA', 'cities': ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Lake Charles', 'Kenner', 'Bossier City', 'Monroe', 'Alexandria', 'Houma']},
    'maine': {'name': 'Maine', 'abbr': 'ME', 'cities': ['Portland', 'Lewiston', 'Bangor', 'South Portland', 'Auburn', 'Biddeford', 'Sanford', 'Augusta', 'Saco', 'Westbrook']},
    'maryland': {'name': 'Maryland', 'abbr': 'MD', 'cities': ['Baltimore', 'Columbia', 'Germantown', 'Silver Spring', 'Waldorf', 'Glen Burnie', 'Ellicott City', 'Frederick', 'Dundalk', 'Rockville']},
    'massachusetts': {'name': 'Massachusetts', 'abbr': 'MA', 'cities': ['Boston', 'Worcester', 'Springfield', 'Cambridge', 'Lowell', 'Brockton', 'New Bedford', 'Quincy', 'Lynn', 'Fall River']},
    'michigan': {'name': 'Michigan', 'abbr': 'MI', 'cities': ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Lansing', 'Ann Arbor', 'Flint', 'Dearborn', 'Livonia', 'Troy']},
    'minnesota': {'name': 'Minnesota', 'abbr': 'MN', 'cities': ['Minneapolis', 'St Paul', 'Rochester', 'Duluth', 'Bloomington', 'Brooklyn Park', 'Plymouth', 'St Cloud', 'Eagan', 'Woodbury']},
    'mississippi': {'name': 'Mississippi', 'abbr': 'MS', 'cities': ['Jackson', 'Gulfport', 'Southaven', 'Biloxi', 'Hattiesburg', 'Meridian', 'Tupelo', 'Olive Branch', 'Greenville', 'Horn Lake']},
    'missouri': {'name': 'Missouri', 'abbr': 'MO', 'cities': ['Kansas City', 'St Louis', 'Springfield', 'Columbia', 'Independence', 'Lee\'s Summit', 'O\'Fallon', 'St Joseph', 'St Charles', 'Blue Springs']},
    'montana': {'name': 'Montana', 'abbr': 'MT', 'cities': ['Billings', 'Missoula', 'Great Falls', 'Bozeman', 'Butte', 'Helena', 'Kalispell', 'Havre', 'Anaconda', 'Miles City']},
    'nebraska': {'name': 'Nebraska', 'abbr': 'NE', 'cities': ['Omaha', 'Lincoln', 'Bellevue', 'Grand Island', 'Kearney', 'Fremont', 'Hastings', 'Norfolk', 'North Platte', 'Columbus']},
    'nevada': {'name': 'Nevada', 'abbr': 'NV', 'cities': ['Las Vegas', 'Henderson', 'Reno', 'North Las Vegas', 'Sparks', 'Carson City', 'Fernley', 'Elko', 'Mesquite', 'Boulder City']},
    'new-hampshire': {'name': 'New Hampshire', 'abbr': 'NH', 'cities': ['Manchester', 'Nashua', 'Concord', 'Derry', 'Dover', 'Rochester', 'Salem', 'Merrimack', 'Hudson', 'Londonderry']},
    'new-jersey': {'name': 'New Jersey', 'abbr': 'NJ', 'cities': ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Edison', 'Woodbridge', 'Lakewood', 'Toms River', 'Hamilton', 'Trenton']},
    'new-mexico': {'name': 'New Mexico', 'abbr': 'NM', 'cities': ['Albuquerque', 'Las Cruces', 'Rio Rancho', 'Santa Fe', 'Roswell', 'Farmington', 'Clovis', 'Hobbs', 'Alamogordo', 'Carlsbad']},
    'new-york': {'name': 'New York', 'abbr': 'NY', 'cities': ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse', 'Albany', 'New Rochelle', 'Mount Vernon', 'Schenectady', 'Utica']},
    'north-carolina': {'name': 'North Carolina', 'abbr': 'NC', 'cities': ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem', 'Fayetteville', 'Cary', 'Wilmington', 'High Point', 'Concord']},
    'north-dakota': {'name': 'North Dakota', 'abbr': 'ND', 'cities': ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo', 'Williston', 'Dickinson', 'Mandan', 'Jamestown', 'Wahpeton']},
    'ohio': {'name': 'Ohio', 'abbr': 'OH', 'cities': ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron', 'Dayton', 'Parma', 'Canton', 'Youngstown', 'Lorain']},
    'oklahoma': {'name': 'Oklahoma', 'abbr': 'OK', 'cities': ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Edmond', 'Lawton', 'Moore', 'Midwest City', 'Enid', 'Stillwater']},
    'oregon': {'name': 'Oregon', 'abbr': 'OR', 'cities': ['Portland', 'Eugene', 'Salem', 'Gresham', 'Hillsboro', 'Beaverton', 'Bend', 'Medford', 'Springfield', 'Corvallis']},
    'pennsylvania': {'name': 'Pennsylvania', 'abbr': 'PA', 'cities': ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading', 'Scranton', 'Bethlehem', 'Lancaster', 'Harrisburg', 'Altoona']},
    'rhode-island': {'name': 'Rhode Island', 'abbr': 'RI', 'cities': ['Providence', 'Warwick', 'Cranston', 'Pawtucket', 'East Providence', 'Woonsocket', 'Newport', 'Central Falls', 'Westerly', 'Bristol']},
    'south-carolina': {'name': 'South Carolina', 'abbr': 'SC', 'cities': ['Columbia', 'Charleston', 'North Charleston', 'Mount Pleasant', 'Rock Hill', 'Greenville', 'Summerville', 'Sumter', 'Goose Creek', 'Hilton Head Island']},
    'south-dakota': {'name': 'South Dakota', 'abbr': 'SD', 'cities': ['Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Watertown', 'Mitchell', 'Yankton', 'Pierre', 'Huron', 'Vermillion']},
    'tennessee': {'name': 'Tennessee', 'abbr': 'TN', 'cities': ['Memphis', 'Nashville', 'Knoxville', 'Chattanooga', 'Clarksville', 'Murfreesboro', 'Franklin', 'Jackson', 'Johnson City', 'Bartlett']},
    'texas': {'name': 'Texas', 'abbr': 'TX', 'cities': ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington', 'Corpus Christi', 'Plano', 'Laredo']},
    'utah': {'name': 'Utah', 'abbr': 'UT', 'cities': ['Salt Lake City', 'West Valley City', 'Provo', 'West Jordan', 'Orem', 'Sandy', 'Ogden', 'St George', 'Layton', 'Taylorsville']},
    'vermont': {'name': 'Vermont', 'abbr': 'VT', 'cities': ['Burlington', 'South Burlington', 'Rutland', 'Barre', 'Montpelier', 'Winooski', 'St Albans', 'Newport', 'Vergennes', 'Middlebury']},
    'virginia': {'name': 'Virginia', 'abbr': 'VA', 'cities': ['Virginia Beach', 'Norfolk', 'Chesapeake', 'Richmond', 'Newport News', 'Alexandria', 'Hampton', 'Roanoke', 'Portsmouth', 'Suffolk']},
    'washington': {'name': 'Washington', 'abbr': 'WA', 'cities': ['Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Bellevue', 'Kent', 'Everett', 'Renton', 'Federal Way', 'Yakima']},
    'west-virginia': {'name': 'West Virginia', 'abbr': 'WV', 'cities': ['Charleston', 'Huntington', 'Morgantown', 'Parkersburg', 'Wheeling', 'Weirton', 'Fairmont', 'Beckley', 'Martinsburg', 'Clarksburg']},
    'wisconsin': {'name': 'Wisconsin', 'abbr': 'WI', 'cities': ['Milwaukee', 'Madison', 'Green Bay', 'Kenosha', 'Racine', 'Appleton', 'Waukesha', 'Eau Claire', 'Oshkosh', 'Janesville']},
    'wyoming': {'name': 'Wyoming', 'abbr': 'WY', 'cities': ['Cheyenne', 'Casper', 'Laramie', 'Gillette', 'Rock Springs', 'Sheridan', 'Green River', 'Evanston', 'Riverton', 'Jackson']},
}

def generate_city_data_file():
    """Generate the complete city data Python file"""
    
    output = '''"""
Comprehensive city data for all 50 US states
Generated for nationwide SEO coverage
"""

CITY_DATA = {
'''
    
    for state_slug, state_info in ALL_STATES_DATA.items():
        output += f"    '{state_slug}': {{\n"
        output += f"        'name': '{state_info['name']}',\n"
        output += f"        'abbr': '{state_info['abbr']}',\n"
        output += f"        'cities': [\n"
        
        for city_name in state_info['cities']:
            city_slug = city_name.lower().replace(' ', '-').replace("'", "")
            # Simple lat/lng approximation (would need real data in production)
            output += f"            {{'name': '{city_name}', 'slug': '{city_slug}', 'county': 'County'}},\n"
        
        output += f"        ]\n"
        output += f"    }},\n"
    
    output += "}\n"
    
    # Calculate total pages
    total_cities = sum(len(state['cities']) for state in ALL_STATES_DATA.values())
    services = 4  # forensic-economist, business-valuation, vocational-expert, life-care-planner
    total_pages = total_cities * services
    
    output += f'''
# Statistics:
# Total States: {len(ALL_STATES_DATA)}
# Total Cities: {total_cities}
# Services per City: {services}
# Total SEO Pages: {total_pages:,}
'''
    
    return output

if __name__ == "__main__":
    city_data = generate_city_data_file()
    
    with open('main/city_data_complete.py', 'w') as f:
        f.write(city_data)
    
    print(f"Generated city data for all 50 states")
    print(f"Total pages that will be created: {sum(len(s['cities']) for s in ALL_STATES_DATA.values()) * 4:,}")