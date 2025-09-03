"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    return a ** b

# Test cases to verify the correctness of the function
assert power(3, 4) == 81
assert power(2, 5) == 32
assert power(0, 10) == 0
assert power(-2, 3) == -8
assert power(10, 0) == 1