"""
Write a function to find the surface area of a cube of a given size.
assert surfacearea_cube(5)==150
"""
def surfacearea_cube(side):
    # Calculate the surface area using the formula 6 * side^2
    return 6 * (side ** 2)

# Test the function with the provided test case
assert surfacearea_cube(5) == 150
