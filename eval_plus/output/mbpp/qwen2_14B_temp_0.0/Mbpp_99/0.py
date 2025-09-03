"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(num):
    # Base case: if num is 0, return '0'
    if num == 0:
        return '0'
    
    binary_str = ''
    
    # Convert decimal to binary
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num = num // 2
    
    return binary_str

# Test the function with the provided test case
assert decimal_to_binary(8) == '1000'
