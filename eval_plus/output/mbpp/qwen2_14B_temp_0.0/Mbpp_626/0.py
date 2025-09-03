"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
import math

def triangle_area(r):
    # Check if the radius is negative
    if r < 0:
        return None
    
    # Calculate the area of the largest inscribed triangle
    area = (3 * math.sqrt(3) * pow(r, 2)) / 4
    return area

# Test the function with the provided test case
assert triangle_area(-1) == None
