
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
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    # Helper function to calculate the sum of digits of an integer
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))
    
    # Sort the list using a custom key that first compares the sum of digits and then the index
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

# Test cases