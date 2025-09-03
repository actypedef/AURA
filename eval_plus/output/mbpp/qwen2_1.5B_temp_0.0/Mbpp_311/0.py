"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""
def set_left_most_unset_bit(n):
    # Find the position of the rightmost unset bit
    pos = n & -n
    
    # Set the leftmost unset bit
    return n | pos

# Test cases
assert set_left_most_unset_bit(10) == 14
assert set_left_most_unset_bit(25) == 31
assert set_left_most_unset_bit(8) == 9
assert set_left_most_unset_bit(7) == 7