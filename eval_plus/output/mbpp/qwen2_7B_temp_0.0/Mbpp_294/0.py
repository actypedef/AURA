"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(heterogeneous_list):
    # Initialize the maximum value as None
    max_value = None
    
    # Iterate through each element in the heterogeneous list
    for element in heterogeneous_list:
        # Check if the current element is an integer or float
        if isinstance(element, (int, float)):
            # Update the maximum value if the current element is greater
            if max_value is None or element > max_value:
                max_value = element
    
    return max_value

# Test the function with the provided test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5