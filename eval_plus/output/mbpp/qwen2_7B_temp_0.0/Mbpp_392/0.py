"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    # Initialize a dictionary to store computed values of f(n)
    dp = [0] * (n + 1)
    
    # Base case: f(0) = 0
    dp[0] = 0
    
    # Compute f(i) for i from 1 to n
    for i in range(1, n + 1):
        # Calculate the maximum sum using the given formula
        dp[i] = max(dp[i // 2] + dp[i // 3] + dp[i // 4] + dp[i // 5], i)
    
    # Return the result for f(n)
    return dp[n]

# Test the function with the provided test case
assert get_max_sum(60) == 106