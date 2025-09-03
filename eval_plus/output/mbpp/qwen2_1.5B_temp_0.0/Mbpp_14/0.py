"""
Write a python function to find the volume of a triangular prism.
assert find_Volume(10,8,6) == 240
"""
def find_Volume(base_length, height, length):
    """
    Calculate the volume of a triangular prism.

    Parameters:
    base_length (float): Length of the base of the triangle.
    height (float): Height of the triangle.
    length (float): Length of the prism.

    Returns:
    float: Volume of the prism.
    """
    return (base_length * height * length) / 2

# Test cases to verify the correctness of the function
assert find_Volume(10,8,6) == 240
assert find_Volume(5,3,7) == 52.5
assert find_Volume(1,1,1) == 0.5