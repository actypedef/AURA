"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""
import math

def volume_sphere(radius):
    # Calculate the volume using the formula (4/3) * π * r^3
    return (4.0 / 3) * math.pi * radius ** 3

# Test the function with the provided test case
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
