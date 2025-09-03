"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, n, k):
    # Initialize variables to store the maximum sum and current sum
    max_so_far = float('-inf')
    curr_max = 0
    
    # Iterate through each element in the repeated array
    for i in range(n * k):
        curr_max += arr[i % n]
        
        # Update the maximum sum found so far
        if curr_max > max_so_far:
            max_so_far = curr_max
        
        # If current sum becomes negative, reset it to zero
        if curr_max < 0:
            curr_max = 0
    
    return max_so_far

# Test the function with the provided test case
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30