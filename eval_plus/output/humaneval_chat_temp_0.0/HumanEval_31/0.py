

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test cases to verify the correctness of the function
assert not is_prime(6), "Test case 1 failed"
assert is_prime(101), "Test case 2 failed"
assert is_prime(11), "Test case 3 failed"
assert is_prime(13441), "Test case 4 failed"
assert is_prime(61), "Test case 5 failed"
assert not is_prime(4), "Test case 6 failed"
assert not is_prime(1), "Test case 7 failed"
