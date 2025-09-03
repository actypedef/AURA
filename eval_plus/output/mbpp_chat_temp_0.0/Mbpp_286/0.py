"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, n, k):
    # Calculate the maximum subarray sum for the original array
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    
    # Calculate the total sum of the array
    total_sum = sum(arr)
    
    # If the total sum is positive, add it (k-1) times to the max_so_far
    if total_sum > 0:
        max_so_far += (total_sum * (k - 1))
    
    return max_so_far

# Test the function with the provided test case
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30