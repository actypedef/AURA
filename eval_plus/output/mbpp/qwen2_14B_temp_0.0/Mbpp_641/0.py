"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
def is_nonagonal(n):
    # Formula to calculate the nth nonagonal number
    return int(n * (7 * n - 5) / 2)

# Test the function with the provided test case
assert is_nonagonal(10) == 325
