"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
import math

def next_Perfect_Square(n):
    """
    Find the next perfect square greater than a given number.

    Args:
    n (int): The number to find the next perfect square for.

    Returns:
    int: The next perfect square greater than n.
    """
    # Calculate the square root of n
    sqrt_n = math.sqrt(n)
    
    # Round up to the nearest whole number
    rounded_sqrt_n = math.ceil(sqrt_n)
    
    # Return the square of the rounded-up value
    return rounded_sqrt_n ** 2

# Test cases to verify the correctness of the function
assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(49) == 50
assert next_Perfect_Square(1) == 4
assert next_Perfect_Square(0) == 1
assert next_Perfect_Square(25) == 26