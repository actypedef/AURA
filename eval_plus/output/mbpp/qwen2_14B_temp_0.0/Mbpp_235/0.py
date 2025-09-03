"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(n):
    # Initialize result to store the final number with even bits set
    result = 0
    # Initialize temp to keep track of the bit position
    temp = 0
    
    # Loop through the bits of the number
    while n > 0:
        # Check if the current bit position is even (0-based index)
        if temp % 2 == 0:
            # Set the corresponding bit in result
            result |= (1 << temp)
        
        # Increment the bit position
        temp += 1
        # Right shift n to process the next bit
        n >>= 1
    
    return result

# Test the function with the provided test case
assert even_bit_set_number(10) == 10
