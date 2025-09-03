"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize a list to store the maximum sum for each index
    dp = [0] * n
    
    # Base case: The maximum sum at the first index is the value at that index itself
    dp[0] = arr[0]
    
    # Fill the dp array using dynamic programming
    for j in range(1, n):
        dp[j] = arr[j]
        for m in range(j):
            if arr[m] < arr[j]:
                dp[j] = max(dp[j], dp[m] + arr[j])
    
    # Return the maximum sum of increasing subsequence up to index i including the kth element
    return dp[i] + arr[k]

# Test the function with the provided test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11