"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Check if the matrix has 4 rows and 4 columns
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        return False
    
    # Calculate the sum of the first row to use as a reference
    ref = sum(matrix[0])
    
    # Check sums of all rows
    for i in range(1, 4):
        if sum(matrix[i]) != ref:
            return False
    
    # Check sums of all columns
    for j in range(4):
        if sum(matrix[i][j] for i in range(4)) != ref:
            return False
    
    # Check sum of the main diagonal
    if sum(matrix[i][i] for i in range(4)) != ref:
        return False
    
    # Check sum of the secondary diagonal
    if sum(matrix[i][3-i] for i in range(4)) != ref:
        return False
    
    # If all checks pass, it's a magic square
    return True

# Test the function with the provided test case
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True