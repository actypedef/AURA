
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
    # Convert the integer to a string to easily manipulate its digits
    digits = str(x)
    
    # Calculate the effective shift needed
    num_digits = len(digits)
    effective_shift = shift % num_digits
    
    # If the shift is greater than the number of digits, reverse the digits
    if effective_shift == 0:
        return digits[::-1]
    
    # Perform the circular shift
    shifted_digits = digits[-effective_shift:] + digits[:-effective_shift]
    
    return shifted_digits

# Test cases