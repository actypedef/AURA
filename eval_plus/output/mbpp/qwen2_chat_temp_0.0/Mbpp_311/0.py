"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(n):
    # Check if all bits of n are set
    if (n & (n + 1)) == 0:
        return n
    
    i = 0
    while n != 0:
        # Set the leftmost unset bit
        n |= (1 << i)
        i += 1
    
    return n

# Test the function with the provided test case
assert set_left_most_unset_bit(10) == 14
