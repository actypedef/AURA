
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
# Define the function to perform circular shift
def circular_shift(x, shift):
    # Convert the integer to a string
    str_x = str(x)
    
    # Calculate the effective shift considering the length of the string
    effective_shift = shift % len(str_x)
    
    # Perform the circular shift
    if effective_shift == 0:
        return str_x[::-1]  # Return the reversed string if no shift is needed
    else:
        return str_x[-effective_shift:] + str_x[:-effective_shift]

# Test cases to verify the correctness of the function
assert circular_shift(12, 1) == "21"
assert circular_shift(12, 2) == "12"
