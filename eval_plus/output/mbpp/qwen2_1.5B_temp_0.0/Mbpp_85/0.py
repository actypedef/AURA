"""
Write a function to find the surface area of a sphere.
assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
"""
import math

def surface_area_sphere(radius):
    """
    Calculate the surface area of a sphere given its radius.

    Args:
    radius (float): The radius of the sphere.

    Returns:
    float: The surface area of the sphere.
    """
    return 4 * math.pi * radius ** 2

# Test cases to verify the correctness of the function
assert math.isclose(surface_area_sphere(10), 1256.6370614359173, rel_tol=0.001)