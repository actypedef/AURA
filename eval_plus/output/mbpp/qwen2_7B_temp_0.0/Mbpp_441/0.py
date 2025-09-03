"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
def surfacearea_cube(size):
    # Calculate the surface area of a cube using the formula 6 * (size^2)
    return 6 * (size ** 2)

# Test the function with the provided test case
assert surfacearea_cube(5) == 150
