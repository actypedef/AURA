"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(side):
    # Calculate the area using the formula for a regular tetrahedron
    area = (math.sqrt(3) * pow(side, 2)) / 4
    return area

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894
