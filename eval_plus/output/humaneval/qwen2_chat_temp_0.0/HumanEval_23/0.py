

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
# Define the function to calculate the length of a given string
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Initialize counter for the length of the string
    length = 0
    
    # Iterate over each character in the string
    for char in string:
        # Increment the counter for each character
        length += 1
    
    # Return the total count of characters as the length of the string
    return length

# Example usage of the function