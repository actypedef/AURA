
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation as a string,
    surrounded by 'db' at the beginning and end."""
    if decimal == 0:
        return "db0db"
    
    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal = decimal // 2
    
    return f"db{binary_str}db"

# Test cases to verify the correctness of the function
assert decimal_to_binary(15) == "db1111db", "Test case 1 failed"
assert decimal_to_binary(32) == "db100000db", "Test case 2 failed"