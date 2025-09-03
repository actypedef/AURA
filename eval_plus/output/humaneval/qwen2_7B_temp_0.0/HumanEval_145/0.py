
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
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, they are ordered based on their index in the original list.
    
    :param nums: List of integers to be sorted.
    :return: Sorted list of integers.
    """
    # Calculate the sum of digits for each number and pair it with its index
    def digit_sum(n: int) -> int:
        return sum(int(digit) for digit in str(abs(n)))
    
    indexed_nums = [(digit_sum(num), idx, num) for idx, num in enumerate(nums)]
    
    # Sort the numbers first by digit sum, then by their original index
    indexed_nums.sort(key=lambda x: (x[0], x[1]))
    
    # Extract the sorted numbers from the tuples
    sorted_nums = [num for _, _, num in indexed_nums]
    
    return sorted_nums

# Check function to verify the correctness of the solution
def check():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []

check()