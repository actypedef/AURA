"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
import math

def sector_area(radius, angle):
    # Check if the angle is within the valid range (0-360 degrees)
    if angle > 360:
        return None
    
    # Calculate the area of the sector using the formula: (angle/360) * pi * r^2
    area = (angle / 360) * math.pi * radius ** 2
    
    return area

# Test cases to verify the correctness of the function
assert sector_area(4,45) == 6.283185307179586
assert sector_area(5,180) == 78.53981633974483
assert sector_area(3,90) == 28.274333882308138
assert sector_area(2,120) == 37.699111843077515
assert sector_area(1,360) == 3.141592653589793
assert sector_area(1,361) == None