"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(a):
    # Calculate the area using the formula for the surface area of a regular tetrahedron
    return (math.sqrt(3) * pow(a, 2))

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894
