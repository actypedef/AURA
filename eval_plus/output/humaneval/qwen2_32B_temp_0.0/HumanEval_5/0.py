from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    return result


def check(candidate):
    assert candidate([], 4) == []
    assert candidate([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert candidate([1, 1, 1, 1], 0) == [1, 0, 1, 0, 1, 0, 1]
    assert candidate([1, 2, 3, 4, 5, 6], 7) == [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]
    assert candidate([1, 2, 3, 4, 5], 0) == [1, 0, 2, 0, 3, 0, 4, 0, 5]
    assert candidate([1, 2], 0) == [1, 0, 2]
    assert candidate([1], 0) == [1]
    assert candidate([1, 2, 3, 4, 5, 6], 1) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 2) == [1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 3) == [1, 3, 2, 3, 3, 3, 4, 3, 5, 3, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 4) == [1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 5) == [1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 6) == [1, 6, 2, 6, 3, 6, 4, 6, 5, 6, 6]
    assert candidate([1, 2, 3, 4, 5, 6], 7) == [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]
    assert candidate([1, 2, 3, 