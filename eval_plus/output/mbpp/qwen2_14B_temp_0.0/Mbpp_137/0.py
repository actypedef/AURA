"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
import math

def zero_count(arr):
    # Initialize counters for zeroes and non-zeroes
    zero_count = 0
    non_zero_count = 0
    
    # Iterate through the array to count zeroes and non-zeroes
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    
    # Calculate the ratio of zeroes to non-zeroes
    zero_ratio = zero_count / non_zero_count
    
    return zero_ratio

# Test the function with the provided test case
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)