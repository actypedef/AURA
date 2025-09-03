"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import cmath
import math

def angle_complex(x, y):
    # Create a complex number from real (x) and imaginary (y) parts
    z = complex(x, y)
    # Calculate the angle of the complex number
    angle = cmath.phase(z)
    return angle

# Test the function with the provided test case
assert math.isclose(angle_complex(0, 1j), 1.5707963267948966, rel_tol=0.001)
