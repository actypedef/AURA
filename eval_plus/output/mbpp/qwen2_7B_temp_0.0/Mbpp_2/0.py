"""
Write a function to find the shared elements from the given two lists.
assert set(similar_elements((3, 4, 5, 6),(5, 7, 4, 10))) == set((4, 5))
"""
def similar_elements(nums1, nums2):
    # Convert both lists to sets and find their intersection
    return list(set(nums1) & set(nums2))

# Test the function with the provided test case
assert set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))) == set((4, 5))
