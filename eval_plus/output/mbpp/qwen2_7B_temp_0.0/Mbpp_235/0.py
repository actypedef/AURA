"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(n):
    # Initialize mask to 0
    mask = 0
    
    # Iterate through each bit position
    for i in range(32):
        # Check if the current bit position is even
        if (i % 2 == 0):
            # Set the bit at the current position in the mask
            mask |= (1 << i)
    
    # Apply the mask to the input number using bitwise OR
    return n | mask

# Test the function with the provided test case
assert even_bit_set_number(10) == 10
