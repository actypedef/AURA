"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
from typing import List

def maxAverageOfPath(cost: List[List[int]]) -> float:
    n = len(cost)
    # Initialize the DP table with zeros
    dp = [[0] * n for _ in range(n)]
    
    # Set the starting point of the DP table
    dp[0][0] = cost[0][0]
    
    # Fill the first row of the DP table
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    
    # Fill the first column of the DP table
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    
    # Fill the rest of the DP table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
    
    # Calculate the maximum average
    max_sum = dp[n - 1][n - 1]
    return max_sum / (2 * n - 1)

# Test the function with the provided test case
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
