
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
import math

def triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides.
    
    Args:
    a (float): Length of the first side of the triangle.
    b (float): Length of the second side of the triangle.
    c (float): Length of the third side of the triangle.
    
    Returns:
    float: The area of the triangle rounded to 2 decimal places if the sides form a valid triangle,
           otherwise returns -1.
           
    A valid triangle has all sides greater than 0 and the sum of any two sides must be greater than the third side.
    """
    # Check for a valid triangle
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return -1
    
    # Calculate semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Round the area to 2 decimal places
    return round(area, 2)

# Test cases