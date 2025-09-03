

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
# Importing necessary package for the solution
from typing import List

def is_palindrome(text: str) -> bool:
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
    # Normalize the text to lowercase and remove non-alphanumeric characters
    normalized_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the normalized text reads the same forwards and backwards
    return normalized_text == normalized_text[::-1]

# Test cases to verify the correctness of the function
test_cases = [
    ('', True),
    ('aba', True),
    ('aaaaa', True),
    ('zbcd', False)
]

for input_text, expected_output in test_cases:
    assert is_palindrome(input_text) == expected_output, f"Test failed for {input_text}. Expected {expected_output}, got {is_palindrome(input_text)}"