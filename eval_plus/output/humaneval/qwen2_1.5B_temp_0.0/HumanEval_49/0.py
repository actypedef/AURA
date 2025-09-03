

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base ** 2) % p
        n //= 2
    return result

# Test cases to verify the correctness of the function
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1