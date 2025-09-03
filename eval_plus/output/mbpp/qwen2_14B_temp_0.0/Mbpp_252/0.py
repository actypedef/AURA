"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(complex_num):
    # Convert complex number to polar coordinates
    polar_coordinates = cmath.polar(complex_num)
    return polar_coordinates

# Test the function with the provided test case
assert convert(1) == (1.0, 0.0)
