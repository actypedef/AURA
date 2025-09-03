"""
Write a python function to move all zeroes to the end of the given list.
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
"""
def move_zero(nums):
    # Count the number of zeroes in the list
    num_zeroes = nums.count(0)
    
    # Remove all zeroes from the list
    while 0 in nums:
        nums.remove(0)
    
    # Append the counted zeroes to the end of the list
    for i in range(num_zeroes):
        nums.append(0)
    
    return nums

# Test the function with the provided test case
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
