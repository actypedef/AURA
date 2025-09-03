
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
    # Convert the string value to a float
    num = float(value)
    
    # Check if the number is halfway between two integers
    if abs(num % 1 - 0.5) < 1e-9:
        # Round away from zero
        return int(math.ceil(num) if num > 0 else math.floor(num))
    else:
        # Use built-in round function for other cases
        return round(num)

# Test cases