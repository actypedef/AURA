"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def assert_and_tuples(tup1, tup2):
    # Extracting elements and tuples from the input tuples
    result = tuple(x - y for x, y in zip(tup1, tup2))
    return result

# Test cases to verify the correctness of the solution
assert assert_and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
assert assert_and_tuples((7, 8, 9, 10), (1, 2, 3, 4)) == (6, 6, 6, 6)
assert assert_and_tuples((1, 2, 3, 4), (5, 6, 7, 8)) == (-4, -4, -4, -4)