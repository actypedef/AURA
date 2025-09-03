"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""
def add_dict_to_tuple(test_tup, K):
    # Convert the tuple to a list to allow modification
    res = list(test_tup)
    
    # Append the dictionary to the list
    res.append(K)
    
    # Convert the list back to a tuple
    res = tuple(res)
    
    return res

# Test the function with the provided test case
assert add_dict_to_tuple((4, 5, 6), {"MSAM": 1, "is": 2, "best": 3}) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
