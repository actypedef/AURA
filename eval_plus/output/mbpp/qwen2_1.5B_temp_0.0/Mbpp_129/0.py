"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Check if the matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        return False
    
    # Calculate the sum of each row, column, and diagonal
    rows_sum = [sum(row) for row in matrix]
    cols_sum = [sum(col) for col in zip(*matrix)]
    diag_sum1 = sum(matrix[i][i] for i in range(len(matrix)))
    diag_sum2 = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
    
    # Check if all sums are equal
    return all(sum == rows_sum[0] for sum in rows_sum) and \
           all(sum == cols_sum[0] for sum in cols_sum) and \
           sum == diag_sum1 and sum == diag_sum2

# Test the function