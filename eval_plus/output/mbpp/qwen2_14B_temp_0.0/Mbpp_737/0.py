"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    # Regex pattern to match a vowel at the start of the string
    text = re.compile(r"^a|e|i|o|u", re.IGNORECASE)
    
    # Check if the string matches the pattern
    if text.match(string):
        return True
    else:
        return False

# Test the function with the provided test case
assert check_str("annie") == True
