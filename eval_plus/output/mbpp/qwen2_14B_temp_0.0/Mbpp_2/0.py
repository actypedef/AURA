"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(test_list1, test_list2):
    # Use a generator expression to find common elements and convert to a list
    res = [ele for ele in test_list1 if ele in test_list2]
    return res

# Test the function with the provided test case
assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))
