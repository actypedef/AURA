"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""
def maximum(x, y):
    # Compare x and y, return the larger value
    if x >= y:
        return x
    else:
        return y

# Test the function with the provided test case
assert maximum(5, 10) == 10
