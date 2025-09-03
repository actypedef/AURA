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
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")
    
    # Initialize variables to store the closest pair and their minimum distance
    closest_pair = (numbers[0], numbers[1])
    min_distance = abs(numbers[0] - numbers[1])
    
    # Iterate through each pair of numbers to find the closest ones
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            current_distance = abs(numbers[i] - numbers[j])
            if current_distance < min_distance:
                min_distance = current_distance
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
                
    return closest_pair
