"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
def max_of_nth(matrix, n):
    # Check if the input matrix is empty or the requested column index is out of range
    if not matrix or n < 0 or n >= len(matrix[0]):
        return None
    
    # Find the maximum value in the specified column
    max_value = float('-inf')
    for row in matrix:
        if row[n] > max_value:
            max_value = row[n]
    
    return max_value

# Test cases to verify the correctness of the solution
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
assert max_of_nth([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 1) == 80
assert max_of_nth([], 3) == None
assert max_of_nth([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1) == None