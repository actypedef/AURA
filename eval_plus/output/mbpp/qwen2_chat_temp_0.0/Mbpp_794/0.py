"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
import re

def text_starta_endb(text):
    # Define the pattern to match 'a' followed by any characters and ending with 'b'
    pattern = 'ab$'
    
    # Use regex search to find if the pattern exists in the text
    if re.search(pattern, text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_starta_endb("aabbbb") == True