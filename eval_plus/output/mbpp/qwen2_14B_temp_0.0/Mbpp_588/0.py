"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""
def big_diff(nums):
    # Calculate the difference between the maximum and minimum values in the list
    diff = max(nums) - min(nums)
    return diff

# Test the function with the provided test case
assert big_diff([1, 2, 3, 4]) == 3
