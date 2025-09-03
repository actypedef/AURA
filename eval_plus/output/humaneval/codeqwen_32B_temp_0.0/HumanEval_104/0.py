
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
    def has_even_digit(n):
        while n > 0:
            if n % 2 == 0:
                return True
            n //= 10
        return False

    return sorted([i for i in x if not has_even_digit(i)])

# Test cases
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([100, 200, 300, 400, 500]) == []
assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
assert unique_digits([123, 456, 789, 101, 202, 303]) == [101, 123, 303, 789]
assert unique_digits([123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909]) == [101, 123, 303, 505, 707, 789, 909]
assert unique_digits([123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == [101, 123, 303, 505, 707, 789, 909]
assert unique_digits([123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,