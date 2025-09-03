from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair


def check(candidate):
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0, 3.0]) == (2.0, 2.0)
    assert candidate([10.6, 7.2, 13.0, 4.4, 3.9, 11.0, 10.9]) == (10.6, 10.9)
    assert candidate([2.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.0)
    assert candidate([2.0, 3.0, 4.0, 5.0, 2.2, 2.0]) == (2.0, 2.0)
    assert candidate([2.0, 3.0, 4.0, 5.0, 2.2, 2.0, 2.1]) == (2.0, 2.0)
    assert candidate([2.0, 3.0, 4.0, 5.0, 2.2, 2.0, 2.1, 2.2]) == (2.2, 2.2)

