"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""
import math

def circle_circumference(radius):
    """
    Calculate the circumference of a circle given its radius.

    Args:
    radius (float): The radius of the circle.

    Returns:
    float: The circumference of the circle.
    """
    return 2 * math.pi * radius

# Test cases to verify the correctness of the function
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)