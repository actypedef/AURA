"""
Given a square matrix of size N*N given as a list of lists, where each cell is associated with a specific cost. A path is defined as a specific sequence of cells that starts from the top-left cell move only right or down and ends on bottom right cell. We want to find a path with the maximum average over all existing paths. Average is computed as total cost divided by the number of cells visited in the path.
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
"""
def maxAverageOfPath(matrix):
    # Get the number of rows (N) in the matrix
    n = len(matrix)
    
    # Initialize a DP table with -1 values
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Define a recursive function to calculate the maximum average path
    def getMaxAvg(i, j):
        # Base case: if out of bounds, return negative infinity
        if i >= n or j >= n:
            return float('-inf')
        
        # If already calculated, return the stored value
        if dp[i][j] != -1:
            return dp[i][j]
        
        # Calculate the current cost and add it to the sum of costs
        curr_cost = matrix[i][j]
        sum_of_costs = curr_cost
        
        # Recursively calculate the maximum average for the next steps
        avg_right = getMaxAvg(i, j + 1)
        avg_down = getMaxAvg(i + 1, j)
        
        # Add the maximum average of the two possible directions
        sum_of_costs += max(avg_right, avg_down)
        
        # Store the result in the DP table
        dp[i][j] = sum_of_costs / (1 + max(avg_right, avg_down))
        
        return dp[i][j]
    
    # Start the calculation from the top-left corner
    return getMaxAvg(0, 0)

# Test the function with the provided test case
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2