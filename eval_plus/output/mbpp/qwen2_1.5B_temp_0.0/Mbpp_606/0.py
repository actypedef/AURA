"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""
import math

def radian_degree(degrees):
    """
    Convert degrees to radians.

    Args:
    degrees (float): The angle in degrees.

    Returns:
    float: The angle in radians.
    """
    return degrees * math.pi / 180

# Test cases to verify the correctness of the function
assert radian_degree(90) == 1.5707963267948966
assert radian_degree(45) == math.pi / 4
assert radian_degree(0) == 0
assert radian_degree(-90) == -1.5707963267948966