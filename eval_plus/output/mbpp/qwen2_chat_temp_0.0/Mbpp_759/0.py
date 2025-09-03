"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
def is_decimal(s):
    # Check if the string can be converted to a float
    try:
        f = float(s)
    except ValueError:
        return False
    
    # Split the string into integer and fractional parts
    s = str(f).split('.')
    
    # Check if there are exactly two parts and the second part has at most two digits
    if len(s) == 2 and len(s[1]) <= 2:
        return True
    else:
        return False

# Test the function with the provided test case
assert is_decimal('123.11') == True