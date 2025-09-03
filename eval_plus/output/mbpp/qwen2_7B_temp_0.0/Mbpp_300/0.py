"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    # Initialize a 2D array for dynamic programming
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: There's one way to have equal sums for both halves when n is 0
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    
    # The result is the number of ways to partition n into two equal parts
    return dp[n][n]

# Test the function with the provided test case
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)