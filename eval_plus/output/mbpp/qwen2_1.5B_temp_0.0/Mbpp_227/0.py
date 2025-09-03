"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""
def min_of_three(a, b, c):
    return min(a, b, c)

# Test cases
assert min_of_three(10, 20, 0) == 0
assert min_of_three(-5, -3, -8) == -8
assert min_of_three(7, 9, 4) == 4