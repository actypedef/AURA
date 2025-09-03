"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(n):
    # Check if n is less than 2, which is not considered a prime number
    if n < 2:
        return True
    
    # Iterate from 2 to the square root of n to check for factors
    for i in range(2, int(n**0.5) + 1):
        # If n has any factor other than 1 and itself, it's not prime
        if n % i == 0:
            return True
    
    # If no factors were found, n is prime
    return False

# Test the function with the provided test case
assert is_not_prime(2) == False
