"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Calculate the sum of the first row to use as a reference
    n = len(matrix)
    sum_of_first_row = sum(matrix[0])
    
    # Check sums of all rows
    for row in matrix:
        if sum(row) != sum_of_first_row:
            return False
    
    # Check sums of all columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != sum_of_first_row:
            return False
    
    # Check sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != sum_of_first_row:
        return False
    
    # Check sum of the secondary diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != sum_of_first_row:
        return False
    
    return True

# Test the function with the provided test case
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True