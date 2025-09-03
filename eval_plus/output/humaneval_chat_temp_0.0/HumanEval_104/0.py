
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
def has_no_even_digit(n):
    """Check if a number contains only odd digits."""
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            return False
        n //= 10
    return True

def unique_digits(x):
    """Return a sorted list of numbers from the input list that contain only odd digits."""
    result = [num for num in x if has_no_even_digit(num)]
    return sorted(result)

# Test cases to verify the correctness of the function