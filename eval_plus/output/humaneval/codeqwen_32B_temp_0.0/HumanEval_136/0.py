
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    neg = [i for i in lst if i < 0]
    pos = [i for i in lst if i > 0]
    return (max(neg) if neg else None, min(pos) if pos else None)

# Test cases
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6]) == (-1, None)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6]) == (None, 1)
assert largest_smallest_integers([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (-1, 1)
assert largest_smallest_integers([-1, -2, -3, -4, -5, -6, 0, 1, 2, 3, 4, 5, 6, 7, 8, 