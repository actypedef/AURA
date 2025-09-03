"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
import re

def remove_lowercase(str1):
    # Use regular expression to find all uppercase letters and join them
    result = ''.join(re.findall('[A-Z]', str1))
    return result

# Test the function with the provided test case
assert remove_lowercase("PYTHon") == 'PYTH'
