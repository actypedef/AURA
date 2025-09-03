
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
from typing import *
from collections import *

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only the number 1 itself
    # For n > 1, there are 2*(10^(n-1)) possibilities in total,
    # but we need to subtract the overlap where numbers both start and end with 1.
    return 2 * (10 ** (n - 1)) - 10 ** (n - 2)

# Test the function