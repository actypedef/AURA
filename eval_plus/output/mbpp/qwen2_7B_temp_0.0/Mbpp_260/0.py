"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    # Initialize variables for the Newman-Shanks-Williams sequence
    a = 1
    b = 2
    
    # Loop until we reach the nth Newman-Shanks-Williams prime
    while n > 0:
        # Calculate the next term in the sequence
        c = (a + b + 1)
        
        # Check if the current term is a prime number
        if all(c % i != 0 for i in range(2, int(c**0.5) + 1)):
            n -= 1
        
        # Update the values of a and b for the next iteration
        a, b = b, c
    
    return b

# Test the function with the provided test case
assert newman_prime(3) == 7
