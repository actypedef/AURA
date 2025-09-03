"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, n, i, k):
    # Initialize the dp array where dp[j] will store the maximum sum of increasing subsequence ending at index j
    dp = [0 for _ in range(n)]
    
    # Base case: The maximum sum for the first element is the element itself
    dp[0] = arr[0]
    
    # Fill the dp array for indices up to i
    for j in range(1, i + 1):
        max_sum = 0
        # Check all previous elements to find the maximum sum of increasing subsequence
        for k in range(j):
            if arr[k] < arr[j] and dp[k] > max_sum:
                max_sum = dp[k]
        dp[j] = max_sum + arr[j]
    
    # Include the k-th element if it forms an increasing subsequence with any element up to i
    for j in range(i + 1):
        if arr[j] < arr[k]:
            dp[k] = max(dp[k], dp[j] + arr[k])
    
    # Return the maximum sum found in the dp array
    return max(dp)

# Test the function with the provided test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
