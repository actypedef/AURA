"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
# Importing necessary package for assertions
import unittest

def is_not_prime(n):
    """
    Check if a number is not prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is not prime, False otherwise.
    """
    # Check if the number is less than 2
    if n < 2:
        return True
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test cases to verify the correctness of the function
class TestIsNotPrime(unittest.TestCase):
    def test_is_not_prime(self):
        self.assertFalse(is_not_prime(2))
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(8))
