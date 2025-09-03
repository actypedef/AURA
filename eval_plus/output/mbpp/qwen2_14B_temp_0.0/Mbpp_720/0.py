"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""
def add_dict_to_tuple(tup, dict):
    # Convert the tuple to a list
    tup = list(tup)
    
    # Append the dictionary to the list
    tup.append(dict)
    
    # Convert the list back to a tuple
    return tuple(tup)

# Test the function with the provided test case
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
