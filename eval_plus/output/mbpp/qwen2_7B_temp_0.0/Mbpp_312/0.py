"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(r, h):
    # Calculate the volume of the cone using the formula (1/3) * π * r^2 * h
    return (math.pi * r**2 * h) / 3

# Test the function with the provided test case
assert math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001)
