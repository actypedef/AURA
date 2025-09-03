
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
from math import sqrt

def is_multiply_prime(a):
    def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # Check if the number can be expressed as the product of three primes
    for i in range(2, a):
        if not is_prime(i):
            continue
        for j in range(i, a):  # Start from i to avoid duplicate pairs
            if not is_prime(j):
                continue
            k = a // (i * j)
            if k >= j and is_prime(k):  # Ensure k is at least j to avoid duplicates and check primality
                return True
    return False

# Test cases