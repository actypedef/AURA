"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""
def left_rotate(n, d):
    # Perform left rotation on n by d bits
    return (n << d) | (n >> (32 - d))

# Test cases to validate the function
assert left_rotate(16, 2) == 64