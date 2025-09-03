"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""
def get_max_sum(n):
    # Initialize a list to store maximum sums for numbers up to n
    dp = [0] * (n + 1)
    
    # Iterate from 1 to n to fill the dp array
    for i in range(1, n + 1):
        # Calculate the sum of divided values
        sum_divided = dp[int(i / 2)] + dp[int(i / 3)] + dp[int(i / 4)]
        # Choose the maximum between the current number and the sum of divided values
        dp[i] = max(i, sum_divided)
    
    # Return the maximum sum for n
    return dp[n]

# Test the function with the provided test case
assert get_max_sum(60) == 106
