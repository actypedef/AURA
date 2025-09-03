"""
Write a function to find the circumference of a circle.
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
"""
import math

def circle_circumference(r):
    # Calculate the circumference of the circle using the formula C = 2 * pi * r
    return 2 * math.pi * r

# Test the function with the provided test case
assert math.isclose(circle_circumference(10), 62.830000000000005, rel_tol=0.001)
