
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
    """
    Convert a decimal number to its binary representation as a string,
    surrounded by 'db' at the start and end.
    
    :param decimal: An integer in decimal format
    :return: A string representing the binary format, surrounded by 'db'
    
    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    if decimal == 0:
        return "db0db"
    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2
    return f"db{binary_str}db"

# Check function to verify the correctness of the solution
def check_solution():
    assert decimal_to_binary(15) == "db1111db", "Test case 1 failed"
    assert decimal_to_binary(32) == "db100000db", "Test case 2 failed"
    assert decimal_to_binary(0) == "db0db", "Test case 3 failed"
    assert decimal_to_binary(1) == "db1db", "Test case 4 failed"
    print("All test cases passed!")

check_solution()