"""
Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
assert text_starta_endb("aabbbb")
"""
import re

# Define the function to match strings starting with 'a' and ending with 'b'
def text_starta_endb(text):
    # Create a regular expression pattern to match strings starting with 'a' and ending with 'b'
    pattern = '^ab$'
    
    # Use the re.match() function to check if the entire string matches the pattern
    if re.match(pattern, text):
        return True  # Return True if the pattern matches
    else:
        return False  # Return False if the pattern does not match

# Test cases to verify the correctness of the function
assert text_starta_endb("aabbbb") == True
