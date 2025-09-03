"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(x, y):
    # XOR the two numbers to find differing bits
    xor_result = x ^ y
    
    # Check if there is exactly one bit set in the result
    return (xor_result & (xor_result - 1)) == 0

# Test the function with the provided test case
assert differ_At_One_Bit_Pos(13, 9) == True