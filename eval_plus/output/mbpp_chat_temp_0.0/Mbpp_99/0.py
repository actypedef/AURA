"""
Write a function to convert the given decimal number to its binary equivalent, represented as a string with no leading zeros.
assert decimal_to_binary(8) == '1000'
"""
def decimal_to_binary(n):
    # Base case: if n is 0, return '0' directly
    if n == 0:
        return '0'
    
    result = ''
    # Loop until n becomes 0
    while n > 0:
        # Prepend the remainder of n divided by 2 to the result string
        result = str(n % 2) + result
        # Update n to be the quotient of n divided by 2
        n //= 2
    
    return result

# Test the function with the provided test case
assert decimal_to_binary(8) == '1000'