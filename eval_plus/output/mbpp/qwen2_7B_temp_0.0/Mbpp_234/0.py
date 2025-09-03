"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side_length):
    # Calculate the volume of the cube using the formula V = s^3
    return side_length ** 3

# Test the function with the provided test case
assert volume_cube(3) == 27
