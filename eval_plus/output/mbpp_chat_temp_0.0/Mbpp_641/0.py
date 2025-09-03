"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
def is_nonagonal(n):
    # Calculate the nth nonagonal number using the formula: n * (7n - 5) / 2
    return int(n * (7 * n - 5) / 2)

# Test the function with the provided test case
assert is_nonagonal(10) == 325
