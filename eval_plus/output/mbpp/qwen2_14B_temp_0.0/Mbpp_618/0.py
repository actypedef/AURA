"""
Write a function to divide two lists element wise.
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
"""
def div_list(nums1, nums2):
    # Use list comprehension to divide elements of nums1 by elements of nums2
    result = [nums1[i] / nums2[i] for i in range(len(nums1))]
    return result

# Test the function with the provided test case
assert div_list([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
