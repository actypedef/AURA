"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(n):
    # Initialize variables
    i = 0
    res = 0
    
    # Iterate through each bit position
    while n > 0:
        # Check if the current bit position is even
        if i % 2 == 0:
            # Set the bit at the current position in result
            res |= (1 << i)
        
        # Move to the next bit position
        i += 1
        # Right shift n to process the next bit
        n >>= 1
    
    # Combine the original number with the result to set even bits
    return n | res

# Test the function with the provided test case
assert even_bit_set_number(10) == 10