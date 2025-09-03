"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
def drop_empty(d):
    # Use dictionary comprehension to filter out items with None values
    return {k: v for k, v in d.items() if v is not None}

# Test the function with the provided test case
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}
