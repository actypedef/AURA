"""
Write a python function to find the sum of the product of consecutive binomial co-efficients.
assert sum_Of_product(3) == 15
"""
import math

def sum_Of_product(n):
    # Calculate the sum of the product of consecutive binomial coefficients
    return int(math.pow(2, n - 1) * (math.pow(2, n) - 1))

# Test the function with the provided test case
assert sum_Of_product(3) == 15
