"""
Write a python function to find the area of the largest triangle that can be inscribed in a semicircle with a given radius.
assert triangle_area(-1) == None
"""
def triangle_area(r):
    # Check if the radius is non-positive
    if r <= 0:
        return None
    
    # Calculate the area of the largest inscribed triangle
    area = (3 * (3 ** 0.5) / 4) * (r ** 2)
    
    return area

# Test the function with the provided test case
assert triangle_area(-1) == None