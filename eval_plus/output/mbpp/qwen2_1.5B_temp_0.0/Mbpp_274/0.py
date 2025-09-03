"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
import math

def even_binomial_Coeff_Sum(n):
    # Calculate the sum of even index binomial coefficients using the formula
    return int(math.pow(2, (n - 1)) / 2)

# Test cases to verify the correctness of the function
assert even_binomial_Coeff_Sum(4) == 8
assert even_binomial_Coeff_Sum(5) == 16
assert even_binomial_Coeff_Sum(6) == 32