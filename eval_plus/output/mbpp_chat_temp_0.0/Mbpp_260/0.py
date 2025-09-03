"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    # Initialize variables for the Newman-Shanks-Williams sequence
    a = 0
    b = 1
    
    # Loop until we find the nth Newman-Shanks-Williams prime
    while n > 0:
        # Calculate the next term in the sequence
        c = (a + b * b) % (2 * b - 1)
        
        # Check if the current term is prime
        if c != 0:
            a, b = b, c
            n -= 1
    
    return b

# Test the function with the provided test case
assert newman_prime(3) == 7