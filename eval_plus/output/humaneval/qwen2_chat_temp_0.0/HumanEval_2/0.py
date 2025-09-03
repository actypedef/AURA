

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
from typing import *
from collections import *

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

# Test cases to verify the correctness of the function
assert truncate_number(3.5) == 0.5
assert truncate_number(4.75) == 0.75
assert truncate_number(10.01) == 0.01
assert truncate_number(123.456) == 0.456
assert truncate_number(0.999) == 0.999