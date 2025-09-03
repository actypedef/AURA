
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
import math

def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    result = 1
    for i in range(1, n+1):
        result *= math.factorial(i)
    return result

# Test cases to verify the correctness of the function
assert special_factorial(4) == 288, "Test case 1 failed"
assert special_factorial(5) == 362880, "Test case 2 failed"
assert special_factorial(0) == 1, "Test case 3 failed"