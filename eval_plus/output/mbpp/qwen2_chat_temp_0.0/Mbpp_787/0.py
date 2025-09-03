"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
import re

def text_match_three(text):
    # Define the pattern to match 'a' followed by exactly three 'b's
    pattern = 'ab{3}'
    
    # Search for the pattern in the given text
    if re.search(pattern, text):
        return True
    else:
        return False

# Test the function with the provided test case
assert not text_match_three("ac")
