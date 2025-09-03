"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    # Calculate the nth hexagonal number using the formula
    return n * (4 * n - 3)

# Test cases to validate the function
assert hexagonal_num(10) == 190
