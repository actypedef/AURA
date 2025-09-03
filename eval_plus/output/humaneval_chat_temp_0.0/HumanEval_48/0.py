

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
    
    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Normalize the string by removing spaces and converting to lowercase
    normalized_text = text.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return normalized_text == normalized_text[::-1]

# Test cases
assert is_palindrome('')
assert is_palindrome('aba')
assert is_palindrome('aaaaa')
assert not is_palindrome('zbcd')