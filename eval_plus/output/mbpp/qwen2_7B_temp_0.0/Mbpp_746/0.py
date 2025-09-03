"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
def sector_area(r, a):
    # Check if the angle is greater than 360 degrees
    if a > 360:
        return None
    
    # Calculate the area of the sector using the formula (π * r^2 * a) / 360
    area = (3.141592653589793 * r * r * a) / 360
    
    return area

# Test cases
assert sector_area(4, 45) == 6.283185307179586