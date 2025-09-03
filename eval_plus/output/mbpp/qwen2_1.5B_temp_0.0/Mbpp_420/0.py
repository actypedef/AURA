"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_Sum(n):
    # Calculate the sum of first n even natural numbers using formula
    return (n * (n + 1)) ** 2

# Test cases to verify the correctness of the function
assert cube_Sum(2) == 72
assert cube_Sum(3) == 288
assert cube_Sum(4) == 672
assert cube_Sum(5) == 1512