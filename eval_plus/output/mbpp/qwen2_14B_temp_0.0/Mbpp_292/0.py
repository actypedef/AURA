"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""
def find(x, y):
    # Integer division to find the quotient
    quotient = x // y
    return quotient

# Test the function with the provided test case
assert find(10, 3) == 3
