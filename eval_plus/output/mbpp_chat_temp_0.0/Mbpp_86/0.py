"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
def centered_hexagonal_number(n):
    # Calculate the nth centered hexagonal number using the formula
    return 3 * n * (n - 1) + 1

# Test the function with the provided test case
assert centered_hexagonal_number(10) == 271
