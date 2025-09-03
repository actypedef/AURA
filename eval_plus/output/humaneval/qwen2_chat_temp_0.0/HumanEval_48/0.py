

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return text == text[::-1]

# Test cases
assert is_palindrome('') == True
assert is_palindrome('aba') == True
assert is_palindrome('aaaaa') == True
assert is_palindrome('zbcd') == False