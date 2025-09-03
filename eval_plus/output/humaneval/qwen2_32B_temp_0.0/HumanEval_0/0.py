from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False


def test():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.5) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.5) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.4) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.6) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.7) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.8) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.9) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.0) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.1) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.2) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.3) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 1.4) == True
    assert has_close_elements([1.0, 2.0, 3.0, 4.