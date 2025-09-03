"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
def dict_depth(d):
    # Check if the input is a dictionary
    if isinstance(d, dict):
        # If it's not empty, return 1 plus the maximum depth of its values
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    # If the input is not a dictionary, return 0
    return 0

# Test the function with the provided test case
assert dict_depth({'a': 1, 'b': {'c': {'d': {}}}}) == 4
