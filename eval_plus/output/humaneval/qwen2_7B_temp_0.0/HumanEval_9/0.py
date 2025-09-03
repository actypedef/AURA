from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = []
    current_max = float('-inf')
    for number in numbers:
        current_max = max(current_max, number)
        result.append(current_max)

    return result

# Test cases to verify the correctness of the function
assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
assert rolling_max([7, 8, 9, 10, 11, 12, 13, 14, 15]) == [7, 8, 9, 10, 11, 12, 13, 14, 15]
assert rolling_max([]) == []
assert rolling_max([10]) == [10]
