"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
def max_val(heterogeneous_list):
    # Initialize the maximum value as negative infinity
    max_value = float('-inf')
    
    # Iterate through each element in the heterogeneous list
    for item in heterogeneous_list:
        # Check if the current item is an integer
        if isinstance(item, int):
            # Update the maximum value if the current item is greater than the current maximum
            if item > max_value:
                max_value = item
    
    # Return the maximum value found
    return max_value

# Test the function with the provided test case
assert max_val(['Python', 3, 2, 4, 5, 'version']) == 5