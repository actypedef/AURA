
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
# Define the function to check if the given sides form a right-angled triangle
def right_angle_triangle(a, b, c):
    # Sort the sides to ensure the longest side is last
    sides = sorted([a, b, c])
    # Check if the square of the longest side equals the sum of the squares of the other two sides
    return (sides[0]**2 + sides[1]**2) == sides[2]**2

# Test cases to verify the correctness of the function
test_cases = [
    (3, 4, 5),  # Expected: True
    (1, 2, 3),  # Expected: False
    (8, 6, 10), # Expected: True
    (7, 24, 25) # Expected: True
]

# Run the test cases and print the results
for sides, expected in test_cases:
    result = right_angle_triangle(*sides)
    print(f"right_angle_triangle({sides}) == {expected}: {result}")