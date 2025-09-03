"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
def is_num_decagonal(n):
    # Calculate the nth decagonal number using the formula: n * (4n - 3)
    return n * (4 * n - 3)

# Test the function with the provided test case
assert is_num_decagonal(3) == 27
