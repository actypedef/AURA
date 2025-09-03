"""
Write a function to convert polar coordinates to rectangular coordinates.
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
"""
import cmath

def polar_rect(r, theta):
    """
    Convert polar coordinates (r, theta) to rectangular coordinates (x, y).
    
    Parameters:
    r (float): The radius of the polar coordinate system.
    theta (float): The angle in radians of the polar coordinate system.
    
    Returns:
    tuple: A tuple containing the x and y coordinates in rectangular form.
    """
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (x, y)

# Test cases to verify the correctness of the function
assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))