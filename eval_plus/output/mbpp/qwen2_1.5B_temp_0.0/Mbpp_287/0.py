"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    return sum(i**2 for i in range(2, 2*n+1, 2))

# Test cases to verify the correctness of the function
assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 84
assert square_Sum(5) == 140