"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
def surface_area(base_edge, height):
    return (base_edge ** 2 + base_edge * height) * 2

# Test cases
assert surface_area(3, 4) == 33
assert surface_area(5, 6) == 180
assert surface_area(7, 8) == 294