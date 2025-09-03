"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
import math

def set_left_most_unset_bit(n):
    # If the number is 0, return 1 as the leftmost unset bit is 1
    if n == 0:
        return 1
    
    # Initialize the position of the leftmost unset bit
    pos = 0
    
    # Iterate to find the position of the leftmost unset bit
    while (1 << pos) & n:
        pos += 1
    
    # Set the leftmost unset bit and return the result
    return n | (1 << pos)

# Test the function with the provided test case
assert set_left_most_unset_bit(10) == 14
