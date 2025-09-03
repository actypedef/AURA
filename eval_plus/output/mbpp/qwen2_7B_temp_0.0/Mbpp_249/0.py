"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""
def intersection_array(nums1, nums2):
    # Use set intersection to find common elements between nums1 and nums2
    return list(set(nums1) & set(nums2))

# Test the function with the provided test case
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
