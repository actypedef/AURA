"""
Write a function to convert a tuple to a string.
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))==("exercises")
"""
def tup_string(tup):
    """
    Convert a tuple to a string.

    Args:
    tup (tuple): The input tuple.

    Returns:
    str: The converted string.
    """
    return ''.join(tup)

# Test cases
assert tup_string(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')) == "exercises"