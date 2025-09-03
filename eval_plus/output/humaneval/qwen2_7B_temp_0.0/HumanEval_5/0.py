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
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The list of integers to be interspersed.
        delimiter (int): The integer to insert between each pair of elements.
        
    Returns:
        List[int]: A new list with the delimiter inserted between each pair of original elements.
        
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the input list starting from the second element
    for num in numbers[1:]:
        result.extend([delimiter, num])  # Append the delimiter followed by the current number

    return result

# Test cases