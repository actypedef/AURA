
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
        return 1  # Only one digit number that starts and ends with 1
    else:
        # For n > 1, calculate the count
        # Numbers starting with 1: 1xxxx...x (n-1 digits)
        # Numbers ending with 1 but not starting with 1: xxxx...x1 (n-2 digits)
        return 9 * (10 ** (n - 2)) + 10 ** (n - 1)

# Test cases to verify the correctness of the function
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 18
assert starts_one_ends(3) == 180
assert starts_one_ends(4) == 1800
