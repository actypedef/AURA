"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import cmath

def angle_complex(real_part, imaginary_part):
    """
    Calculate the angle (in radians) of a complex number.

    Args:
    real_part (float): The real part of the complex number.
    imaginary_part (float): The imaginary part of the complex number.

    Returns:
    float: The angle of the complex number in radians.
    """
    # Create a complex number from the given real and imaginary parts
    complex_number = complex(real_part, imaginary_part)
    
    # Calculate the angle using cmath.phase()
    angle = cmath.phase(complex_number)
    
    return angle

# Test the function with provided data points
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)