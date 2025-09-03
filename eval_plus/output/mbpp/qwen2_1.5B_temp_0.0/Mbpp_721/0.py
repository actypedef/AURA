"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
def maxAverageOfPath(matrix):
    n = len(matrix)
    # Initialize dp array with zeros
    dp = [[0] * n for _ in range(n)]
    
    # Fill the first row and column of dp array
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    for j in range(1, n):
        dp[j][0] = dp[j-1][0] + matrix[j][0]
    
    # Fill the rest of the dp array
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # Calculate the maximum average
    max_avg = float('-inf')
    for i in range(n):
        for j in range(n):
            avg = dp[i][j] / (i+1) * (j+1)
            if avg > max_avg:
                max_avg = avg
    
    return max_avg

# Test cases
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2