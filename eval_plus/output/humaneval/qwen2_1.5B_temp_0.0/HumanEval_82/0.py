
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to determine if the length of a string is a prime number
def prime_length(string):
    return is_prime(len(string))

# Test cases
assert prime_length('Hello') == True
assert prime_length('abcdcba') == True
assert prime_length('kittens') == True
assert prime_length('orange') == False