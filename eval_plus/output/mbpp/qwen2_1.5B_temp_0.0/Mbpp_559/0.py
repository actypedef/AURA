"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""
def max_sub_array_sum(nums, k):
    # Initialize variables to keep track of the maximum sum found so far and the current sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Iterate through each number in the list
    for i in range(len(nums)):
        # Add the current number to the current sum
        current_sum += nums[i]
        
        # If the current sum exceeds the maximum sum, update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
        
        # If the current sum becomes negative, reset it to zero as we are looking for the maximum sum
        if current_sum < 0:
            current_sum = 0
    
    # Return the maximum sum found
    return max_sum

# Test the function with the provided test case
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7