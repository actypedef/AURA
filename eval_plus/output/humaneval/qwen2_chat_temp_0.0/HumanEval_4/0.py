from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
from typing import *
from collections import *

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0

    mean_value = sum(numbers) / len(numbers)
    total_deviation = sum(abs(x - mean_value) for x in numbers)
    mad = total_deviation / len(numbers)

    return mad

# Check function to verify the correctness of the solution
def check_solution():
    test_cases = [
        ([1.0, 2.0, 3.0, 4.0], 1.0),
        ([5.0, 7.0, 9.0], 1.6666666666666667),
        ([10.0, 10.0, 10.0], 0.0),
        ([], 0.0)
    ]

    for i, (numbers, expected) in enumerate(test_cases):
        result = mean_absolute_deviation(numbers)
        assert abs(result - expected) < 1e-6, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

check_solution()