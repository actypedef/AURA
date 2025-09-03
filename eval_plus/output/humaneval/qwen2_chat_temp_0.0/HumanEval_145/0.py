
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
    # Define a helper function to calculate the sum of digits of a number
    def sum_of_digits(n: int) -> int:
        return sum(int(digit) for digit in str(abs(n)))
    
    # Sort the list using the sum of digits as the primary key and index as the secondary key
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

# Test cases