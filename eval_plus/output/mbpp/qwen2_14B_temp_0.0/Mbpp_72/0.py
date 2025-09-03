"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
import math 

def dif_Square(n): 
    # Check if n is odd
    if (n % 2 != 0): 
        return True
    else: 
        # Check if n is a perfect square
        x = math.sqrt(n / 2) 
        if (x * x == int(x) * int(x)): 
            return True
        else: 
            return False

# Test the function with the provided test case
assert dif_Square(5) == True
