"""
Write a function to remove lowercase substrings from a given string.
assert remove_lowercase("PYTHon")==('PYTH')
"""
import re

def remove_lowercase(s):
    # Use regular expression to replace all lowercase letters with an empty string
    return (re.sub('[a-z]', '', s))

# Test the function with the provided test case
assert remove_lowercase("PYTHon") == 'PYTH'
