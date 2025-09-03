"""
Write a function to find the lateral surface area of a cone given radius r and the height h.
assert lateralsurface_cone(5,12)==204.20352248333654
"""
import math

def lateralsurface_cone(r, h):
    # Calculate the slant height of the cone using Pythagorean theorem
    l = math.sqrt(h**2 + r**2)
    
    # Calculate the lateral surface area of the cone
    LSA = math.pi * r * l
    
    return LSA

# Test the function with the provided test case
assert lateralsurface_cone(5, 12) == 204.20352248333654
