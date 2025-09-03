
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
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Test cases
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
assert right_angle_triangle(5, 12, 13) == True
assert right_angle_triangle(10, 6, 8) == True
assert right_angle_triangle(7, 24, 25) == True
assert right_angle_triangle(2, 2, 2) == False
assert right_angle_triangle(1, 1, 1.41421356237) == True
assert right_angle_triangle(1, 1, 1.41421356238) == False
assert right_angle_triangle(1, 1, 1.41421356236) == False
assert right_angle_triangle(1, 1, 1.41421356235) == False
assert right_angle_triangle(1, 1, 1.41421356234) == False
assert right_angle_triangle(1, 1, 1.41421356233) == False
assert right_angle_triangle(1, 1, 1.41421356232) == False
assert right_angle_triangle(1, 1, 1.41421356231) == False
assert right_angle_triangle(1, 1, 1.41421356230) == False
assert right_angle_triangle(1, 1, 1.41421356229) == False
assert right_angle_triangle(1, 1, 1.41421356228) == False
assert right_angle_triangle(1, 1, 1.41421356227) == False
assert right_angle_triangle(1, 1, 1.41421356226) == False
assert right_angle_triangle(1, 1, 1.41421356225) == False
assert right_angle_triangle(1, 1, 1.41421356224) == False
assert right_angle_triangle(1, 1, 1.41421356223) == False
assert right_angle_triangle(1, 1, 1.41421356222) == False
assert right_angle_triangle(1, 1, 1.41421356221) == False
assert right_angle_triangle(1, 1, 