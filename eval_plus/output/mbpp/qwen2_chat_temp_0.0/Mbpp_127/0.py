"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
def multiply_int(x, y):
    # Initialize the result variable to zero
    res = 0
    
    # If x is negative, make it positive and negate the result at the end
    if x < 0:
        x = -x
        y = -y
    
    # Loop through each bit of y
    while y > 0:
        # If the least significant bit of y is set (i.e., odd), add x to the result
        if y & 1:
            res += x
        
        # Double x for the next bit
        x <<= 1
        # Shift right y to check the next bit
        y >>= 1
    
    return res

# Test the function with the provided test case
assert multiply_int(10, 20) == 200