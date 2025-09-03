"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
def merge_dictionaries_three(dict1, dict2, dict3):
    # Create an empty dictionary to store the merged results
    result = {}
    
    # Add all items from the first dictionary to the result
    for key, value in dict1.items():
        result[key] = value
    
    # Add all items from the second dictionary to the result
    for key, value in dict2.items():
        result[key] = value
    
    # Add all items from the third dictionary to the result
    for key, value in dict3.items():
        result[key] = value
    
    return result

# Test the function with the provided test case
assert merge_dictionaries_three(
    {"R": "Red", "B": "Black", "P": "Pink"},
    {"G": "Green", "W": "White"},
    {"O": "Orange", "W": "White", "B": "Black"}
) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}