"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
import math

def volume_sphere(radius):
    """
    Calculate the volume of a sphere given its radius.
    
    Args:
    radius (float): The radius of the sphere.
    
    Returns:
    float: The volume of the sphere.
    """
    return (4/3) * math.pi * radius**3

# Test the function
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)