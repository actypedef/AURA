
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
import math

def closest_integer(value):
    """
    This function takes a string representation of a number and returns the closest integer to it,
    rounding away from zero if necessary.
    
    Args:
    value (str): A string representing a floating-point or integer number.
    
    Returns:
    int: The closest integer to the input number, rounded away from zero if equidistant.
    
    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    """
    num = float(value)
    if num > 0:
        return math.floor(num + 0.5)
    else:
        return math.ceil(num - 0.5)

# Check function to verify the correctness of the solution
def check():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    print("All tests passed!")

check()