"""
Write a function to find the volume of a cone.
assert math.isclose(volume_cone(5,12), 314.15926535897927, rel_tol=0.001)
"""
import math

def volume_cone(radius, height):
    # Calculate the volume of a cone using the formula (1/3) * π * radius^2 * height
    return (math.pi * radius ** 2 * height) / 3

# Test the function with the provided test case
assert math.isclose(volume_cone(5, 12), 314.15926535897927, rel_tol=0.001)