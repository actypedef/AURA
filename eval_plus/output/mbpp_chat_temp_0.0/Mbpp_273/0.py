"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
def substract_elements(test_tup1, test_tup2):
    # Using list comprehension to subtract elements of both tuples at the same index
    res = tuple(x - y for x, y in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
