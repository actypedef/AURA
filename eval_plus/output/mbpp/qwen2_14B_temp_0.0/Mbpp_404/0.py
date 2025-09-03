"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
def minimum(x, y):
    # Return the smaller of x and y
    return x if x < y else y

# Test the function with the provided test case
assert minimum(1, 2) == 1
