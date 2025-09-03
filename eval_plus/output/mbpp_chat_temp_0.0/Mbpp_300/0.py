"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    # Initialize a list to store binomial coefficients
    C = [0] * (2 * n + 1)
    
    # Base case: C[0] is always 1
    C[0] = 1
    
    # Calculate binomial coefficients using Pascal's triangle
    for i in range(1, 2 * n + 1):
        C[i] = 0
        for j in range(min(i, n), -1, -1):
            C[j] += C[j - 1]
    
    # Initialize result variable
    res = 0
    
    # Sum up the squares of binomial coefficients
    for i in range(n + 1):
        res += C[i] ** 2
    
    return res

# Test the function with the provided test case
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)