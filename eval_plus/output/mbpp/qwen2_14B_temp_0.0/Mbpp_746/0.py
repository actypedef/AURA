"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
import math

def sector_area(r, a):
    # Return None if the angle is larger than 360 degrees
    if a > 360:
        return None
    # Calculate the area of the sector
    return (math.pi * r**2) * (a / 360)

# Test the function with the provided test case
assert sector_area(4, 45) == 6.283185307179586
