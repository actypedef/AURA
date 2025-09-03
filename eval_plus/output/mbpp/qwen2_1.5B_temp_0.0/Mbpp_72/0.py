"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
def dif_Square(n):
    # Check if n is odd
    if n % 2 != 0:
        return False
    
    # Find the square root of n
    sqrt_n = int(n**0.5)
    
    # Check if the square of the integer part of the square root equals n
    return sqrt_n * sqrt_n == n

# Test cases
assert dif_Square(5) == True
assert dif_Square(13) == False
assert dif_Square(49) == True
assert dif_Square(8) == False