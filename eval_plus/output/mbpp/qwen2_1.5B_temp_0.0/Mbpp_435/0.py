"""
Write a python function to find the last digit of a given number.
assert last_Digit(123) == 3
"""
def last_Digit(n):
    """
    Write a python function to find the last digit of a given number.
    
    Parameters:
    n (int): The input number
    
    Returns:
    int: The last digit of the input number
    """
    return abs(n) % 10

# Test cases
assert last_Digit(123) == 3
assert last_Digit(-456) == 6
assert last_Digit(7890) == 0
assert last_Digit(-1000) == 0