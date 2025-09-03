"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
def triangle_area(radius):
    # Check if the radius is negative
    if radius < 0:
        return None
    
    # Calculate the area using the formula for the largest triangle inscribed in a semicircle
    area = (3 * (radius ** 2)) / 4
    
    return area

# Test the function with the provided test case
assert triangle_area(-1) == None