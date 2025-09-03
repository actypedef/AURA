"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
def next_Perfect_Square(n):
    # Calculate the square root of the given number
    x = int(n**0.5)
    
    # Increment the square root value to get the next integer
    x += 1
    
    # Return the square of the incremented value
    return x * x

# Test the function with the provided test case
assert next_Perfect_Square(35) == 36
