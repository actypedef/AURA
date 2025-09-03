

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
# Define the function to find the largest divisor of a given number
def largest_divisor(n: int) -> int:
    # Start from the largest possible divisor (n-1) and iterate downwards
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            return i

# Test cases to verify the correctness of the function
assert largest_divisor(15) == 5
assert largest_divisor(24) == 8
assert largest_divisor(36) == 12
assert largest_divisor(7) == 1