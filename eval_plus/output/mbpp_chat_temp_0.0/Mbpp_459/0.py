"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
import re

def remove_uppercase(str1):
    # Use regular expression to replace all uppercase letters with an empty string
    result = re.sub('[A-Z]', '', str1)
    return result

# Test the function with the provided test case
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
