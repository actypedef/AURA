"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(nums):
    # Initialize two pointers
    i = 0
    j = 0
    
    # Iterate through the list
    while j < len(nums):
        # If the current element is not zero, swap it with the element at pointer i
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    
    return nums

# Test the function with the provided test case
assert move_zero([1, 0, 2, 0, 3, 4]) == [1, 2, 3, 4, 0, 0]