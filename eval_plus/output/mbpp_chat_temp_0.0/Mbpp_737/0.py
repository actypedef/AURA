"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(string):
    # Define a regular expression pattern for vowels at the beginning of the string
    pattern = '^[aeiou]'
    
    # Use re.search() to find a match between the pattern and the string
    if re.search(pattern, string):
        return True  # Return True if a match is found (string starts with a vowel)
    else:
        return False  # Return False if no match is found (string does not start with a vowel)

# Test the function with the provided test case
assert check_str("annie") == True