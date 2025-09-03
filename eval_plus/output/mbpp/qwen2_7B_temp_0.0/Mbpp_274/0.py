"""
Write a python function that takes in a positive integer n and finds the sum of even index binomial coefficients.
assert even_binomial_Coeff_Sum(4) == 8
"""
def even_binomial_Coeff_Sum(n):
    # Initialize the result to store the sum of even index binomial coefficients
    res = 0
    
    # Iterate over the range from 0 to n (inclusive)
    for i in range(n + 1):
        # Check if the current index is even
        if i % 2 == 0:
            # Add the binomial coefficient at the current index to the result
            res += binom(i, i)
    
    return res

# Test the function with the provided test case
assert even_binomial_Coeff_Sum(4) == 8