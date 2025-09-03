"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
def next_Perfect_Square(n):
    # Calculate the square root of the given number
    sqrt_n = n ** 0.5
    
    # Increment the square root to get the next integer
    next_int = int(sqrt_n) + 1
    
    # Return the square of the next integer, which is the next perfect square
    return next_int ** 2

# Test the function with the provided test case
assert next_Perfect_Square(35) == 36
