"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""
import bisect

def last(nums, target):
    # Find the rightmost index where the target can be inserted to maintain sorted order
    i = bisect.bisect_right(nums, target)
    
    # Check if the found index is within the bounds of the list and the element at that index is equal to the target
    return i if i < len(nums) and nums[i] == target else -1

# Test the function with the provided test case
assert last([1, 2, 3], 1) == 0
