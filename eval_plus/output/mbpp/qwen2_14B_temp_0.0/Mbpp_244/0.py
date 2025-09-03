"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
import math

def next_Perfect_Square(N):
    # Find the square root of the given number
    root = math.sqrt(N)
    
    # Round up to the nearest whole number to get the next integer
    if root == int(root):
        return (int(root) + 1) * (int(root) + 1)
    else:
        return (int(root) + 1) * (int(root) + 1)

# Test the function with the provided test case
assert next_Perfect_Square(35) == 36
