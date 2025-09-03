
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
from typing import *
from collections import *

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_str = str(abs(num))  # Convert to string and remove sign if negative
    even_count = sum(1 for digit in num_str if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in num_str if int(digit) % 2 != 0)
    return even_count, odd_count

# Test cases
assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(0) == (1, 0)
assert even_odd_count(1111) == (0, 4)
assert even_odd_count(2222) == (4, 0)
