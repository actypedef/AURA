"""
Write a function to find the size in bytes of the given tuple.
assert tuple_size(("A", 1, "B", 2, "C", 3) ) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
"""
import sys

def tuple_size(test_tup):
    # Calculate the size of the tuple in bytes using sys.getsizeof()
    res = sys.getsizeof(test_tup)
    return res

# Test the function with the provided test case
assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
