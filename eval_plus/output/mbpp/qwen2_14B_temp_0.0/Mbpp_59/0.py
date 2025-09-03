"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    # Formula to calculate the nth octagonal number
    return n * (6 * n - 4)

# Test the function with the provided test case
assert is_octagonal(5) == 65
