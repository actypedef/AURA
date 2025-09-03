"""
Write a function to find the intersection of two arrays.
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
"""
def intersection_array(nums1, nums2):
    # Convert both lists to sets and find their intersection
    result = list(set(nums1) & set(nums2))
    return result

# Test the function with the provided test case
assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
