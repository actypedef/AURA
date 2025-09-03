"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(list1, list2):
    # Use set intersection to find common elements between the two lists
    return set(list1) & set(list2)

# Test the function with the provided test case
assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))
