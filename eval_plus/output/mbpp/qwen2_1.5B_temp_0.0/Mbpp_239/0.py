"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    # Initialize a list to store the number of sequences for each length up to n
    dp = [0] * (n + 1)
    
    # Base case: There's one way to form a sequence of length 1 (with any single number)
    dp[1] = 1
    
    # Fill the dp array using dynamic programming
    for i in range(2, n + 1):
        for j in range(i // 2, i + 1):
            if j <= m:
                dp[i] += dp[j - 1]
    
    return dp[n]

# Test cases to verify the correctness of the solution
assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 3) == 2
assert get_total_number_of_sequences(8, 6) == 19