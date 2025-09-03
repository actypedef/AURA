"""
Write a function to find the area of a rectangle.
assert rectangle_area(10,20)==200
"""
def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
    length (int): The length of the rectangle.
    width (int): The width of the rectangle.

    Returns:
    int: The area of the rectangle.
    """
    return length * width

# Test cases to verify the correctness of the function
assert rectangle_area(10, 20) == 200
assert rectangle_area(5, 7) == 35
assert rectangle_area(8, 9) == 72