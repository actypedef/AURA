"""
Write a function that takes in the radius and height of a cylinder and returns the the volume.
assert math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001)
"""
import math

def volume_cylinder(radius, height):
    # Calculate the area of the circular base using the formula πr^2
    base_area = math.pi * (radius ** 2)
    
    # Calculate the volume of the cylinder using the formula V = base_area * height
    return base_area * height

# Test the function with the provided test case
assert math.isclose(volume_cylinder(10, 5), 1570.7500000000002, rel_tol=0.001)
