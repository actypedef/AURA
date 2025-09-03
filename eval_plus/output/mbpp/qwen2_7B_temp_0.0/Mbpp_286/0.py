"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, n, k):
    # Calculate the maximum subarray sum for the original array
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1, n):
        curr_max = max(curr_max + arr[i], arr[i])
        max_so_far = max(max_so_far, curr_max)
    
    # Calculate the total sum of the original array
    total_sum = sum(arr)
    
    # If the total sum is negative, we can't get a positive sum by repeating
    if total_sum < 0:
        return max_so_far
    
    # Calculate the maximum subarray sum for the repeated array
    max_repeat = (k - 1) * total_sum + max_so_far
    
    return max_repeat

# Test the function with the provided test case
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30