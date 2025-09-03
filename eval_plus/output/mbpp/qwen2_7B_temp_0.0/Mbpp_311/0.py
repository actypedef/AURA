"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(n):
    # Check if all bits of n are set (i.e., n is a power of two)
    if n & (n - 1) == 0:
        return n + 1
    
    # Find the position of the leftmost unset bit
    pos = 0
    while n != 0:
        n >>= 1
        pos += 1
    
    # Set the leftmost unset bit
    return (1 << pos) | n

# Test the function with the provided test case
assert set_left_most_unset_bit(10) == 14