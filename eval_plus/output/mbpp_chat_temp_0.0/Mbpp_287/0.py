"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    # Calculate the sum of squares of the first n even natural numbers
    return int((n * (n + 1) * (2 * n + 1)) / 3)

# Test the function with the provided test case
assert square_Sum(2) == 20
