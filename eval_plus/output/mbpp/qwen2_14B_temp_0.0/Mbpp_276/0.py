"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    # Calculate the volume using the formula πr^2h
    return math.pi * radius**2 * height

# Test the function with the provided test case
assert math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001)
