"""
Write a python function to check whether the given list contains consecutive numbers or not.
assert check_Consecutive([1,2,3,4,5]) == True
"""
def check_Consecutive(nums):
    # Check if the length of the list is 0 or 1, return True as they are trivially consecutive
    if len(nums) <= 1:
        return True
    
    # Sort the list to ensure consecutive order
    nums.sort()
    
    # Iterate through the sorted list and check for consecutive elements
    for i in range(len(nums) - 1):
        # If any two adjacent elements differ by more than 1, return False
        if nums[i + 1] - nums[i] > 1:
            return False
    
    # If no non-consecutive elements were found, return True
    return True

# Test the function with the provided test case
assert check_Consecutive([1, 2, 3, 4, 5]) == True