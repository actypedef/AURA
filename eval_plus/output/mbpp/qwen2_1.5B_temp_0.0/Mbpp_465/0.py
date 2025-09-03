"""
Write a function to drop empty items from a given dictionary.
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
"""
def drop_empty(input_dict):
    # Use dictionary comprehension to filter out None values
    return {key: value for key, value in input_dict.items() if value is not None}

# Test cases to verify the correctness of the function
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}) == {'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'a': 1, 'b': None, 'c': 2}) == {'a': 1, 'c': 2}
assert drop_empty({}) == {}