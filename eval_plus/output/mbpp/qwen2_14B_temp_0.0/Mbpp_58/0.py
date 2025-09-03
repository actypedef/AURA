"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(x, y): 
    # Check if the product of x and y is negative
    return (x ^ y) < 0

# Test the function with the provided test case
assert opposite_Signs(1, -2) == True
