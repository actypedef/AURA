

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t."""
    return all(x < t for x in l)

# Test cases to verify the correctness of the function
assert below_threshold([1, 2, 4, 10], 100) == True
assert below_threshold([1, 20, 4, 10], 5) == False
