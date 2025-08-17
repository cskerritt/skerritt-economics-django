"""
City validation utilities
"""

def validate_unique_city_state_combinations(city_list):
    """
    Validate that there are no duplicate city-state combinations in the list.
    
    Args:
        city_list: List of dictionaries containing 'city' and 'state' keys
        
    Raises:
        ValueError: If duplicate city-state combination is found
    """
    seen_combinations = set()
    for city_data in city_list:
        combo_key = (city_data['city'], city_data['state'])
        if combo_key in seen_combinations:
            raise ValueError(
                f"Duplicate city-state combination found: {combo_key[0]}-{combo_key[1]}"
            )
        seen_combinations.add(combo_key)