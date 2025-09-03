"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
# Importing the cmath module for complex number operations
import cmath

def convert(z):
    # Using the cmath.polar() method to convert a complex number to polar coordinates
    return cmath.polar(z)

# Test case to verify the correctness of the function
assert convert(1) == (1.0, 0.0)
