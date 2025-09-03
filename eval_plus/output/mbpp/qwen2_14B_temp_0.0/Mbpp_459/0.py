"""
Write a function to remove uppercase substrings from a given string.
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
"""
import re

def remove_uppercase(s):
    # Use regex to replace uppercase letters with an empty string
    return re.sub('[A-Z]', '', s)

# Test the function with the provided test case
assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'
