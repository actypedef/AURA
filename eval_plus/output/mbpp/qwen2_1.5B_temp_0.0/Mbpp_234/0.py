"""
Write a function to find the volume of a cube given its side length.
assert volume_cube(3)==27
"""
def volume_cube(side_length):
    """
    Calculate the volume of a cube.

    Args:
    side_length (int): The length of one side of the cube.

    Returns:
    int: The volume of the cube.
    """
    return side_length ** 3

# Test cases to verify the correctness of the function
assert volume_cube(3) == 27
assert volume_cube(4) == 64
assert volume_cube(5) == 125