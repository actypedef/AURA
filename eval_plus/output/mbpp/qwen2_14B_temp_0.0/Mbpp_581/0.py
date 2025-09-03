"""
Write a python function to find the surface area of a square pyramid with a given base edge and height.
assert surface_Area(3,4) == 33
"""
def surface_Area(b, s):
    # Calculate the slant height using the Pythagorean theorem
    l = (b**2 + s**2)**0.5
    # Calculate the surface area using the formula: base area + 4 * triangle area
    SA = b**2 + 2 * b * l
    return SA

# Test the function with the provided test case
assert surface_Area(3, 4) == 33
