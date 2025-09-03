"""
Write a function to convert a given tuple of positive integers into a single integer.
assert tuple_to_int((1,2,3))==123
"""
def tuple_to_int(tup):
    """
    Convert a given tuple of positive integers into a single integer.

    Args:
    tup (tuple): A tuple of positive integers.

    Returns:
    int: The resulting integer after concatenating all elements of the tuple.
    """
    return int(''.join(map(str, tup)))

# Test cases to verify the correctness of the solution
assert tuple_to_int((1, 2, 3)) == 123
assert tuple_to_int((4, 5, 6, 7)) == 4567
assert tuple_to_int((8, 9, 0)) == 890
assert tuple_to_int((10, 20, 30, 40, 50)) == 1020304050