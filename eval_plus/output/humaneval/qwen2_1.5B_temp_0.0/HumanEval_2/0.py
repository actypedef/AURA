

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
# Define the function to truncate a floating point number
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    """
    return number - int(number)

# Test cases to verify the correctness of the function
assert truncate_number(3.5) == 0.5
assert truncate_number(7.2) == 0.2
assert truncate_number(9.99999) == 0.99999
assert truncate_number(0.00001) == 0.00001