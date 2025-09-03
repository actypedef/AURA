"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(num):
    # Check if the number is less than 2
    if num < 2:
        return True
    # Iterate from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):
        # If num is divisible by any number in this range, it's not prime
        if num % i == 0:
            return True
    # If no divisors were found, num is prime
    return False

# Test the function with the provided test case
assert is_not_prime(2) == False
