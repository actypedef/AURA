"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
def count_Set_Bits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive call to count the set bits
        return 1 + count_Set_Bits(n & (n - 1))

# Test the function with the provided test case
assert count_Set_Bits(2) == 1