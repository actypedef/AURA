
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
def x_or_y(n, x, y):
    # Check if n is a prime number
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Return x if n is prime, else y
    return x if is_prime(n) else y

# Test cases to verify the correctness of the solution
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5