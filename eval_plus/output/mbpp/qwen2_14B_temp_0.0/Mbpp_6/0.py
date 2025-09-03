"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(x, y):
    # Calculate the XOR of x and y
    xor = x ^ y
    
    # Check if xor is a power of 2
    # This can be done by checking if xor & (xor - 1) is 0 and xor is not 0
    return (xor & (xor - 1)) == 0 and xor != 0

# Test the function with the provided test case
assert differ_At_One_Bit_Pos(13, 9) == True
