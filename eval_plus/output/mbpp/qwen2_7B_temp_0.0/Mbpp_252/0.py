"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(z):
    # Convert the complex number to polar coordinates
    return cmath.polar(complex(z))

# Test the function with the provided test case
assert convert(1) == (1.0, 0.0)
