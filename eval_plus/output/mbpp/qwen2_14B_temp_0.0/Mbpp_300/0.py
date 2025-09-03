"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    # Initialize a list to store binomial coefficients
    C = [0] * (n + 1)
    C[0] = 1  # nC0 is 1
    
    # Calculate binomial coefficients using dynamic programming
    for i in range(1, n + 1):
        for j in range(i):
            C[j] = C[j] + C[j - 1]
    
    # Return the square of the binomial coefficient C[n]
    return C[n] * C[n]

# Test the function with the provided test case
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)