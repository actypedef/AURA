"""
Write a python function to find the first digit of a given number.
assert first_Digit(123) == 1
"""
def first_Digit(n):
    """
    Find the first digit of a given number.

    Args:
    n (int): The number to find the first digit of.

    Returns:
    int: The first digit of the given number.
    """
    while n >= 10:
        n //= 10
    return n

# Test cases
assert first_Digit(123) == 1
assert first_Digit(987654321) == 9
assert first_Digit(-12345) == 1
assert first_Digit(0) == 0