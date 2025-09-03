"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Calculate the sum of the first row to use as a reference
    n = len(matrix)
    magic_sum = sum(matrix[0])
    
    # Check sums of all rows
    for i in range(1, n):
        if sum(matrix[i]) != magic_sum:
            return False
    
    # Check sums of all columns
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_sum:
            return False
    
    # Check sum of main diagonal
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    
    # Check sum of secondary diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_sum:
        return False
    
    # If all checks pass, it's a magic square
    return True

# Test the function with the provided test case
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True