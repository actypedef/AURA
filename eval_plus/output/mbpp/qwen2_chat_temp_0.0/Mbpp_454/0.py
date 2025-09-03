"""
Write a function that matches a word containing 'z'.
assert text_match_wordz("pythonz.")==True
"""
import re

def text_match_wordz(text):
    # Define the pattern to match words containing 'z'
    pattern = '\w*z.\w*'
    
    # Use regular expression search to find matches
    if re.search(pattern,  text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_match_wordz("pythonz.") == True