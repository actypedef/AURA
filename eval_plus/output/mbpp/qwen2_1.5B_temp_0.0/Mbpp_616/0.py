"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""
def tuple_modulo(tup1, tup2):
    # Check if both tuples have the same length
    assert len(tup1) == len(tup2), "Both tuples must have the same length"
    
    # Perform element-wise modulo operation
    result = tuple(a % b for a, b in zip(tup1, tup2))
    
    return result

# Test cases to verify the correctness of the solution
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
assert tuple_modulo((3, 8, 9, 10), (2, 3, 4, 5)) == (1, 5, 1, 0)
assert tuple_modulo((1, 2, 3, 4), (5, 6, 7, 8)) == (-4, -4, -4, -4)