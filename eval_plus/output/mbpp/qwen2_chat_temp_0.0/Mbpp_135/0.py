"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    # Calculate the nth hexagonal number using the formula: n * (2n - 1)
    return int(n * (2 * n - 1))

# Test the function with the provided test case
assert hexagonal_num(10) == 190
