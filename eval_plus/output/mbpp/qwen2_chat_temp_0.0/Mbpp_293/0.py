"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
import math

def otherside_rightangle(a, b):
    # Calculate the square of the hypotenuse using Pythagorean theorem
    c_square = (a ** 2) + (b ** 2)
    # Take the square root to get the length of the hypotenuse
    c = math.sqrt(c_square)
    return c

# Test the function with the provided test case
assert otherside_rightangle(7, 8) == 10.63014581273465