"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    # Loop until n becomes zero
    while n != 0:
        # If n is odd, it cannot be represented as a power of 2
        if n % 2 == 1:
            return False
        # Right shift n by 1 bit (equivalent to dividing by 2)
        n >>= 1
    
    # If loop completes, n was a power of 2
    return True

# Test the function with the provided test case
assert is_Sum_Of_Powers_Of_Two(10) == True