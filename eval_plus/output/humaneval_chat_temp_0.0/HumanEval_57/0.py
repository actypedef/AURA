

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): The list to check for monotonicity.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    # Check if the list is empty or has one element, which is trivially monotonic
    if len(l) <= 1:
        return True
    
    # Determine if the list is non-decreasing or non-increasing
    increasing = all(x <= y for x, y in zip(l, l[1:]))
    decreasing = all(x >= y for x, y in zip(l, l[1:]))
    
    # Return True if either condition is met
    return increasing or decreasing

# Test cases