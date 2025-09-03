"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
def dict_depth(dic):
    # Check if the input is a dictionary
    if isinstance(dic, dict):
        # If it's not empty, return 1 (for the current level) plus the maximum depth of its values
        return 1 + (max(map(dict_depth, dic.values())) if dic else 0)
    # If the input is not a dictionary, return 0 as it has no depth
    return 0

# Test the function with the provided test case
assert dict_depth({'a': 1, 'b': {'c': {'d': {}}}}) == 4
