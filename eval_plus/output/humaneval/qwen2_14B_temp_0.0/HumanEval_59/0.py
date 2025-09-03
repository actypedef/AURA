

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
from typing import *
from collections import *

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Initialize the largest prime factor
    largest_factor = None
    
    # Divide n by 2 until it becomes odd
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    
    # If n is still greater than 2, then it is prime
    if n > 2:
        largest_factor = n
    
    return largest_factor

# Test cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2
