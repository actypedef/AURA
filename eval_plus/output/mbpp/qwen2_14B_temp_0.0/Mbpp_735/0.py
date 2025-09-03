"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""
def toggle_middle_bits(n):
    # Find the position of the highest set bit
    p = 0
    while (1 << p) < n:
        p += 1
    
    # If there are less than 2 bits, return the number itself
    if p < 2:
        return n
    
    # Set all bits except the first and last bit to 1
    num = (1 << p) - 1
    
    # Toggle the middle bits by XORing with the original number
    return num ^ n

# Test the function with the provided test case
assert toggle_middle_bits(9) == 15
