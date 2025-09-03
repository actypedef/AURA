"""
Write a python function to convert complex numbers to polar coordinates.
assert convert(1) == (1.0, 0.0)
"""
import cmath

def convert(complex_num):
    """
    Convert a complex number to polar coordinates.

    Args:
    complex_num (complex): The complex number to be converted.

    Returns:
    tuple: A tuple containing the magnitude and phase angle of the complex number in radians.
    """
    return cmath.polar(complex_num)

# Test cases
assert convert(1) == (1.0, 0.0)
