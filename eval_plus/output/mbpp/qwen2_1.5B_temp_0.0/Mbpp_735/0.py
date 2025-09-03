"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""
def toggle_middle_bits(n):
    # Remove the first and last bits using bitwise operations
    n = (n >> 1) ^ (n << 1)
    return n

# Test cases to verify the correctness of the solution
assert toggle_middle_bits(9) == 15
assert toggle_middle_bits(8) == 7
assert toggle_middle_bits(0) == 0
assert toggle_middle_bits(1) == 2
assert toggle_middle_bits(3) == 4
assert toggle_middle_bits(15) == 14