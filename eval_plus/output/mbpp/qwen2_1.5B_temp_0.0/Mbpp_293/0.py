"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
import math

def otherside_rightangle(a, b):
    """
    Calculate the length of the third side of a right-angled triangle given the lengths of the other two sides.

    Args:
    a (float): Length of one side of the right-angled triangle.
    b (float): Length of another side of the right-angled triangle.

    Returns:
    float: Length of the third side of the right-angled triangle.
    """
    # Using the Pythagorean theorem to calculate the hypotenuse
    c = math.sqrt(a**2 + b**2)
    return c

# Test cases to verify the correctness of the function
assert otherside_rightangle(7, 8) == 10.63014581273465