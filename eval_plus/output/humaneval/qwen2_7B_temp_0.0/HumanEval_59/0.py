

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
import math

def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Start with the smallest prime number
    factor = 2
    last_factor = 1
    
    while n % factor == 0:
        last_factor = factor
        n //= factor
    
    # Check for odd factors
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % factor == 0:
            last_factor = factor
            n //= factor
    
    # If n is still greater than 2, then it's a prime number
    if n > 2:
        last_factor = n
    
    return last_factor

# Test cases
assert largest_prime_factor(13195) == 29
assert largest_prime_factor(2048) == 2