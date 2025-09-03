"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_At_One_Bit_Pos(num1, num2):
    """
    Check whether the two numbers differ at one bit position only or not.
    """
    # XOR the two numbers
    xor_result = num1 ^ num2

    # Count the number of set bits in the XOR result
    count = 0
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1

    # If the count is 1, the numbers differ at one bit position only
    return count == 1


# Test cases
assert differ_At_One_Bit_Pos(13, 9) == True
assert differ_At_One_Bit_Pos(10, 12) == True
assert differ_At_One_Bit_Pos(15, 11) == False
assert differ_At_One_Bit_Pos(2, 3) == True
assert differ_At_One_Bit_Pos(5, 7) == False