"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(n):
    # Check if all bits of n are set
    if (n & (n + 1)) == 0:
        return n
    
    # Initialize variables for bit manipulation
    count = 0
    temp = n
    
    # Find the position of the rightmost unset bit
    while temp != 0:
        if (temp & 1) == 0:
            break
        count += 1
        temp >>= 1
    
    # Set the leftmost unset bit
    return n | (1 << count)

# Test the function with the provided test case
assert set_left_most_unset_bit(10) == 14