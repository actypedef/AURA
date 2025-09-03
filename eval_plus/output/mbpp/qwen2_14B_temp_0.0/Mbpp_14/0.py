"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(length, base, height):
    # Calculate the volume using the formula for a triangular prism
    Volume = (length * base * height) / 2
    return Volume

# Test the function with the provided test case
assert find_Volume(10, 8, 6) == 240
