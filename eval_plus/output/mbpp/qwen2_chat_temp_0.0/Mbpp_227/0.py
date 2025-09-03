"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(x, y, z):
    # Use the built-in min function to find the minimum of the three numbers
    return min(x, y, z)

# Test the function with the provided test case
assert min_of_three(10, 20, 0) == 0
