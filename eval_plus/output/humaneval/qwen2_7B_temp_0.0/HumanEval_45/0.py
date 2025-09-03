

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
# Importing necessary library
import math

def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of the base of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area using the formula: (base * height) / 2
    area = (a * h) / 2
    return area

# Test the function with provided data points