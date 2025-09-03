"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(a, b, c):
    """
    Find the median of three numbers.

    Args:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.

    Returns:
    int or float: The median of the three numbers.
    """
    # Sort the numbers
    sorted_numbers = sorted([a, b, c])
    
    # Return the middle element
    return sorted_numbers[1]

# Test cases
assert median_numbers(25, 55, 65) == 55.0
assert median_numbers(30, 40, 50) == 40.0
assert median_numbers(-10, -20, -30) == -20.0
assert median_numbers(7, 8, 9) == 8.0