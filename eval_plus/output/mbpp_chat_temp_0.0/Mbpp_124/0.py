"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import cmath

def angle_complex(x, y):
    # Create a complex number from real part x and imaginary part y
    z = complex(x, y)
    
    # Calculate the angle (phase) of the complex number using cmath module
    return cmath.phase(z)

# Test the function with the provided test case
assert math.isclose(angle_complex(0, 1j), 1.5707963267948966, rel_tol=0.001)