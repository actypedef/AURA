"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""
def closest_num(n):
    """
    Find the closest smaller number than n.

    Args:
    n (int): The number for which to find the closest smaller number.

    Returns:
    int: The closest smaller number than n.
    """
    # Subtract 1 from n to get the closest smaller number
    return n - 1

# Test cases to verify the correctness of the solution
assert closest_num(11) == 10
assert closest_num(23) == 22
assert closest_num(7) == 6
assert closest_num(99) == 98