from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
# Importing necessary package for deep copy
from copy import deepcopy

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Using a set to track seen numbers
    seen = set()
    # Using a list to store unique numbers while preserving their original order
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test cases to verify the correctness of the function
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4], "Test case 1 failed"
assert remove_duplicates([5, 6, 7, 8, 9, 5, 6, 7, 8, 9]) == [5, 6, 7, 8, 9], "Test case 2 failed"
assert remove_duplicates([]) == [], "Test case 3 failed"
assert remove_duplicates([10]) == [10], "Test case 4 failed"
