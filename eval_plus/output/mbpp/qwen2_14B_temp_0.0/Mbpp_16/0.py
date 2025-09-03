"""
Write a function to that returns true if the input string contains sequences of lowercase letters joined with an underscore and false otherwise.
assert text_lowercase_underscore("aab_cbbbc")==(True)
"""
import re

def text_lowercase_underscore(text):
    # Regex pattern to match sequences of lowercase letters joined with an underscore
    text = re.compile(r".*[a-z]+_[a-z]+.*")
    
    # Check if the input string matches the pattern
    if text.match(string):
        return True
    else:
        return False

# Test the function with the provided test case
assert text_lowercase_underscore("aab_cbbbc") == True
