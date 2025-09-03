"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
def maxAverageOfPath(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)
    
    # Initialize a DP table with the same dimensions as the input matrix
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Set the starting point in the DP table
    dp[0][0] = matrix[0][0]
    
    # Fill the first row of the DP table
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + matrix[0][i]
    
    # Fill the first column of the DP table
    for j in range(1, n):
        dp[j][0] = dp[j - 1][0] + matrix[j][0]
    
    # Fill the rest of the DP table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
    
    # Calculate the maximum average path length
    max_average_path_length = dp[n - 1][n - 1] / (2 * n - 1)
    
    return max_average_path_length

# Test the function with the provided test case
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2