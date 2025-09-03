"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
import math

def area_tetrahedron(side_length):
    """
    Calculate the area of a tetrahedron given its side length.

    Args:
    side_length (float): The length of each side of the tetrahedron.

    Returns:
    float: The area of the tetrahedron.
    """
    # Calculate the volume of the tetrahedron using Heron's formula
    s = (side_length ** 3) / (6 * math.sqrt(2))
    volume = (math.sqrt(2) / 12) * s**3
    
    # Calculate the area of one face of the tetrahedron
    face_area = math.sqrt(3) * (side_length ** 2)
    
    # Calculate the total surface area of the tetrahedron
    total_surface_area = 4 * face_area
    
    return total_surface_area

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894