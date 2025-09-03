from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    
    # Initialize variables
    max_so_far = numbers[0]
    result = [max_so_far]
    
    # Iterate through the list starting from the second element
    for num in numbers[1:]:
        # Update max_so_far if the current number is greater than it
        if num > max_so_far:
            max_so_far = num
        
        # Append the current max to the result list
        result.append(max_so_far)
    
    return result

# Test cases
assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4], "Test case 1 failed"
assert rolling_max([]) == [], "Test case 2 failed"
assert rolling_max([7]) == [7], "Test case 3 failed"