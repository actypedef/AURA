"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(z):
    # Convert the complex number z to its polar coordinate representation
    return cmath.polar(complex(z))

# Test the function with the provided test case
assert convert(1) == (1.0, 0.0)
