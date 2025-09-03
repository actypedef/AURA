

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
# Define the function to calculate the area of a triangle
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area using the formula (1/2) * base * height
    area = (1/2) * a * h
    return area

# Test the function with provided data points
assert triangle_area(5, 3) == 7.5