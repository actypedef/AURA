"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""
def max_sub_array_sum(a, size):
    # Initialize variables to store the maximum sum so far and the current sum
    max_so_far = float('-inf')
    curr_max = 0
    
    for i in range(0, size):
        # Update the current sum by adding the current element
        curr_max = curr_max + a[i]
        
        # If the current sum is greater than the maximum sum, update the maximum sum
        if (max_so_far < curr_max):
            max_so_far = curr_max
        
        # If the current sum becomes negative, reset it to zero
        if curr_max < 0:
            curr_max = 0
    
    return max_so_far

# Test the function with the provided test case
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7