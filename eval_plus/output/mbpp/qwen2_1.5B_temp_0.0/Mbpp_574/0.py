"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
import math

def surfacearea_cylinder(radius, height):
    """
    Calculate the surface area of a cylinder.

    Args:
    radius (float): The radius of the cylinder's base.
    height (float): The height of the cylinder.

    Returns:
    float: The surface area of the cylinder.
    """
    return 2 * math.pi * radius * (radius + height)

# Test cases to verify the correctness of the function
assert surfacearea_cylinder(10,5) == 942.45
assert surfacearea_cylinder(7,3) == 185.496
assert surfacearea_cylinder(1,1) == 6.28318