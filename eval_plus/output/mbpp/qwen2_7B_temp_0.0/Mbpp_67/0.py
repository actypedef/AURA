"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    # Initialize a 2D list to store Bell numbers
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base case: Bell number for n=0 is 1
    dp[0][0] = 1
    
    # Fill the table using the Bell number recurrence relation
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][i - 1]
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    
    # Return the Bell number for n
    return dp[n][0]

# Test the function with the provided test case
assert bell_number(2) == 2