
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
from math import sqrt

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    
    # Check if the length is less than 2 (not prime)
    if length < 2:
        return False
    
    # Check divisibility from 2 to the square root of the length
    for i in range(2, int(sqrt(length)) + 1):
        if length % i == 0:
            return False
    
    return True

# Test cases