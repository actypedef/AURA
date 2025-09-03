"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    # Calculate the formula for the nth octagonal number
    return n * (3 * n - 2)

# Test cases to verify the correctness of the function
assert is_octagonal(1) == 1
assert is_octagonal(2) == 8
assert is_octagonal(3) == 21
assert is_octagonal(4) == 36
assert is_octagonal(5) == 65
assert is_octagonal(6) == 105
assert is_octagonal(7) == 153
assert is_octagonal(8) == 210
assert is_octagonal(9) == 285
assert is_octagonal(10) == 364