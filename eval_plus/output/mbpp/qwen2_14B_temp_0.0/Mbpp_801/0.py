"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(a, b, c):
    # Check if all three numbers are equal
    if a == b == c:
        return 3
    # Check if any two numbers are equal
    elif a == b or b == c or a == c:
        return 2
    else:
        return 0

# Test cases
assert test_three_equal(1, 1, 1) == 3
assert test_three_equal(1, 1, 2) == 2
assert test_three_equal(1, 2, 2) == 2
assert test_three_equal(1, 2, 3) == 0
