"""
Write a function to merge three dictionaries into a single dictionary.
assert merge_dictionaries_three({ "R": "Red", "B": "Black", "P": "Pink" }, { "G": "Green", "W": "White" },{ "O": "Orange", "W": "White", "B": "Black" })=={'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}
"""
def merge_dictionaries_three(dict1, dict2, dict3):
    # Merge all dictionaries into one
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict

# Test the function
assert merge_dictionaries_three({"R": "Red", "B": "Black", "P": "Pink"}, {"G": "Green", "W": "White"}, {"O": "Orange", "W": "White", "B": "Black"}) == {'B': 'Black', 'R': 'Red', 'P': 'Pink', 'G': 'Green', 'W': 'White', 'O': 'Orange'}