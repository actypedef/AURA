"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
import sys

def kadane(arr):
    # Initialize maximum sum and current sum
    max_so_far = -sys.maxsize
    max_ending_here = 0
    
    for i in range(len(arr)):
        # Update current sum
        max_ending_here = max_ending_here + arr[i]
        
        # Update maximum sum if current sum is greater
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        # Reset current sum if it becomes negative
        if max_ending_here < 0:
            max_ending_here = 0
    
    return max_so_far

def max_sub_array_sum_repeated(arr, n, k):
    # Calculate sum of the entire array
    sum_all = sum(arr)
    
    # Find maximum subarray sum using Kadane's algorithm
    max_kadane = kadane(arr)
    
    # If k is 1, return the result of Kadane's algorithm
    if k == 1:
        return max_kadane
    
    # If sum of the array is positive, use it to form a larger sum
    if sum_all > 0:
        return max_kadane + (sum_all * (k - 2)) + kadane(arr * 2)
    else:
        # If sum of the array is negative, consider the best between two Kadane results
        return max(max_kadane, max_kadane + (sum_all * (k - 2)))

# Test the function with the provided test case
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30