"""
Write a function to find nth centered hexagonal number.
assert centered_hexagonal_number(10) == 271
"""
def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    Args:
    n (int): The position of the centered hexagonal number to calculate.

    Returns:
    int: The nth centered hexagonal number.
    """
    return 3 * n * (n - 1) + 1

# Test cases to verify the correctness of the function
assert centered_hexagonal_number(10) == 271
assert centered_hexagonal_number(5) == 41
assert centered_hexagonal_number(1) == 1
assert centered_hexagonal_number(8) == 169