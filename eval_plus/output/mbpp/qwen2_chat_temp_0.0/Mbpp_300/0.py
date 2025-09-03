"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
# Importing the comb function from the math module for combination calculations
from math import comb

def count_binary_seq(n):
    # Initialize result variable to store the count of valid binary sequences
    res = 0
    
    # Iterate over each possible number of set bits (i) from 0 to n
    for i in range(n + 1):
        # Calculate the number of ways to choose i bits out of n for the first half
        # and also for the second half, then square it to account for both halves
        res += comb(n, i) ** 2
    
    # Return the total count of valid binary sequences
    return res

# Test the function with the provided test case
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)