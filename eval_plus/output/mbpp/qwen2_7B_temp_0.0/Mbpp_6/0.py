"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(x, y):
    # XOR the two numbers to find differing bits
    xor = x ^ y
    
    # Check if the result of XOR has exactly one bit set (i.e., it's a power of 2)
    return xor != 0 and (xor & (xor - 1)) == 0

# Test the function with the provided test case
assert differ_At_One_Bit_Pos(13, 9) == True
