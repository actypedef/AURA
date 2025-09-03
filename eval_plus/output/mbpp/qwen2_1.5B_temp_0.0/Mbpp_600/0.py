"""
Write a python function to check whether the given number is even or not.
assert is_Even(1) == False
"""
def is_even(n):
    """
    Check if the given number is even or not.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return n % 2 == 0

# Test cases
assert is_even(1) == False
assert is_even(2) == True
assert is_even(3) == False
assert is_even(4) == True
assert is_even(5) == False
assert is_even(6) == True
assert is_even(7) == False
assert is_even(8) == True
assert is_even(9) == False
assert is_even(10) == True