"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
def prime_num(n):
    """
    Check if the given integer is a prime number.

    Args:
    n (int): The integer to check.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check for factors from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Test cases
assert prime_num(13) == True
assert prime_num(4) == False
assert prime_num(2) == True
assert prime_num(1) == False
assert prime_num(67) == True
assert prime_num(100) == False