from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
from typing import *
from collections import *

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []

    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)

    return result

# Test cases to verify the correctness of the function
assert intersperse([], 4) == [], "Test case 1 failed"
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3], "Test case 2 failed"
