"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
def surface_Area(base_edge, height):
    # Calculate the slant height using Pythagorean theorem
    slant_height = ((base_edge / 2) ** 2 + height ** 2) ** 0.5
    
    # Calculate the lateral surface area (area of four triangular faces)
    lateral_surface_area = 2 * base_edge * slant_height
    
    # Calculate the base area
    base_area = base_edge ** 2
    
    # Calculate the total surface area
    total_surface_area = lateral_surface_area + base_area
    
    return total_surface_area

# Test the function with the provided test case
assert surface_Area(3, 4) == 33