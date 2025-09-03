"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
import numpy as np

def zero_ratio(arr):
    """
    Calculate the ratio of zeroes to non-zero elements in an array.

    Parameters:
    arr (list): A list of integers.

    Returns:
    float: The ratio of zeroes to non-zero elements.
    """
    total_elements = len(arr)
    zero_count = sum(1 for x in arr if x == 0)
    return zero_count / total_elements

# Test the function
arr = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]