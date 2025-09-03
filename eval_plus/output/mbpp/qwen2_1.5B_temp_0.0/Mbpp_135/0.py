"""
Write a function to find the nth hexagonal number.
assert hexagonal_num(10) == 190
"""
def hexagonal_num(n):
    """
    Calculate the nth hexagonal number.

    Args:
    n (int): The position of the hexagonal number to calculate.

    Returns:
    int: The nth hexagonal number.
    """
    return 3 * n * (n - 1) // 2

# Test cases to verify the correctness of the function
assert hexagonal_num(10) == 190
assert hexagonal_num(5) == 45
assert hexagonal_num(1) == 1
assert hexagonal_num(7) == 63