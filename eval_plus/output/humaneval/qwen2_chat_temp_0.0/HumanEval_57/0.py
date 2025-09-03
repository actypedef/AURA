

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
    
    # Determine the direction of monotonicity based on the first two elements
    increasing = l[1] >= l[0]
    
    for i in range(1, len(l)):
        if increasing and l[i] < l[i - 1]:
            return False
        elif not increasing and l[i] > l[i - 1]:
            return False
    
    return True

# Test cases to verify the correctness of the function
assert monotonic([1, 2, 4, 20]) == True
assert monotonic([1, 20, 4, 10]) == False
assert monotonic([4, 1, 0, -10]) == True