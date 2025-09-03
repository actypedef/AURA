"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""
def big_diff(nums):
    # Calculate the maximum value in the list
    max_value = max(nums)
    
    # Calculate the minimum value in the list
    min_value = min(nums)
    
    # Return the difference between the maximum and minimum values
    return max_value - min_value

# Test the function with the provided test case
assert big_diff([1, 2, 3, 4]) == 3