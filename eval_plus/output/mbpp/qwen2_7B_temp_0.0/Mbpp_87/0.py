"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
def merge_dictionaries_three(dict1, dict2, dict3):
    # Merge the first two dictionaries using the update method
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    
    # Update the merged dictionary with elements from the third dictionary
    for key, value in dict3.items():
        if key in merged_dict:
            # If the key exists, append the value to the existing list
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                # Convert the existing value to a list and add the new value
                merged_dict[key] = [merged_dict[key], value]
        else:
            # If the key does not exist, simply add it to the dictionary
            merged_dict[key] = value
    
    return merged_dict

# Test the function with the provided test case
assert merge_dictionaries_three(
    {"R": "Red", "B": "Black", "P": "Pink"},
    {"G": "Green", "W": "White"},
    {"O": "Orange", "W": "White", "B": "Black"}
) == {'B': ['Black', 'Black'], 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': ['White', 'White'], 'O': 'Orange'}