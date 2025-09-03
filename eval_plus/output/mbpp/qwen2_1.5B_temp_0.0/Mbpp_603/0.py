"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    """
    Get all lucid numbers smaller than or equal to n.

    Args:
    n (int): The upper limit for generating lucid numbers.

    Returns:
    list: A list of lucid numbers less than or equal to n.
    """
    lucids = []
    i = 1
    while True:
        if is_lucid(i):
            lucids.append(i)
        if i > n:
            break
        i += 1
    return lucids

def is_lucid(num):
    """
    Check if a number is lucid.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is lucid, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test cases
assert get_ludic(10) == [1, 2, 3, 5, 7]
assert get_ludic(1) == [1]
assert get_ludic(2) == [1, 2]
assert get_ludic(3) == [1, 2, 3]
assert get_ludic(4) == [1, 2, 3, 5]
assert get_ludic(5) == [1, 2, 3, 5, 7]
assert get_ludic(6) == [1, 2, 3, 5, 7, 111]
assert get_ludic(7) == [1, 2, 3, 5, 7, 111, 137]
assert get_ludic(8) == [1, 2, 3, 5, 7, 111, 137, 197]
assert get_ludic(9) == [1, 2, 3, 5, 7, 111, 137, 197, 149]
assert get_ludic(100) == [1, 2, 3, 5, 7, 111, 137, 197, 149, 173, 181, 197, 1113, 1377, 1977, 1497, 1737, 1817, 1977, 11137, 13777, 19777, 14977, 17377, 18177, 19777, 111377, 137777, 197777, 149777, 173777, 181777, 197777, 1113777, 1377777, 1977777, 1497777, 1737777, 1817777, 1977777, 11137777, 13777777, 1977777