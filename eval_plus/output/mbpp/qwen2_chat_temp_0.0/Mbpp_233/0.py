"""
Write a function to find the lateral surface area of a cylinder.
assert math.isclose(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)
"""
import math

def lateralsuface_cylinder(radius, height):
    # Calculate the lateral surface area of the cylinder using the formula 2 * pi * radius * height
    return (2 * math.pi * radius * height)

# Test the function with the provided test case
assert math.isclose(lateralsuface_cylinder(10, 5), 314.15000000000003, rel_tol=0.001)