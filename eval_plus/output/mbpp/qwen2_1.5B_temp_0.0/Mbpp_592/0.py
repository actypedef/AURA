"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
import math

def sum_of_product(n):
    # Calculate the sum of the product of consecutive binomial coefficients using the formula (2^n - 1)^2 / 4
    return int((2**n - 1)**2 / 4)

# Test cases to verify the correctness of the solution
assert sum_of_product(3) == 15
assert sum_of_product(4) == 80
assert sum_of_product(5) == 272