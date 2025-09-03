"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
import math

def triangle_area(radius):
    if radius < 0:
        return None
    # The formula for the area of a triangle inscribed in a semicircle is (1/2) * r^2 * sin(90)
    area = (1/2) * radius**2 * math.sin(math.pi / 2)
    return area

# Test cases
assert triangle_area(-1) == None