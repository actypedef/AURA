"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    # Initialize a 2D list for memoization
    dp = [[-1] * (n + 1) for _ in range(m + 1)]
    
    def helper(x, y):
        # Base case: if sequence length is 1, return x
        if y == 1:
            return x
        # If already computed, return from memoization table
        if dp[x][y] != -1:
            return dp[x][y]
        
        total_sequences = 0
        
        # Iterate through all possible values for the next element
        for i in range(x // 2, x + 1):
            total_sequences += helper(i, y - 1)
        
        # Store the result in memoization table
        dp[x][y] = total_sequences
        return dp[x][y]

    # Sum up all possible sequences starting from each value from 1 to m
    return sum(helper(i, n) for i in range(1, m + 1))

# Test the function with the provided test case
assert get_total_number_of_sequences(10, 4) == 4