"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
import math

def surface_Area(base_edge, height):
    # Calculate the slant height using Pythagorean theorem
    slant_height = math.sqrt((base_edge / 2)**2 + height**2)
    
    # Calculate the area of one triangular face
    triangle_area = (base_edge * slant_height) / 2
    
    # Calculate the total surface area (4 triangular faces + 1 square base)
    total_surface_area = 4 * triangle_area + base_edge ** 2
    
    return total_surface_area

# Test the function with the provided test case
assert surface_Area(3, 4) == 33
