"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def even_binomial_Coeff_Sum(n):
    # Calculate the sum of even-indexed binomial coefficients using bit manipulation
    return (1 << (n - 1))

# Test the function with the provided test case
assert even_binomial_Coeff_Sum(4) == 8