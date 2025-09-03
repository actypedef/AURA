
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
from typing import *
from collections import *

def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    # Since the smallest sum of 4 positive even numbers is 2+2+2+2=8,
    # any number less than 8 cannot be expressed as such a sum.
    if n < 8:
        return False
    
    # If n is even and greater than or equal to 8, it can always be expressed
    # as the sum of four even numbers. For example, n = 8 can be expressed as 2+2+2+2,
    # and any larger even number can be expressed by adding 2 to one of the terms.
    return n % 2 == 0

# Test cases