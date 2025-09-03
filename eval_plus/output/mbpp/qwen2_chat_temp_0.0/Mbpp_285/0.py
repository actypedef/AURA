"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
import re

def text_match_two_three(text):
    # Define the regex pattern to match 'a' followed by 2 to 3 'b's
    pattern = 'ab{2,3}'
    
    # Search for the pattern in the given text
    if re.search(pattern, text):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_match_two_three("ac") == (False)
