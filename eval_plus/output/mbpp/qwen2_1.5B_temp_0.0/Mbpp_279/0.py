"""
Write a function to find the nth decagonal number.
assert is_num_decagonal(3) == 27
"""
def is_num_decagonal(n):
    """
    Calculate the nth decagonal number.

    Args:
    n (int): The position of the decagonal number to calculate.

    Returns:
    int: The nth decagonal number.
    """
    return 5 * n * (n - 1)

# Test cases to verify the correctness of the function
assert is_num_decagonal(3) == 27
assert is_num_decagonal(4) == 60
assert is_num_decagonal(5) == 120
assert is_num_decagonal(6) == 210
assert is_num_decagonal(7) == 330
assert is_num_decagonal(8) == 495
assert is_num_decagonal(9) == 690
assert is_num_decagonal(10) == 945