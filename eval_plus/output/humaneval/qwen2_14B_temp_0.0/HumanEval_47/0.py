

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l."""
    sorted_list = sorted(l)
    n = len(sorted_list)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2.0
    else:
        return sorted_list[mid]

# Test cases