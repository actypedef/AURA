"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
def is_num_decagonal(n):
    # Formula to calculate the nth decagonal number
    return 4 * n * n - 3 * n

# Test the function with the provided test case
assert is_num_decagonal(3) == 27