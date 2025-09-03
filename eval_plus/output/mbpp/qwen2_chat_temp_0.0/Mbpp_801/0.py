"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(x, y, z):
    # Check if all three numbers are equal
    if x == y == z:
        return 3
    else:
        return 0

# Test the function with the provided test case
assert test_three_equal(1, 1, 1) == 3