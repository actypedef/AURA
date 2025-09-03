"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""
def find_dissimilar(test_tup1, test_tup2):
    # Convert tuples to sets and use symmetric difference to find dissimilar elements
    res = tuple(set(test_tup1) ^ set(test_tup2))
    return res

# Test the function with the provided test case
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
