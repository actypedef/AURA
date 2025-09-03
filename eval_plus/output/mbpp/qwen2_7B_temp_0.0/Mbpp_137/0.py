"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
import math

def zero_count(arr):
    # Calculate the total number of elements in the array
    n = len(arr)
    
    # Count the number of zeroes in the array
    count_zero = arr.count(0)
    
    # Calculate the ratio of zeroes to non-zeroes
    if count_zero == 0:
        return 0
    else:
        return round(count_zero / (n - count_zero), 6)

# Test the function with the provided test case
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)