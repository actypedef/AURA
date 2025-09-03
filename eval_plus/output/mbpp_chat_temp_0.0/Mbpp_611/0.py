"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
def max_of_nth(matrix, n):
    # Extract the nth element from each sublist in the matrix
    nth_elements = [row[n] for row in matrix]
    # Return the maximum value among the extracted elements
    return max(nth_elements)

# Test the function with the provided test case
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
