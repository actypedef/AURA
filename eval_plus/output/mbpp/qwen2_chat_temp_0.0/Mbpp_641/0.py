"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
def is_nonagonal(n):
    # Calculate the nth nonagonal number using the formula
    return int((7 * n * (n - 1)) / 2 + n)

# Test the function with the provided test case
assert is_nonagonal(10) == 325
