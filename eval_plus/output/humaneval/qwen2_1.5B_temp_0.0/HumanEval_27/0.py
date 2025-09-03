

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
# Define the function to flip case of each character in a string
def flip_case(string: str) -> str:
    # Use list comprehension to iterate over each character in the input string
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test cases to verify the correctness of the function
assert flip_case('Hello') == 'hELLO', "Test case 1 failed"
assert flip_case('Python') == 'pYTHON', "Test case 2 failed"
assert flip_case('12345') == '12345', "Test case 3 failed"
assert flip_case('abcABC') == 'ABCabc', "Test case 4 failed"