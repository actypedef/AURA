"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(heterogeneous_list):
    # Initialize the minimum value to None
    min_value = None
    
    # Iterate through each element in the heterogeneous list
    for item in heterogeneous_list:
        # Check if the current item is an integer or float
        if isinstance(item, (int, float)):
            # If min_value is None or the current item is less than min_value, update min_value
            if min_value is None or item < min_value:
                min_value = item
    
    # Return the minimum value found
    return min_value

# Test the function with the provided test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2
