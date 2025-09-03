"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
def minimum(a, b):
    # Compare 'a' and 'b' and return the smaller value
    if a < b:
        return a
    else:
        return b

# Test the function with the provided test case
assert minimum(1, 2) == 1
