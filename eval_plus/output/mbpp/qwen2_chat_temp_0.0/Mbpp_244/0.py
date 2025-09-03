"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
def next_Perfect_Square(n):
    # Calculate the square root of n and round it up to the nearest integer
    sqrt_n = int(n**0.5) + 1
    
    # Return the square of the calculated square root
    return sqrt_n * sqrt_n

# Test the function with the provided test case
assert next_Perfect_Square(35) == 36
