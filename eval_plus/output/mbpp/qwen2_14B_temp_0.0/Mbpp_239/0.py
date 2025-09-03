"""
Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
assert get_total_number_of_sequences(10, 4) == 4
"""
def get_total_number_of_sequences(m, n):
    # Initialize a table to store results of subproblems
    T = [[0 for j in range(n + 1)] for i in range(m + 1)]
    
    # If there are 0 elements in the sequence, there is one way (empty sequence)
    for i in range(m + 1):
        T[i][0] = 1
    
    # Fill the table using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Sum up all valid sequences ending with any number from 1 to i
            T[i][j] = T[i - 1][j] + T[i // 2][j - 1]
    
    # Return the total number of sequences of length n with elements <= m
    return T[m][n]

# Test the function with the provided test case
assert get_total_number_of_sequences(10, 4) == 4
