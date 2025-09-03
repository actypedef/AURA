"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    # Initialize an array to store the Newman-Conway sequence values
    dp = [0] * (n + 1)
    
    # Base cases for the Newman-Conway sequence
    dp[1], dp[2] = 1, 1
    
    # Fill the array using the recurrence relation
    for i in range(3, n + 1):
        dp[i] = dp[dp[i - 1]] + dp[i - dp[i - 1]]
    
    # Return the nth value of the sequence
    return dp[n]

# Test the function with the provided test case
assert sequence(10) == 6