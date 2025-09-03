"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""
def toggle_middle_bits(n):
    # Initialize mask to 0
    mask = 0
    
    # Calculate the number of bits in n
    num_bits = n.bit_length()
    
    # Create a mask with all bits set except the first and last bits
    for i in range(1, num_bits - 1):
        mask |= (1 << i)
    
    # Toggle the middle bits using XOR operation
    return n ^ mask

# Test the function with the provided test case
assert toggle_middle_bits(9) == 15
