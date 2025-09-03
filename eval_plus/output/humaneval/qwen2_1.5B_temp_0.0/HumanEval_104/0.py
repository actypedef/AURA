
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    # Filter out numbers containing even digits
    filtered_numbers = [num for num in x if not any(digit % 2 == 0 for digit in str(num))]
    
    # Sort the filtered numbers
    sorted_numbers = sorted(filtered_numbers)
    
    return sorted_numbers

# Test cases
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Test case 1 failed"
assert unique_digits([152, 323, 1422, 10]) == [], "Test case 2 failed"