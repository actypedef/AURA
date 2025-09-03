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
    # Sort the list to easily find adjacent elements
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to store the closest pair and their difference
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_difference = abs(sorted_numbers[0] - sorted_numbers[1])
    
    # Iterate through the sorted list to find the closest pair
    for i in range(len(sorted_numbers) - 1):
        current_difference = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        if current_difference < min_difference:
            min_difference = current_difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i + 1])
    
    return closest_pair

# Test cases