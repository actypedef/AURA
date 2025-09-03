"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    # Calculate the nth octagonal number using the formula: n * (2n - 1)
    return n * (2 * n - 1)

# Test the function with the provided test case
assert is_octagonal(5) == 65
