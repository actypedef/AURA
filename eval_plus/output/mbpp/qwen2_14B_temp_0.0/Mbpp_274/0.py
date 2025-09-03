"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
import math 

def even_binomial_Coeff_Sum(n): 
    # Initialize sum to 0
    Sum = 0
    # Iterate through the first half of the binomial coefficients
    for k in range(0, n + 1): 
        # Add the binomial coefficient at even index
        Sum += math.comb(n, k) 
    # Return the sum of even index binomial coefficients
    return Sum 

# Test the function with the provided test case
assert even_binomial_Coeff_Sum(4) == 8
