"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(x, y):
    # XOR the two numbers
    xor_result = x ^ y
    
    # Check if there is exactly one set bit (i.e., 1)
    return xor_result & -xor_result == 1

# Test cases
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(25, 4) == False
assert differ_At_One_Bit_Pos(7, 8) == True
assert differ_At_One_Bit_Pos(0, 1) == True
assert differ_At_One_Bit_Pos(1, 0) == True