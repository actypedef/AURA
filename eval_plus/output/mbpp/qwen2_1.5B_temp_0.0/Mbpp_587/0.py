"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""
def list_tuple(lst):
    """
    Convert a list to a tuple.

    Args:
    lst (list): The input list to be converted.

    Returns:
    tuple: The converted tuple.
    """
    return tuple(lst)

# Test the function
assert list_tuple([5, 10, 7, 4, 15, 3]) == (5, 10, 7, 4, 15, 3)