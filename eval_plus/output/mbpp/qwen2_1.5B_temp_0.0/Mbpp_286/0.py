"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, n, k):
    # Calculate the maximum subarray sum for one repetition of the array
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    
    # Multiply the maximum subarray sum by k to get the result
    return max_sum * k

# Test cases
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-5, -1, -8, -9], 2, 2) == -16
assert max_sub_array_sum_repeated([1, 2, 3, 4, 5], 3, 1) == 15