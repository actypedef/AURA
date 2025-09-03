
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
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = bin(decimal)[2:]
    return f"db{binary}db"

# Test cases
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(32) == "db100000db"
assert decimal_to_binary(0) == "db0db"
assert decimal_to_binary(1) == "db1db"
assert decimal_to_binary(2) == "db10db"
assert decimal_to_binary(3) == "db11db"
assert decimal_to_binary(4) == "db100db"
assert decimal_to_binary(5) == "db101db"
assert decimal_to_binary(6) == "db110db"
assert decimal_to_binary(7) == "db111db"
assert decimal_to_binary(8) == "db1000db"
assert decimal_to_binary(9) == "db1001db"
assert decimal_to_binary(10) == "db1010db"
assert decimal_to_binary(11) == "db1011db"
assert decimal_to_binary(12) == "db1100db"
assert decimal_to_binary(13) == "db1101db"
assert decimal_to_binary(14) == "db1110db"
assert decimal_to_binary(15) == "db1111db"
assert decimal_to_binary(16) == "db10000db"
assert decimal_to_binary(17) == "db10001db"
assert decimal_to_binary(18) == "db10010db"
assert decimal_to_binary(19) == "db10011db"
assert decimal_to_binary(20) == "db10100db"
assert decimal_to_binary(21) == "db10101db"
assert decimal_to_binary(22) == "db10110db"
assert decimal_to_binary(23) == "db10111db"
assert decimal_to_binary(24) == "db11000db"
assert decimal_to_binary(25) == "db11001db"
assert decimal_to_binary(26) == "db11010db"
assert decimal_to_binary(27) == "db11011db"
assert decimal_to_binary(28) == "db11100db"
assert decimal_to_binary(29) == "db11101db"
assert decimal_to_binary(30) == "db11110db"
assert decimal_to_binary(31) == "db11111db"
assert decimal_to_binary(32) == "db100000db"
assert decimal_to_binary(33) == "db100