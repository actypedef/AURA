"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
def median_trapezium(a, b, c):
    """
    Calculate the median length of a trapezium given its three sides.

    Args:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    float: The median length of the trapezium.
    """
    # Sort the sides to easily calculate the median
    sides = sorted([a, b, c])
    # The median is the average of the two middle sides
    return (sides[1] + sides[2]) / 2

# Test cases to verify the correctness of the solution
assert median_trapezium(15, 25, 35) == 20
assert median_trapezium(7, 9, 11) == 8.5
assert median_trapezium(4, 6, 8) == 6