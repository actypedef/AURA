"""
Write a python function to find the maximum of two numbers.
assert maximum(5,10) == 10
"""
def maximum(a, b):
    # Compare two numbers and return the larger one
    if a >= b:
        return a
    else:
        return b

# Test the function with the provided test case
assert maximum(5, 10) == 10
