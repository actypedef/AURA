

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
import math

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Start from the smallest possible prime number (2) and check for divisibility
    largest_factor = -1
    while largest_factor < n // 2:
        if n % largest_factor == 0:
            largest_factor = largest_factor
            # Divide n by the largest factor found to reduce the problem size
            n //= largest_factor
        else:
            largest_factor += 1
    
    # If n is still greater than 1, it's the largest prime factor
    return n if n > 1 else largest_factor

# Test cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2