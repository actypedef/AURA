"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(radius, height):
    """
    Calculate the volume of a cone.

    Args:
    radius (float): The radius of the base of the cone.
    height (float): The height of the cone.

    Returns:
    float: The volume of the cone.
    """
    return (1/3) * math.pi * radius**2 * height

# Test cases to verify the correctness of the function
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)