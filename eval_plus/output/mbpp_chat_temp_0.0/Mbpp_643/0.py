"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
import re

def text_match_wordz_middle(text):
    # Define the regex pattern to match 'z' not at the start or end of the word
    pattern = '\Bz\B'
    
    # Search for the pattern in the given text
    if re.search(pattern,  text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_match_wordz_middle("pythonzabc.") == True