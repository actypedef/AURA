"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
def multiply_int(x, y):
    # Initialize result to 0
    result = 0
    
    # Determine the number of iterations based on the sign of y
    positive = y > 0
    
    # Work with absolute value of y to simplify the loop
    y = abs(y)
    
    # Add x to the result y times
    for _ in range(y):
        result += x
    
    # Adjust the sign of the result if necessary
    if not positive:
        result = -result
    
    return result

# Test the function with the provided test case
assert multiply_int(10, 20) == 200
