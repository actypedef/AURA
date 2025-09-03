"""
Write a function to find the pairwise addition of the neighboring elements of the given tuple.
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
"""
def add_pairwise(test_tup):
    # Use list comprehension to iterate through pairs of consecutive elements
    res = tuple(x + y for x, y in zip(test_tup[:-1], test_tup[1:]))
    return res

# Test the function with the provided test case
assert add_pairwise((1, 5, 7, 8, 10)) == (6, 12, 15, 18)
