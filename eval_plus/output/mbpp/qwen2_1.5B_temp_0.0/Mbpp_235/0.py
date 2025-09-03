"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""
def even_bit_set_number(n):
    # Initialize result variable
    result = 0
    
    # Iterate through each bit position from right to left
    for i in range(32):  # Assuming n is an integer
        # Check if the current bit is even (i.e., i % 2 == 0)
        if i % 2 == 0:
            # Set the corresponding bit in the result
            result |= (1 << i)
    
    return result

# Test cases to verify the correctness of the function
assert even_bit_set_number(10) == 10
assert even_bit_set_number(15) == 14
assert even_bit_set_number(8) == 8
assert even_bit_set_number(7) == 6