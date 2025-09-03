"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(nums):
    """
    Move all zeroes to the end of the given list.
    
    Args:
    nums (list): The input list containing integers.
    
    Returns:
    list: The modified list with all zeroes moved to the end.
    """
    # Initialize pointers for non-zero elements and the end of the list
    i = 0
    j = len(nums) - 1
    
    while i < j:
        # If the current element is zero, swap it with the element at the end of the list
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
            
    return nums

# Test cases to verify the correctness of the solution
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([0,1,0,3,12]) == [1,3,12,0,0]
assert move_zero([0,0,0,0]) == [0,0,0,0]
assert move_zero([1,2,3]) == [1,2,3]