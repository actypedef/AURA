from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
from typing import *
from collections import *

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Args:
        numbers: A list of floating-point numbers.
        
    Returns:
        A list of floating-point numbers where each number has been scaled between 0 and 1 based on the minimum and maximum values in the input list.
    """
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")
    
    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    
    return [(num - min_val) / range_val for num in numbers]

# Test cases