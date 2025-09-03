"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""
def lateralsurface_cube(side):
    # Calculate the lateral surface area of a cube
    LSA = 4 * side ** 2
    return LSA

# Test the function with the provided test case
assert lateralsurface_cube(5) == 100
