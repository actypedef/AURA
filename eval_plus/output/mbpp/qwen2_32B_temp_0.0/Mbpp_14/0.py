"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base_length, base_width, height):
    """
    This function calculates the volume of a triangular prism.
    """
    return (base_length * base_width * height) / 2

# Test cases
assert find_Volume(10, 8, 6) == 240
assert find_Volume(5, 4, 3) == 30
assert find_Volume(7, 6, 5) == 105