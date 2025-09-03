"""
Write a function to caluclate the area of a tetrahedron.
assert area_tetrahedron(3)==15.588457268119894
"""
def area_tetrahedron(a):
    # Calculate the area of a regular tetrahedron using the formula
    return (a * a * 0.447213595)

# Test the function with the provided test case
assert area_tetrahedron(3) == 15.588457268119894
