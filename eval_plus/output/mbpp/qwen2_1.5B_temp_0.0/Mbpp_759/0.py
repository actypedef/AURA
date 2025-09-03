"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
def is_decimal(s):
    try:
        # Attempt to convert the string to a float
        float(s)
        # Check if the float has exactly two decimal places
        return s.count('.') == 1 and len(str(float(s)).split('.')[1]) == 2
    except ValueError:
        # If conversion fails or does not have exactly two decimal places, return False
        return False

# Test cases
assert is_decimal('123.11') == True
assert is_decimal('123.1') == False
assert is_decimal('123.') == False
assert is_decimal('.123') == False
assert is_decimal('123.123456789') == False
assert is_decimal('123.123') == True
assert is_decimal('123.0') == True
assert is_decimal('123') == False
assert is_decimal('123.1') == True
assert is_decimal('123.111') == False
assert is_decimal('123.1111') == False
assert is_decimal('123.11111') == False
assert is_decimal('123.111111') == False
assert is_decimal('123.1111111') == False
assert is_decimal('123.11111111') == False
assert is_decimal('123.111111111') == False
assert is_decimal('123.1111111111') == False
assert is_decimal('123.11111111111') == False
assert is_decimal('123.111111111111') == False
assert is_decimal('123.1111111111111') == False
assert is_decimal('123.11111111111111') == False
assert is_decimal('123.111111111111111') == False
assert is_decimal('123.1111111111111111') == False
assert is_decimal('123.11111111111111111') == False
assert is_decimal('123.111111111111111111') == False
assert is_decimal('123.1111111111111111111') == False
assert is_decimal('123.11111111111111111111') == False
assert is_decimal('123.111111111111111111111') == False
assert is_decimal('123.1111111111111111111111') == False
assert is_decimal('123.11111111111111111111111') == False
assert is_decimal('123.11111111111111111111111') == False
