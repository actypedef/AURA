"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r, h):
    # Calculate the slant height using Pythagorean theorem
    l = math.sqrt(r * r + h * h)
    
    # Calculate the lateral surface area of the cone
    lateral_surface_area = math.pi * r * l
    
    return lateral_surface_area

# Test the function with the provided test case
assert lateralsurface_cone(5, 12) == 204.20352248333654