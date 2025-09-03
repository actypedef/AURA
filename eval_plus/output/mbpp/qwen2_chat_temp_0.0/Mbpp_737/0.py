"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    # Define the regular expression pattern for vowels at the beginning of the string
    pattern = '^[aeiouAEIOU]'
    
    # Use re.match to check if the pattern matches the start of the string
    if re.match(pattern, string):
        return True
    else:
        return False

# Test the function with the provided test case
assert check_str("annie") == True