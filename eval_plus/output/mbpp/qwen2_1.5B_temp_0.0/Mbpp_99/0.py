"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(decimal):
    """
    Convert a given decimal number to its binary equivalent, represented as a string with no leading zeros.
    
    Args:
    decimal (int): The decimal number to be converted.
    
    Returns:
    str: The binary representation of the decimal number as a string without leading zeros.
    """
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2
    return binary

# Test cases to verify the correctness of the function
assert decimal_to_binary(8) == '1000'
assert decimal_to_binary(7) == '111'
assert decimal_to_binary(0) == '0'
assert decimal_to_binary(15) == '1111'