"""
Write a function to calculate whether the matrix is a magic square.
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
"""
def magic_square_test(matrix):
    # Calculate the sum of each row
    row_sums = [sum(row) for row in matrix]
    
    # Calculate the sum of each column
    col_sums = [sum(col) for col in zip(*matrix)]
    
    # Calculate the sum of the main diagonal
    diag_sum_1 = sum(matrix[i][i] for i in range(len(matrix)))
    
    # Calculate the sum of the secondary diagonal
    diag_sum_2 = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
    
    # Check if all sums are equal
    all_equal = len(set(row_sums + col_sums + [diag_sum_1, diag_sum_2])) == 1
    
    return all_equal

# Test the function with the provided test case
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True