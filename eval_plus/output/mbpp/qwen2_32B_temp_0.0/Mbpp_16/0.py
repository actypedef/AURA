"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
import re

def text_lowercase_underscore(s):
    """
    Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
    """
    pattern = r'^[a-z]+_[a-z]+$'
    return bool(re.match(pattern, s))

# Test cases
assert text_lowercase_underscore("aab_cbbbc") == True
assert text_lowercase_underscore("aab_Abbbc") == False
assert text_lowercase_underscore("Aaab_abbbc") == False