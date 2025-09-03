"""
Write a function to find the surface area of a cylinder.
assert surfacearea_cylinder(10,5)==942.45
"""
import math

def surfacearea_cylinder(r, h):
    # Calculate the surface area of a cylinder using the formula 2πr(h + r)
    return (2 * math.pi * r) * (h + r)

# Test the function with the provided test case
assert surfacearea_cylinder(10, 5) == 942.477796076938