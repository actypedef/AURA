"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(lst):
    # Filter out non-integer values from the list
    new_lst = [item for item in lst if isinstance(item, int)]
    
    # Return the minimum value from the filtered list
    return min(new_lst)

# Test the function with the provided test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
