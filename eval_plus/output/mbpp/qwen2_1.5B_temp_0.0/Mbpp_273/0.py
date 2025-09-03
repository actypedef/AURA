"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
def substract_elements(tuple1, tuple2):
    # Subtracting corresponding elements from tuple1 by tuple2
    result = tuple(a - b for a, b in zip(tuple1, tuple2))
    return result

# Test cases to verify the correctness of the solution
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
assert substract_elements((1, 2, 3), (4, 5, 6)) == (-3, -3, -3)
assert substract_elements((-1, -2, -3), (-4, -5, -6)) == (3, 3, 3)