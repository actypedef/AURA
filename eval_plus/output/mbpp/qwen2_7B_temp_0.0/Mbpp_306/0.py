"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize a list to store the maximum sum for each index
    dp = [0] * n
    
    # Copy the original array into the dp array
    for j in range(n):
        dp[j] = arr[j]
    
    # Iterate through the array to fill the dp table
    for j in range(1, n):
        if arr[j] > arr[i]:
            dp[j] = max(dp[j], dp[i] + arr[j])
    
    # Return the maximum sum including the kth element
    return dp[k]

# Test the function with the provided test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
