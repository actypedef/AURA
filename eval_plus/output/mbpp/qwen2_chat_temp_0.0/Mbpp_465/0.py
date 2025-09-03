"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
def drop_empty(dict):
    # Use dictionary comprehension to filter out None values
    return {key: value for key, value in dict.items() if value is not None}

# Test the function with the provided test case
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}
