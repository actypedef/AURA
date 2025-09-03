

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
def incr_list(l: list) -> list:
    # Increment each element in the list by 1
    return [x + 1 for x in l]

# Test cases to verify the correctness of the function
assert incr_list([1, 2, 3]) == [2, 3, 4], "Test case 1 failed"
assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124], "Test case 2 failed"
