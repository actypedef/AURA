"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
import math 

def is_Sum_Of_Powers_Of_Two(n): 
    # Iterate over each bit position from 0 to log2(n)
    for i in range(int(math.log2(n)) + 1): 
        # Check if the ith bit is set in n
        if (n & (1 << i)) != 0: 
            # Subtract 2^i from n
            n = n - (1 << i) 
    # If n becomes 0, it can be represented as a sum of non-zero powers of 2
    return n == 0

# Test the function with the provided test case
assert is_Sum_Of_Powers_Of_Two(10) == True
