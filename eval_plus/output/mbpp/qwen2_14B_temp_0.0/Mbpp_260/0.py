"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
import math

def newman_prime(n):
    # Base case for the first Newman-Shanks-Williams prime
    if n == 1:
        return 2
    
    # Initialize variables for the recursive calculation
    a = 6
    b = 2
    c = 1
    
    # Loop to calculate the nth Newman-Shanks-Williams prime
    for i in range(2, n + 1):
        temp = a
        a = b + c
        b = temp
        c = c + 1
    
    # Return the nth Newman-Shanks-Williams prime
    return a - c

# Test the function with the provided test case
assert newman_prime(3) == 7