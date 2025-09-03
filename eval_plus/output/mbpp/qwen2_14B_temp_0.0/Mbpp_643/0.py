"""
Write a function that checks if a strings contains 'z', except at the start and end of the word.
assert text_match_wordz_middle("pythonzabc.")==True
"""
import re

def text_match_wordz_middle(text):
    # Regex pattern to match 'z' except at the start or end of the word
    patterns = 'z.*?z'
    
    # Search for the pattern in the text
    if re.search(patterns, text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_match_wordz_middle("pythonzabc.") == True
