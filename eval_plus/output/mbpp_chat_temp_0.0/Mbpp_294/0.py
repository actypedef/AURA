"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(mixed_list):
    # Filter out non-integer values from the list using a generator expression
    filtered_values = (item for item in mixed_list if isinstance(item, int))
    
    # Use the built-in max() function to find the maximum integer value
    return max(filtered_values)

# Test the function with the provided test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5
