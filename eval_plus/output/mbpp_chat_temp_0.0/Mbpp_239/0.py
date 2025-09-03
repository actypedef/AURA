"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    # Initialize a 2D list (m+1)x(n+1) with zeros
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    
    # Iterate over all possible values of m and n
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If there's only one position in the sequence
            if j == 1:
                dp[i][j] = i
            else:
                # Calculate the number of sequences ending with i
                dp[i][j] = dp[i - 1][j] + dp[i // 2][j - 1]
    
    # Return the total number of sequences of length n with elements up to m
    return dp[m][n]

# Test the function with the provided test case
assert get_total_number_of_sequences(10, 4) == 4