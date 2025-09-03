"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(n):
    # Check if the number is less than 2
    if n < 2:
        return True
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test the function with the provided test case
assert is_not_prime(2) == False
