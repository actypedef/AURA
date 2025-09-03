"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    # Loop until n becomes 0
    while (n != 0):
        # If n is odd and not equal to 1, it cannot be expressed as a sum of powers of 2
        if ((n & 1) == 1 and n != 1):
            return False
        # Right shift n by 1 bit to check the next bit
        n = n >> 1
    
    # If all bits except one are zero, n can be expressed as a sum of powers of 2
    return True

# Test the function with the provided test case
assert is_Sum_Of_Powers_Of_Two(10) == True