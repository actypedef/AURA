from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return [num for num in numbers if counts[num] == 1]


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 1, 1, 1, 1]) == []
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([]) == []
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5]) == [3, 4, 6]
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5, 7, 8, 9, 8, 7]) == [3, 4, 6, 9]
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5, 7, 8, 9, 8, 7, 10, 11, 12, 11, 10]) == [3, 4, 6, 9, 12]
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5, 7, 8, 9, 8, 7, 10, 11, 12, 11, 10, 13, 14, 15, 14, 13]) == [3, 4, 6, 9, 12, 15]
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5, 7, 8, 9, 8, 7, 10, 11, 12, 11, 10, 13, 14, 15, 14, 13, 16, 17, 18, 17, 16]) == [3, 4, 6, 9, 12, 15, 18]
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5, 6, 5, 7, 8, 9, 8, 7, 10, 11, 12, 11, 10, 13, 14, 15, 14, 13, 16, 17, 18, 17, 16, 19, 20, 21, 20, 19]) == [3