"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    # Define the regex pattern to match strings starting with a vowel
    pattern = '^[aeiou]'
    
    # Use re.match() to check if the pattern matches the beginning of the string
    if re.match(pattern, string):
        return True
    else:
        return False

# Test the function with the provided test case
assert check_str("annie") == True
