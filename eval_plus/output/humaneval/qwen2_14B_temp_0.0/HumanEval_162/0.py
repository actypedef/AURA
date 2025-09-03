
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

# Test cases
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
assert string_to_md5('') is None
assert string_to_md5('OpenAI') == 'd0a29130f8b0d7c7c475e4638a889c4b'
