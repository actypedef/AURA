"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r, h):
    """
    Calculate the lateral surface area of a cone.

    Parameters:
    r (float): The radius of the base of the cone.
    h (float): The height of the cone.

    Returns:
    float: The lateral surface area of the cone.
    """
    return math.pi * r * h

# Test cases to verify the correctness of the function
assert lateralsurface_cone(5, 12) == 204.20352248333654
assert lateralsurface_cone(7, 9) == 138.54407177940904
assert lateralsurface_cone(10, 15) == 785.3981633974483