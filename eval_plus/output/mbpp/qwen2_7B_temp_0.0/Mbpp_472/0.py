"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(nums):
    # Sort the list to ensure it's in ascending order
    nums.sort()
    
    # Iterate through the sorted list to check for consecutive numbers
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i + 1]:
            return False
    
    # If all pairs of numbers are consecutive, return True
    return True

# Test the function with the provided test case
assert check_Consecutive([1, 2, 3, 4, 5]) == True
