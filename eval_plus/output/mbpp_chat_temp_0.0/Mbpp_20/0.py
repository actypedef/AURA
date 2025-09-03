"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    # Check if n is less than 2, which cannot be a Woodall number
    if n < 2:
        return False
    
    # Initialize k to 0
    k = 0
    
    # Loop until n becomes odd
    while (n & 1) == 0:
        n >>= 1  # Right shift n by 1 bit
        k += 1  # Increment k
    
    # Check if n is now equal to 1 and k is even
    return n == 1 and k % 2 == 0

# Test the function with the provided test case
assert is_woodall(383) == True