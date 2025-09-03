
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
from typing import *
from collections import *

def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            has_odd_digit = True
        n //= 10
    return product if has_odd_digit else 0

# Test cases
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(2468) == 0
assert digits(13579) == 945
