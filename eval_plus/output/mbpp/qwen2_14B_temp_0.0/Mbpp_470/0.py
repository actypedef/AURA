"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(test_tup):
    # Create a new tuple by adding each element with its next neighbor
    res = tuple(b + a for a, b in zip(test_tup, test_tup[1:]))
    return res

# Test the function with the provided test case
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
