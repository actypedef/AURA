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
    total_product = 1
    for number in numbers:
        total_product *= number
    
    return (total_sum, total_product)

# Check function to verify the correctness of the solution
def check_function():
    assert sum_product([]) == (0, 1), "Test case 1 failed"
    assert sum_product([1, 2, 3, 4]) == (10, 24), "Test case 2 failed"
    assert sum_product([5]) == (5, 5), "Test case 3 failed"
    assert sum_product([-1, 1, -2, 2]) == (0, 4), "Test case 4 failed"
    print("All test cases passed!")

check_function()