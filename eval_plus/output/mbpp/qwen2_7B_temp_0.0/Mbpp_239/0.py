"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    # Initialize a 2D array to store the number of sequences
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j == 1:
                dp[i][j] = i
            else:
                dp[i][j] = dp[i - 1][j] + dp[i // 2][j - 1]
    
    return dp[m][n]

# Test the function with the provided test case
assert get_total_number_of_sequences(10, 4) == 4