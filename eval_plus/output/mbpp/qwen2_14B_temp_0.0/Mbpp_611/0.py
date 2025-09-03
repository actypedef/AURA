"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
def max_of_nth(matrix, n):
    # Extract the nth column from each row in the matrix
    column = [row[n] for row in matrix]
    # Return the maximum value from the extracted column
    return max(column)

# Test the function with the provided test case
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
