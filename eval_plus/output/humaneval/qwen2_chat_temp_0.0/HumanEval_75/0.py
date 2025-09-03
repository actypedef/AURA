
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
from typing import *
from collections import *

def is_multiply_prime(a: int) -> bool:
    def is_prime(n):
        """Check if a number is a prime number."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in range(2, 100) if is_prime(i)]
    
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 * p2 * p3 == a:
                    return True
    return False

# Test cases to verify the correctness of the function
assert is_multiply_prime(30) == True  # 30 = 2 * 3 * 5
assert is_multiply_prime(60) == True  # 60 = 2 * 2 * 3 * 5 (but only three distinct primes)
assert is_multiply_prime(7) == False   # 7 is a prime itself, not a product of three primes
assert is_multiply_prime(84) == True  # 84 = 2 * 2 * 3 * 7 (but only three distinct primes)
assert is_multiply_prime(100) == False # 100 = 2 * 2 * 5 * 5 (but only two distinct primes)