"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
def count_Set_Bits(n):
    """
    Count the number of set bits (binary digits with value 1) in a given number.

    Args:
    n (int): The number to count set bits for.

    Returns:
    int: The count of set bits in the number.
    """
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

# Test cases
assert count_Set_Bits(2) == 1
assert count_Set_Bits(5) == 2
assert count_Set_Bits(7) == 3
assert count_Set_Bits(10) == 2
assert count_Set_Bits(15) == 4