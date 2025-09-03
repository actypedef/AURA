"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
import re

def is_decimal(num):
    # Regular expression pattern to match a decimal number with precision of 2
    decimal_pattern = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    
    # Check if the number matches the pattern
    result = decimal_pattern.search(num)
    
    return bool(result)

# Test the function with the provided test case
assert is_decimal('123.11') == True
