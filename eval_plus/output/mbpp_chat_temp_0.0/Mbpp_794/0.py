"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
import re

def text_starta_endb(text):
    # Define the pattern to match 'a' followed by any characters until 'b'
    pattern = '^ab*$'
    
    # Search for the pattern in the given text
    if re.search(pattern, text):
        return True  # Return True if the pattern is found
    else:
        return False  # Return False if the pattern is not found

# Test the function with the provided test case
assert text_starta_endb("aabbbb") == True