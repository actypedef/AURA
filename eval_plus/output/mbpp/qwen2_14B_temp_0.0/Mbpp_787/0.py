"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
import re

def text_match_three(text):
    # Regex pattern to match 'a' followed by three 'b's
    patterns = 'ab{3}'
    
    # Search the pattern in the text
    if re.search(patterns, text):
        return True
    else:
        return False

# Test the function with the provided test case
assert not text_match_three("ac")
