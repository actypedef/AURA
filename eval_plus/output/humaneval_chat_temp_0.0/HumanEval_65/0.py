
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string to easily manipulate its digits
    str_x = str(x)
    length = len(str_x)
    
    # If shift is greater than the number of digits, reverse the string
    if shift >= length:
        return str_x[::-1]
    
    # Perform the circular shift
    shift = shift % length  # In case shift is larger than twice the number of digits
    shifted_str = str_x[-shift:] + str_x[:-shift]
    
    return shifted_str

# Test cases