"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(a):
    # Calculate the area of one face of the tetrahedron using the formula for an equilateral triangle
    area_face = (math.sqrt(3) / 4) * a**2
    
    # Since a tetrahedron has four faces, multiply the area of one face by 4 to get the total surface area
    return 4 * area_face

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894