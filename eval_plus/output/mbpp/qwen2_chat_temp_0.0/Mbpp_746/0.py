"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
def sector_area(radius, angle):
    # Check if the angle is greater than 360 degrees
    if angle > 360:
        return None
    
    # Calculate the area of the sector using the formula (angle/360) * π * radius^2
    area = (angle / 360) * 3.1415 * radius ** 2
    
    return area

# Test the function with the provided test case
assert sector_area(4, 45) == 6.283185307179586
