"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""
def tuple_modulo(test_tup1, test_tup2):
    # Calculate the element-wise modulo using a generator expression
    res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
