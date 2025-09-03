"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(nums, n, k, m):
    # Initialize dp array where dp[i] will store the maximum sum of increasing subsequence ending at index i
    dp = [0] * (n + 1)
    
    # Iterate through each number in the list
    for i in range(1, n + 1):
        # Check all previous numbers to find the longest increasing subsequence ending at i
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + nums[i])
    
    # Find the maximum sum of increasing subsequence ending at index k
    max_sum = 0
    for i in range(k + 1, n + 1):
        max_sum = max(max_sum, dp[i])
    
    return max_sum

# Test the function with the provided test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11