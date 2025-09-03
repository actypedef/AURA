"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
def count_samepair(nums1, nums2, nums3):
    # Use zip to iterate over all three lists simultaneously and count elements that match at each index
    return sum(x == y == z for x, y, z in zip(nums1, nums2, nums3))

# Test the function with the provided test case
assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3