"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(x, y):
    # XOR the two numbers to find differing bits
    xor = x ^ y
    
    # Count the number of set bits (differing bits)
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    
    # Return True if there's exactly one differing bit, False otherwise
    return count == 1

# Test the function with the provided test case
assert differ_At_One_Bit_Pos(13, 9) == True