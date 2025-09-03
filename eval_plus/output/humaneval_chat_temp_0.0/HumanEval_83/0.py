
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
        return 1  # Only '1' itself
    else:
        # For n > 1, calculate the count
        # Numbers starting with 1: 1xxxx... (n-1 digits)
        # Numbers ending with 1 but not starting with 1: xxxx...1 (n-1 digits) - 1 (to avoid double counting '1xxxx...1')
        return 2 * (10 ** (n - 1)) - 1

# Test cases to verify the correctness of the function
assert starts_one_ends(1) == 1
assert starts_one_ends(2) == 19
assert starts_one_ends(3) == 180
assert starts_one_ends(4) == 1800