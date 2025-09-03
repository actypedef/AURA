"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""
def add_dict_to_tuple(tup, dict):
    # Convert the tuple to a list to allow modification
    lst = list(tup)
    # Append the dictionary to the list
    lst.append(dict)
    # Convert the list back to a tuple
    return tuple(lst)

# Test the function
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3}) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})