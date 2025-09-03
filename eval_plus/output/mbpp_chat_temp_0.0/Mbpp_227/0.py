"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(x, y, z):
    # Initialize the minimum value as x
    min_val = x
    
    # Compare with y and update if y is smaller
    if y < min_val:
        min_val = y
    
    # Compare with z and update if z is smaller
    if z < min_val:
        min_val = z
    
    return min_val

# Test the function with the provided test case
assert min_of_three(10, 20, 0) == 0