"""
Write a function to find the sum of the largest contiguous sublist in the given list.
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""
def max_sub_array_sum(a, size):
    # Initialize variables to store the maximum sum so far and the current sum
    max_so_far = -9999999999999999
    max_ending_here = 0
    
    # Iterate through each element in the array
    for i in range(0, size):
        # Update the current sum by adding the current element
        max_ending_here += a[i]
        
        # If the current sum exceeds the maximum sum found so far, update it
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        # If the current sum becomes negative, reset it to zero
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

# Test the function with the provided test case
assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7