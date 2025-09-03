"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
import math

def is_woodall(n):
    # Check if n is less than 2
    if n < 2:
        return False
    
    # Calculate the value of k using logarithms
    k = (math.log(n * 2 + 1, 2))
    
    # Check if k is an integer and if 2^k - 1 equals n
    return k.is_integer() and (2 ** int(k) - 1 == n)

# Test the function with the provided test case
assert is_woodall(383) == True
