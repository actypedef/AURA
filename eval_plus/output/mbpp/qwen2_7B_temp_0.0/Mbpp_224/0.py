"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""
def count_Set_Bits(n):
    # Initialize count to zero
    count = 0
    
    # Loop until n becomes zero
    while n > 0:
        # Check if the least significant bit is 1
        if n & 1:
            count += 1
        
        # Right shift n by 1 to check the next bit
        n >>= 1
    
    return count

# Test the function with the provided test case
assert count_Set_Bits(2) == 1
