
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        return 2 * (10 ** (n - 2)) + 9 * (10 ** (n - 3))

# Test cases to verify the correctness of the function
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 18
assert starts_one_ends(3) == 180
assert starts_one_ends(4) == 1800