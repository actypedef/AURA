
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
from typing import *
from collections import *

def digit_sum(n):
    """Helper function to calculate the sum of digits of an integer."""
    return sum(int(digit) for digit in str(abs(n)))

def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.
    """
    # Sorting the list using a custom key
    # The primary key is the digit sum, and the secondary key is the original index
    return sorted(enumerate(nums), key=lambda x: (digit_sum(x[1]), x[0]))[::1]

# Check function to verify the correctness of the solution
def check_solution():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11], "Test case 1 failed"
    assert order_by_points([]) == [], "Test case 2 failed"
    assert order_by_points([56, 34, 12, 89, 23]) == [12, 23, 34, 56, 89], "Test case 3 failed"
    print("All test cases passed!")

check_solution()