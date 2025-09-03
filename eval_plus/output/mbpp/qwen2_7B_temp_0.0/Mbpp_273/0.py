"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
def substract_elements(test_tup1, test_tup2):
    # Using zip to iterate over both tuples simultaneously and subtracting corresponding elements
    res = tuple(a - b for a, b in zip(test_tup1, test_tup2))
    return res

# Test case to verify the function works as expected
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
