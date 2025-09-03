"""
Write a function to check whether the given string is starting with a vowel or not using regex.
assert check_str("annie")
"""
import re

def check_str(s):
    # Define a regular expression pattern for vowels
    pattern = r'^[aeiouAEIOU]'
    
    # Use the re.match() function to check if the string starts with a vowel
    if re.match(pattern, s):
        return True
    else:
        return False

# Test cases to verify the correctness of the function
assert check_str("annie") == True
assert check_str("banana") == False
assert check_str("apple") == True
assert check_str("orange") == False
assert check_str("Egg") == True
assert check_str("dog") == False