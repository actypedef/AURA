

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
import re

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    # Define a regular expression pattern for vowels (both lowercase and uppercase)
    vowel_pattern = r'[aeiouAEIOU]'
    
    # Use re.sub() to replace all occurrences of vowels with an empty string
    return re.sub(vowel_pattern, '', text)

# Test cases