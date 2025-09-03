"""
Write a function to check whether the given number is a perfect square or not. https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
assert not is_perfect_square(10)
"""
import math

def is_perfect_square(n):
    """
    Check if the given number is a perfect square.
    
    Args:
    n (int): The number to check.
    
    Returns:
    bool: True if n is a perfect square, False otherwise.
    """
    root = int(math.sqrt(n))
    return root * root == n

# Test cases
assert not is_perfect_square(10)  # Output: True
assert is_perfect_square(25)  # Output: True
assert not is_perfect_square(36)  # Output: True
assert not is_perfect_square(49)  # Output: True
assert not is_perfect_square(50)  # Output: False