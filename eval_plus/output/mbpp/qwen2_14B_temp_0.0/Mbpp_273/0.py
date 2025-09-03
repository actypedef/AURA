"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
def substract_elements(test_tup1, test_tup2):
    # Subtract elements of the second tuple from the first tuple using zip
    res = tuple(ele1 - ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
    return res

# Test the function with the provided test case
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
