"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""
def lateralsurface_cube(side_length):
    """
    Calculate the lateral surface area of a cube.

    Args:
    side_length (int): The length of one side of the cube.

    Returns:
    int: The lateral surface area of the cube.
    """
    return 4 * side_length ** 2

# Test cases to verify the correctness of the function
assert lateralsurface_cube(5) == 100
assert lateralsurface_cube(3) == 36
assert lateralsurface_cube(7) == 196