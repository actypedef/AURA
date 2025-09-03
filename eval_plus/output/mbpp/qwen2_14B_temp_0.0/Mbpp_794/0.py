"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
import re

def text_starta_endb(text):
    # Regex pattern to match a string that starts with 'a', followed by any character, and ends with 'b'
    patterns = 'a.*?b$'
    
    # Search the pattern in the text
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

# Test the function with the provided test case
assert text_starta_endb("aabbbb") == 'Found a match!'
