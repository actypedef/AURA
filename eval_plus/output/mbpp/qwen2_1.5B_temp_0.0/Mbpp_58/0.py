"""
Write a python function to check whether the given two integers have opposite sign or not.
assert opposite_Signs(1,-2) == True
"""
def opposite_signs(a, b):
    """
    Check if two integers have opposite signs.

    Args:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    bool: True if the integers have opposite signs, False otherwise.
    """
    return (a > 0) != (b > 0)

# Test cases
assert opposite_signs(1, -2) == True
assert opposite_signs(-3, 4) == True
assert opposite_signs(5, 6) == False
assert opposite_signs(-7, -8) == False