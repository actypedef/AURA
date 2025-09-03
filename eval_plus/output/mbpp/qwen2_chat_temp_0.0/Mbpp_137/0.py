"""
Write a function to find the ratio of zeroes to non-zeroes in an array of integers.
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""
# Importing the math module for mathematical operations
import math

def zero_count(arr):
    # Initialize counters for zeros and non-zeros
    count_zero = 0
    count_nonzero = 0
    
    # Iterate through each element in the array
    for i in range(len(arr)):
        # Check if the current element is zero
        if arr[i] == 0:
            count_zero += 1
        else:
            count_nonzero += 1
    
    # Calculate the total number of elements in the array
    total_elements = len(arr)
    
    # Calculate the ratio of zeros to non-zeros
    ratio = count_zero / total_elements
    
    return ratio

# Test the function with the provided test case
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)