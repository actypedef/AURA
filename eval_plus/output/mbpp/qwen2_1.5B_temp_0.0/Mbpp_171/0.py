"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
def perimeter_pentagon(side_length):
    """
    Calculate the perimeter of a regular pentagon given the length of one side.

    Args:
    side_length (float): The length of one side of the pentagon.

    Returns:
    float: The perimeter of the pentagon.
    """
    return 5 * side_length

# Test cases to verify the correctness of the function
assert perimeter_pentagon(5) == 25
assert perimeter_pentagon(10) == 50
assert perimeter_pentagon(7) == 35