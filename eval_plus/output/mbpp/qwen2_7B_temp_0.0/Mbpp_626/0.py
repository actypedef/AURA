"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
def triangle_area(r):
    # Check if the radius is negative or zero
    if r <= 0:
        return None
    
    # Calculate the area of the largest triangle inscribed in a semicircle
    area = (3 * r ** 2) / 4
    
    return area

# Test cases
assert triangle_area(-1) == None