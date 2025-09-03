"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(n):
    # Convert the decimal number to binary using bin() function
    # Remove the '0b' prefix from the binary representation
    return bin(n)[2:]

# Test the function with the provided test case
assert decimal_to_binary(8) == '1000'
