"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""
import math 

def find_Index(N): 
    # Calculate the index using the formula for the smallest triangular number with n digits
    return int(math.ceil((9 * (10 ** (N - 1))) ** 0.5))

# Test the function with the provided test case
assert find_Index(2) == 4
