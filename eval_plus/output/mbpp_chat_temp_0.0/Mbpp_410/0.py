"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(mixed_list):
    # Filter out non-integer values from the list using a generator expression
    filtered_values = (item for item in mixed_list if isinstance(item, int))
    
    # Use the built-in min() function to find the smallest integer in the filtered list
    return min(filtered_values)

# Test the function with the provided test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
