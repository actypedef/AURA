"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
def remove_lowercase(s):
    """
    Remove all lowercase letters from the input string.

    Args:
    s (str): The input string from which lowercase letters will be removed.

    Returns:
    str: A new string with all lowercase letters removed.
    """
    return ''.join(char for char in s if not char.islower())

# Test cases to verify the correctness of the solution
assert remove_lowercase("PYTHon") == 'PYTH'
assert remove_lowercase("Hello World!") == 'Hll Wrld!'
assert remove_lowercase("123abcABC") == '123ABC'
assert remove_lowercase("") == ''
assert remove_lowercase("aAaaaXa") == 'X'