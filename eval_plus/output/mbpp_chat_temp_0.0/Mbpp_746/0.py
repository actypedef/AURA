"""
Write a function to find area of a sector. The function takes the radius and angle as inputs. Function should return None if the angle is larger than 360 degrees.
assert sector_area(4,45)==6.283185307179586
"""
def sector_area(r, theta):
    # Check if the angle is greater than 360 degrees
    if theta > 360:
        return None
    
    # Calculate the area of the sector using the formula (theta/360) * pi * r^2
    area = (theta / 360) * 3.141592653589793 * r ** 2
    
    # Return the calculated area
    return area

# Test the function with the provided test case
assert sector_area(4, 45) == 6.283185307179586
