"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    # Calculate the nth octagonal number using the formula: n * (3n - 2)
    return n * (3 * n - 2)

# Test the function with the provided test case
assert is_octagonal(5) == 65
