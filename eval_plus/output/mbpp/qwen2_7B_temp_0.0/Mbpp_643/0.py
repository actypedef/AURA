"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
import re

def text_match_wordz_middle(text):
    # Regular expression to check for 'z' not at the start or end of the word
    pattern = r'\Bz\B'
    # Search for the pattern in the given text
    if re.search(pattern, text):
        return True
    else:
        return False

# Test cases to validate the function
assert text_match_wordz_middle("pythonzabc.") == True
assert text_match_wordz_middle("programming") == False
assert text_match_wordz_middle("xyzzy") == True