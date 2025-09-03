"""
Write a function to find the third side of a right angled triangle.
assert otherside_rightangle(7,8)==10.63014581273465
"""
import math

def otherside_rightangle(a, b):
    # Calculate the third side using the Pythagorean theorem
    c = math.sqrt(a**2 + b**2)
    return round(c, 6)

# Test the function with the provided test case
assert otherside_rightangle(7, 8) == 10.63014581273465
