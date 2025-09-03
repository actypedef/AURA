"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(x, y, z):
    # Initialize the minimum value as x
    min_value = x
    
    # Compare y with the current minimum value and update if necessary
    if y < min_value:
        min_value = y
    
    # Compare z with the current minimum value and update if necessary
    if z < min_value:
        min_value = z
    
    # Return the minimum value found
    return min_value

# Test the function with the provided test case
assert min_of_three(10, 20, 0) == 0