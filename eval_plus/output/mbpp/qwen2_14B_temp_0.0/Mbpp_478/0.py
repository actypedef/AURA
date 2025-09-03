"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
import re

def remove_lowercase(s):
    # Use regex to replace lowercase letters with nothing
    result = re.sub('[a-z]', '', s)
    return result

# Test the function with the provided test case
assert remove_lowercase("PYTHon") == 'PYTH'
