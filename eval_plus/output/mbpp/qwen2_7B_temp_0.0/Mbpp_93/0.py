"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""
def power(a, b):
    # Initialize result to 1 (base case for exponentiation)
    res = 1
    
    # Loop 'b' times to multiply 'a' to the result each time
    while b > 0:
        res *= a
        b -= 1
    
    # Return the final result after the loop completes
    return res

# Test the function with the provided test case
assert power(3, 4) == 81
