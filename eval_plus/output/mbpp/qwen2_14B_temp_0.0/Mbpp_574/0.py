"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
import math

def surfacearea_cylinder(r, h):
    # Calculate the surface area using the formula 2*pi*r*(r + h)
    return 2 * math.pi * r * (r + h)

# Test the function with the provided test case
assert surfacearea_cylinder(10, 5) == 942.45
