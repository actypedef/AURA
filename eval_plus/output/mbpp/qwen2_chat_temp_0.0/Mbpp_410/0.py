"""
Write a function to find the minimum value in a given heterogeneous list.
assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
"""
def min_val(lst):
    # Initialize the minimum value to None
    min_value = None
    
    # Iterate through each element in the list
    for i in lst:
        # Check if the current element is an integer or float
        if isinstance(i, (int, float)):
            # If it's the first number encountered or smaller than the current minimum
            if min_value is None or i < min_value:
                # Update the minimum value
                min_value = i
                
    return min_value

# Test the function with the provided test case
assert min_val(['Python', 3, 2, 4, 5, 'version']) == 2