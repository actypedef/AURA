"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side):
    # Calculate the volume of the cube using the formula side^3
    return side ** 3

# Test the function with the provided test case
assert volume_cube(3) == 27
