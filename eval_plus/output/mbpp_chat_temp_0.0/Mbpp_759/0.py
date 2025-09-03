"""
Write a function to check whether a given string is a decimal number with a precision of 2.
assert is_decimal('123.11')==True
"""
def is_decimal(num):
    # Check if the input string can be converted to a float
    try:
        num = float(num)
    except ValueError:
        return False
    
    # Convert the float back to an integer and compare it to the original number
    if int(num) == num:
        return False
    
    # Split the number into integer and fractional parts
    num_parts = str(num).split('.')
    
    # Check if there are exactly two parts and the second part has at most two digits
    if len(num_parts) != 2 or len(num_parts[1]) > 2:
        return False
    
    return True

# Test the function with the provided test case
assert is_decimal('123.11') == True