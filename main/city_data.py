"""
City data for SEO-optimized location pages
"""

# Major cities in New England states with population and economic data
CITY_DATA = {
    'rhode-island': {
        'state_name': 'Rhode Island',
        'state_abbr': 'RI',
        'cities': [
            {'name': 'Providence', 'slug': 'providence', 'population': '190934', 'county': 'Providence County', 'lat': 41.8240, 'lng': -71.4128},
            {'name': 'Warwick', 'slug': 'warwick', 'population': '82823', 'county': 'Kent County', 'lat': 41.7001, 'lng': -71.4162},
            {'name': 'Cranston', 'slug': 'cranston', 'population': '81456', 'county': 'Providence County', 'lat': 41.7798, 'lng': -71.4373},
            {'name': 'Pawtucket', 'slug': 'pawtucket', 'population': '75604', 'county': 'Providence County', 'lat': 41.8787, 'lng': -71.3826},
            {'name': 'East Providence', 'slug': 'east-providence', 'population': '47139', 'county': 'Providence County', 'lat': 41.8137, 'lng': -71.3701},
            {'name': 'Woonsocket', 'slug': 'woonsocket', 'population': '43240', 'county': 'Providence County', 'lat': 42.0029, 'lng': -71.5148},
            {'name': 'Newport', 'slug': 'newport', 'population': '24996', 'county': 'Newport County', 'lat': 41.4901, 'lng': -71.3128},
            {'name': 'Smithfield', 'slug': 'smithfield', 'population': '22118', 'county': 'Providence County', 'lat': 41.8669, 'lng': -71.5493},
            {'name': 'Westerly', 'slug': 'westerly', 'population': '23421', 'county': 'Washington County', 'lat': 41.3776, 'lng': -71.8273},
            {'name': 'Johnston', 'slug': 'johnston', 'population': '29568', 'county': 'Providence County', 'lat': 41.8312, 'lng': -71.5170},
            {'name': 'North Providence', 'slug': 'north-providence', 'population': '33935', 'county': 'Providence County', 'lat': 41.8501, 'lng': -71.4662},
            {'name': 'West Warwick', 'slug': 'west-warwick', 'population': '30146', 'county': 'Kent County', 'lat': 41.6969, 'lng': -71.5217},
            {'name': 'Bristol', 'slug': 'bristol', 'population': '22493', 'county': 'Bristol County', 'lat': 41.6771, 'lng': -71.2662},
            {'name': 'Cumberland', 'slug': 'cumberland', 'population': '36405', 'county': 'Providence County', 'lat': 41.9667, 'lng': -71.4323},
            {'name': 'North Kingstown', 'slug': 'north-kingstown', 'population': '27732', 'county': 'Washington County', 'lat': 41.5501, 'lng': -71.4662},
        ]
    },
    'massachusetts': {
        'state_name': 'Massachusetts',
        'state_abbr': 'MA',
        'cities': [
            {'name': 'Boston', 'slug': 'boston', 'population': '675647', 'county': 'Suffolk County', 'lat': 42.3601, 'lng': -71.0589},
            {'name': 'Worcester', 'slug': 'worcester', 'population': '206518', 'county': 'Worcester County', 'lat': 42.2626, 'lng': -71.8023},
            {'name': 'Springfield', 'slug': 'springfield', 'population': '155929', 'county': 'Hampden County', 'lat': 42.1015, 'lng': -72.5898},
            {'name': 'Cambridge', 'slug': 'cambridge', 'population': '118403', 'county': 'Middlesex County', 'lat': 42.3736, 'lng': -71.1097},
            {'name': 'Lowell', 'slug': 'lowell', 'population': '115554', 'county': 'Middlesex County', 'lat': 42.6334, 'lng': -71.3162},
            {'name': 'Brockton', 'slug': 'brockton', 'population': '105643', 'county': 'Plymouth County', 'lat': 42.0834, 'lng': -71.0184},
            {'name': 'New Bedford', 'slug': 'new-bedford', 'population': '101079', 'county': 'Bristol County', 'lat': 41.6362, 'lng': -70.9342},
            {'name': 'Quincy', 'slug': 'quincy', 'population': '101636', 'county': 'Norfolk County', 'lat': 42.2529, 'lng': -71.0023},
            {'name': 'Lynn', 'slug': 'lynn', 'population': '101253', 'county': 'Essex County', 'lat': 42.4668, 'lng': -70.9495},
            {'name': 'Fall River', 'slug': 'fall-river', 'population': '94000', 'county': 'Bristol County', 'lat': 41.7015, 'lng': -71.1550},
            {'name': 'Newton', 'slug': 'newton', 'population': '88923', 'county': 'Middlesex County', 'lat': 42.3370, 'lng': -71.2092},
            {'name': 'Somerville', 'slug': 'somerville', 'population': '81562', 'county': 'Middlesex County', 'lat': 42.3876, 'lng': -71.0995},
            {'name': 'Framingham', 'slug': 'framingham', 'population': '72362', 'county': 'Middlesex County', 'lat': 42.2793, 'lng': -71.4162},
            {'name': 'Plymouth', 'slug': 'plymouth', 'population': '61217', 'county': 'Plymouth County', 'lat': 41.9584, 'lng': -70.6673},
            {'name': 'Attleboro', 'slug': 'attleboro', 'population': '46461', 'county': 'Bristol County', 'lat': 41.9445, 'lng': -71.2856},
        ]
    },
    'connecticut': {
        'state_name': 'Connecticut',
        'state_abbr': 'CT',
        'cities': [
            {'name': 'Bridgeport', 'slug': 'bridgeport', 'population': '148654', 'county': 'Fairfield County', 'lat': 41.1865, 'lng': -73.1952},
            {'name': 'New Haven', 'slug': 'new-haven', 'population': '134023', 'county': 'New Haven County', 'lat': 41.3083, 'lng': -72.9279},
            {'name': 'Hartford', 'slug': 'hartford', 'population': '121054', 'county': 'Hartford County', 'lat': 41.7638, 'lng': -72.6856},
            {'name': 'Stamford', 'slug': 'stamford', 'population': '135470', 'county': 'Fairfield County', 'lat': 41.0534, 'lng': -73.5387},
            {'name': 'Waterbury', 'slug': 'waterbury', 'population': '114403', 'county': 'New Haven County', 'lat': 41.5582, 'lng': -73.0515},
            {'name': 'Norwalk', 'slug': 'norwalk', 'population': '91184', 'county': 'Fairfield County', 'lat': 41.1177, 'lng': -73.4082},
            {'name': 'Danbury', 'slug': 'danbury', 'population': '86518', 'county': 'Fairfield County', 'lat': 41.3948, 'lng': -73.4540},
            {'name': 'New Britain', 'slug': 'new-britain', 'population': '74135', 'county': 'Hartford County', 'lat': 41.6612, 'lng': -72.7795},
            {'name': 'West Haven', 'slug': 'west-haven', 'population': '55584', 'county': 'New Haven County', 'lat': 41.2706, 'lng': -72.9470},
            {'name': 'Meriden', 'slug': 'meriden', 'population': '60850', 'county': 'New Haven County', 'lat': 41.5382, 'lng': -72.8070},
            {'name': 'Bristol', 'slug': 'bristol-ct', 'population': '60477', 'county': 'Hartford County', 'lat': 41.6718, 'lng': -72.9493},
            {'name': 'Milford', 'slug': 'milford', 'population': '56389', 'county': 'New Haven County', 'lat': 41.2223, 'lng': -73.0565},
            {'name': 'Fairfield', 'slug': 'fairfield', 'population': '62717', 'county': 'Fairfield County', 'lat': 41.1412, 'lng': -73.2637},
            {'name': 'Greenwich', 'slug': 'greenwich', 'population': '63518', 'county': 'Fairfield County', 'lat': 41.0262, 'lng': -73.6282},
            {'name': 'Westport', 'slug': 'westport', 'population': '28016', 'county': 'Fairfield County', 'lat': 41.1415, 'lng': -73.3579},
        ]
    },
    'new-hampshire': {
        'state_name': 'New Hampshire',
        'state_abbr': 'NH',
        'cities': [
            {'name': 'Manchester', 'slug': 'manchester', 'population': '115644', 'county': 'Hillsborough County', 'lat': 42.9956, 'lng': -71.4548},
            {'name': 'Nashua', 'slug': 'nashua', 'population': '91322', 'county': 'Hillsborough County', 'lat': 42.7654, 'lng': -71.4676},
            {'name': 'Concord', 'slug': 'concord', 'population': '43976', 'county': 'Merrimack County', 'lat': 43.2081, 'lng': -71.5376},
            {'name': 'Derry', 'slug': 'derry', 'population': '34317', 'county': 'Rockingham County', 'lat': 42.8806, 'lng': -71.3273},
            {'name': 'Dover', 'slug': 'dover', 'population': '32741', 'county': 'Strafford County', 'lat': 43.1979, 'lng': -70.8737},
            {'name': 'Rochester', 'slug': 'rochester', 'population': '32492', 'county': 'Strafford County', 'lat': 43.3045, 'lng': -70.9756},
            {'name': 'Salem', 'slug': 'salem', 'population': '30089', 'county': 'Rockingham County', 'lat': 42.7884, 'lng': -71.2009},
            {'name': 'Merrimack', 'slug': 'merrimack', 'population': '26939', 'county': 'Hillsborough County', 'lat': 42.8651, 'lng': -71.4934},
            {'name': 'Keene', 'slug': 'keene', 'population': '23047', 'county': 'Cheshire County', 'lat': 42.9336, 'lng': -72.2782},
            {'name': 'Portsmouth', 'slug': 'portsmouth', 'population': '21956', 'county': 'Rockingham County', 'lat': 43.0718, 'lng': -70.7626},
        ]
    },
    'vermont': {
        'state_name': 'Vermont',
        'state_abbr': 'VT',
        'cities': [
            {'name': 'Burlington', 'slug': 'burlington', 'population': '44743', 'county': 'Chittenden County', 'lat': 44.4759, 'lng': -73.2121},
            {'name': 'Essex', 'slug': 'essex', 'population': '22094', 'county': 'Chittenden County', 'lat': 44.4906, 'lng': -73.1018},
            {'name': 'South Burlington', 'slug': 'south-burlington', 'population': '20292', 'county': 'Chittenden County', 'lat': 44.4670, 'lng': -73.1710},
            {'name': 'Colchester', 'slug': 'colchester', 'population': '17524', 'county': 'Chittenden County', 'lat': 44.5439, 'lng': -73.1481},
            {'name': 'Rutland', 'slug': 'rutland', 'population': '15807', 'county': 'Rutland County', 'lat': 43.6106, 'lng': -72.9726},
            {'name': 'Bennington', 'slug': 'bennington', 'population': '15333', 'county': 'Bennington County', 'lat': 42.8781, 'lng': -73.1968},
            {'name': 'Brattleboro', 'slug': 'brattleboro', 'population': '12184', 'county': 'Windham County', 'lat': 42.8509, 'lng': -72.5579},
            {'name': 'Milton', 'slug': 'milton', 'population': '10723', 'county': 'Chittenden County', 'lat': 44.6306, 'lng': -73.1110},
            {'name': 'Montpelier', 'slug': 'montpelier', 'population': '8074', 'county': 'Washington County', 'lat': 44.2601, 'lng': -72.5754},
            {'name': 'Barre', 'slug': 'barre', 'population': '8491', 'county': 'Washington County', 'lat': 44.1970, 'lng': -72.5020},
        ]
    },
    'maine': {
        'state_name': 'Maine',
        'state_abbr': 'ME',
        'cities': [
            {'name': 'Portland', 'slug': 'portland', 'population': '68408', 'county': 'Cumberland County', 'lat': 43.6591, 'lng': -70.2568},
            {'name': 'Lewiston', 'slug': 'lewiston', 'population': '37121', 'county': 'Androscoggin County', 'lat': 44.1004, 'lng': -70.2148},
            {'name': 'Bangor', 'slug': 'bangor', 'population': '31753', 'county': 'Penobscot County', 'lat': 44.8012, 'lng': -68.7778},
            {'name': 'South Portland', 'slug': 'south-portland', 'population': '26498', 'county': 'Cumberland County', 'lat': 43.6415, 'lng': -70.2409},
            {'name': 'Auburn', 'slug': 'auburn', 'population': '24061', 'county': 'Androscoggin County', 'lat': 44.0979, 'lng': -70.2312},
            {'name': 'Biddeford', 'slug': 'biddeford', 'population': '22552', 'county': 'York County', 'lat': 43.4926, 'lng': -70.4534},
            {'name': 'Augusta', 'slug': 'augusta', 'population': '18899', 'county': 'Kennebec County', 'lat': 44.3106, 'lng': -69.7795},
            {'name': 'Saco', 'slug': 'saco', 'population': '20381', 'county': 'York County', 'lat': 43.5009, 'lng': -70.4428},
            {'name': 'Westbrook', 'slug': 'westbrook', 'population': '20400', 'county': 'Cumberland County', 'lat': 43.6770, 'lng': -70.3712},
            {'name': 'Waterville', 'slug': 'waterville', 'population': '15722', 'county': 'Kennebec County', 'lat': 44.5520, 'lng': -69.6317},
        ]
    }
}

def get_all_cities():
    """Get all cities across all states"""
    all_cities = []
    for state, data in CITY_DATA.items():
        for city in data['cities']:
            city_info = city.copy()
            city_info['state'] = state
            city_info['state_name'] = data['state_name']
            city_info['state_abbr'] = data['state_abbr']
            all_cities.append(city_info)
    return all_cities

def get_city_by_slug(city_slug, state_slug=None):
    """Get city data by slug"""
    for state, data in CITY_DATA.items():
        if state_slug and state != state_slug:
            continue
        for city in data['cities']:
            if city['slug'] == city_slug:
                city_info = city.copy()
                city_info['state'] = state
                city_info['state_name'] = data['state_name']
                city_info['state_abbr'] = data['state_abbr']
                return city_info
    return None