"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
def max_of_nth(lst, n):
    # Extract the nth column from each row using list comprehension
    nth_column = [row[n] for row in lst]
    # Return the maximum value from the extracted column
    return max(nth_column)

# Test the function with the provided test case
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
