"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    """
    Calculate the sum of the digits of a given non-negative integer.

    Args:
    n (int): A non-negative integer whose digits will be summed.

    Returns:
    int: The sum of the digits of the input number.
    """
    return sum(int(digit) for digit in str(n))

# Test cases to verify the correctness of the solution
assert sum_digits(345) == 12
assert sum_digits(0) == 0
assert sum_digits(999) == 27
assert sum_digits(123456789) == 45