"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
import re

def remove_uppercase(str1):
    # Using regular expression to find and replace all uppercase letters with an empty string
    result = re.sub('[A-Z]', '', str1)
    return result

# Test cases to validate the function
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
