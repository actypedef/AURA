from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
from typing import *
from collections import *

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    
    total_sum = sum(numbers)
    total_product = reduce(lambda x, y: x * y, numbers, 1)
    
    return (total_sum, total_product)

# Check function to verify the correctness of the solution
def check_function():
    assert sum_product([]) == (0, 1), "Test with an empty list failed"
    assert sum_product([1, 2, 3, 4]) == (10, 24), "Test with [1, 2, 3, 4] failed"
    assert sum_product([5, -1, 2]) == (6, -10), "Test with [5, -1, 2] failed"
    print("All tests passed!")

check_function()