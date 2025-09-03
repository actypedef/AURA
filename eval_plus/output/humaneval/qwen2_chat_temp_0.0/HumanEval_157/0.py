
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
def right_angle_triangle(a, b, c):
    """
    Check if the given sides can form a right-angled triangle.

    :param a: Length of side a
    :param b: Length of side b
    :param c: Length of side c
    :return: True if it forms a right-angled triangle, False otherwise
    """
    # Sort the sides to ensure the longest side is last (c)
    sides = sorted([a, b, c])
    
    # Apply Pythagoras theorem to check for right-angled triangle
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Test cases to verify the correctness of the function
assert right_angle_triangle(3, 4, 5) == True, "Test case 1 failed"
assert right_angle_triangle(1, 2, 3) == False, "Test case 2 failed"