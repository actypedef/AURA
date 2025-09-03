"""
Write a function to extract the elementwise and tuples from the given two tuples.
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
"""
def and_tuples(test_tup1, test_tup2):
    # Use zip to iterate over both tuples simultaneously
    # Use map with lambda to compare elements and return 1 if they are equal, otherwise 0
    res = tuple(map(lambda ele1, ele2: int(ele1 == ele2), test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)