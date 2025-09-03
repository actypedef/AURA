"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    # Loop until n becomes less than or equal to 1
    while (n > 1):
        # If n is odd and greater than 1, it cannot be expressed as a sum of powers of 2
        if (n % 2 != 0):
            return False
        # Right shift n by 1 bit to divide it by 2
        n = n >> 1
    
    # If n is reduced to 1, it can be expressed as a sum of powers of 2
    return True

# Test the function with the provided test case
assert is_Sum_Of_Powers_Of_Two(10) == True