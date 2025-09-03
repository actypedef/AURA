"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
import re

def text_match_wordz(text):
    # Regular expression to match any word containing 'z'
    pattern = '\w*z.\w*'
    # Search for the pattern in the given text
    if re.search(pattern,  text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_match_wordz("pythonz.") == True