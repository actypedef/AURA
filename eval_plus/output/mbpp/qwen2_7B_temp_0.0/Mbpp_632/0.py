"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(nums):
    # Initialize two pointers, one for non-zero elements and another for zero elements
    non_zero_index = 0
    
    # Iterate through the list
    for i in range(len(nums)):
        # If the current element is not zero, swap it with the element at non_zero_index
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1

# Test the function with the provided test case
assert move_zero([1, 0, 2, 0, 3, 4]) == [1, 2, 3, 4, 0, 0]
