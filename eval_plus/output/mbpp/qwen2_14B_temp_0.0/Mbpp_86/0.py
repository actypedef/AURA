"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
def centered_hexagonal_number(n):
    # Formula to calculate the nth centered hexagonal number
    return 3 * n * (n - 1) + 1

# Test the function with the provided test case
assert centered_hexagonal_number(10) == 271
