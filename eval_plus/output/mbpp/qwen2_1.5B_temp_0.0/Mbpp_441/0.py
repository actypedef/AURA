"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
def surfacearea_cube(size):
    """
    Calculate the surface area of a cube.

    Args:
    size (int): The side length of the cube.

    Returns:
    int: The surface area of the cube.
    """
    return 6 * size ** 2

# Test cases to verify the correctness of the function
assert surfacearea_cube(5) == 150
assert surfacearea_cube(3) == 54
assert surfacearea_cube(7) == 294