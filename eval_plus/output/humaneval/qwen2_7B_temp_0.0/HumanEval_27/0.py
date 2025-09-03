

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
def flip_case(s: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in s)

# Test cases