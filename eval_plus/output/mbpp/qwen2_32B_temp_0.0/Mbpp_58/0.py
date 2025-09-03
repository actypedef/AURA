"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_Signs(x, y):
    return (x ^ y) < 0

# Test cases
assert opposite_Signs(1, -2) == True
assert opposite_Signs(-1, 2) == True
assert opposite_Signs(1, 2) == False
assert opposite_Signs(-1, -2) == False