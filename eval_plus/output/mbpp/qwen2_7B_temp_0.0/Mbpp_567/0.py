"""
Write a function to check whether a specified list is sorted or not.
assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
"""
def issort_list(nums):
    # Check if the list is sorted in ascending order
    return nums == sorted(nums)

# Test the function with the provided test case
assert issort_list([1, 2, 4, 6, 8, 10, 12, 14, 16, 17]) == True
