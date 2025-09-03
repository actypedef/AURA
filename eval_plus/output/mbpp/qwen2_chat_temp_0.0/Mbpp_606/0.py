"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""
# Importing the math module for mathematical functions
import math

def radian_degree(degree):
    # Converting degree to radian using the formula: radian = degree * (pi / 180)
    return degree * (math.pi / 180)

# Test the function with the provided test case
assert radian_degree(90) == 1.5707963267948966