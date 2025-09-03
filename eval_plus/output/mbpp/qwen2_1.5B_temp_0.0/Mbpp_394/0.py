"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
def check_distinct(tup):
    """
    Check if given tuple contains no duplicates.

    Args:
    tup (tuple): The tuple to be checked.

    Returns:
    bool: True if the tuple contains no duplicates, False otherwise.
    """
    return len(set(tup)) == len(tup)

# Test cases
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 2, 3, 4, 5)) == True
assert check_distinct(('a', 'b', 'c')) == True
assert check_distinct(('a', 'a', 'b')) == False