"""
Write a function to find the union of the elements of two given tuples and output them in sorted order.
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
"""
def union_elements(test_tup1, test_tup2):
    # Combine both tuples using set union and convert back to tuple
    res = tuple(sorted(set(test_tup1) | set(test_tup2)))
    return res

# Test the function with the provided test case
assert union_elements((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)
