
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
# Importing necessary packages
import math

def is_multiply_prime(a):
    """
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    # Check if the input number is less than 100
    if a >= 100:
        return "Input must be less than 100."
    
    # Find all factors of the input number
    factors = [i for i in range(2, a+1) if a % i == 0]
    
    # Count the number of prime factors
    prime_factors_count = sum(is_prime(i) for i in factors)
    
    # Return True if there are exactly three prime factors, False otherwise
    return prime_factors_count == 3

# Test cases