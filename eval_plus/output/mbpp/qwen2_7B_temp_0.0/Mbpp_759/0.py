"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
import re

def is_decimal(s):
    # Regular expression pattern for matching a decimal number with a precision of 2
    pattern = r"^[0-9]+\.[0-9]{2}$"
    
    # Using regex search to check if the string matches the pattern
    return bool(re.search(pattern, s))

# Test cases to validate the correctness of the function
assert is_decimal('123.11') == True
