"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import cmath

def angle_complex(x, y):
    # Create a complex number from real and imaginary parts
    complex_num = x + y * 1j
    
    # Calculate the angle (phase) of the complex number
    angle = cmath.phase(complex_num)
    
    return angle

# Test the function with the provided test case
assert math.isclose(angle_complex(0, 1j), 1.5707963267948966, rel_tol=0.001)