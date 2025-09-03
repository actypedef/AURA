"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
def bell_number(n):
    # Initialize a 2D list (matrix) to store Bell numbers
    B = [[0 for i in range(n + 1)] for j in range(n + 1)]
    
    # Base case: The first Bell number is 1
    B[0][0] = 1
    
    # Fill the matrix using the recursive relation
    for i in range(1, n + 1):
        B[i][0] = B[i - 1][i - 1]
        for j in range(1, i + 1):
            B[i][j] = B[i - 1][j - 1] + B[i][j - 1]
    
    # Return the nth Bell number
    return B[n][0]

# Test the function with the provided test case
assert bell_number(2) == 2