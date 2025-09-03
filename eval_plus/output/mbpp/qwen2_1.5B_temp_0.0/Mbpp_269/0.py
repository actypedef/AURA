"""
Write a function to find the ascii value of a character.
assert ascii_value('A')==65
"""
def ascii_value(char):
    """
    Returns the ASCII value of a given character.

    Args:
    char (str): The character whose ASCII value is to be found.

    Returns:
    int: The ASCII value of the character.
    """
    return ord(char)

# Test cases to verify the correctness of the function
assert ascii_value('A') == 65
assert ascii_value('a') == 97
assert ascii_value('1') == 49
assert ascii_value('!') == 33
assert ascii_value(' ') == 32
assert ascii_value('$') == 36
assert ascii_value('%') == 37
assert ascii_value('&') == 38
assert ascii_value('*') == 42
assert ascii_value('(') == 40
assert ascii_value(')') == 41
assert ascii_value('+') == 43
assert ascii_value(',') == 44
assert ascii_value('-') == 45
assert ascii_value('.') == 46
assert ascii_value('/') == 47
assert ascii_value(':') == 58
assert ascii_value(';') == 59
assert ascii_value('<') == 60
assert ascii_value('=') == 61
assert ascii_value('>') = 62
assert ascii_value('?') == 63
assert ascii_value('@') == 64
assert ascii_value('[') == 91
assert ascii_value('\\') == 92
assert ascii_value(']') == 93
assert ascii_value('^') == 94
assert ascii_value('_') == 95
assert ascii_value('{') == 123
assert ascii_value('|') == 124
assert ascii_value('}') == 125
assert ascii_value('~') == 126