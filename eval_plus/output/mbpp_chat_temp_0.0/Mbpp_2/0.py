"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(test_tup1, test_tup2):
    # Use set intersection to find common elements between the two tuples
    res = tuple(set(test_tup1) & set(test_tup2))
    return res

# Test the function with the provided test case
assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))
