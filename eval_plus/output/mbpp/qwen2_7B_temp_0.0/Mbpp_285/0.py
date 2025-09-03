"""
Write a function that checks whether a string contains the 'a' character followed by two or three 'b' characters.
assert text_match_two_three("ac")==(False)
"""
import re

def text_match_two_three(text):
    # Define the pattern to match 'a' followed by two or three 'b's
    pattern = 'ab{2,3}'
    
    # Use regular expression search to find matches
    if re.search(pattern, text):
        return True
    else:
        return False

# Test cases to validate the function
assert text_match_two_three("ac") == False
assert text_match_two_three("abc") == True
assert text_match_two_three("abbc") == True
assert text_match_two_three("abbb") == True
assert text_match_two_three("abbbb") == False