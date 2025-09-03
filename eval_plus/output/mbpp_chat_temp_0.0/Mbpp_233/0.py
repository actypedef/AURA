"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
import math

def lateralsuface_cylinder(r, h):
    # Calculate the lateral surface area of a cylinder using the formula: 2 * pi * r * h
    return 2 * math.pi * r * h

# Test the function with the provided test case
assert math.isclose(lateralsuface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001)
