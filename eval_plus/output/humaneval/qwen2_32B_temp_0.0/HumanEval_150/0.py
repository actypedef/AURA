
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n < 2:
        return y
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return y
    return x

# Test cases
assert x_or_y(7, 34, 12) == 34
assert x_or_y(15, 8, 5) == 5
assert x_or_y(2, 10, 20) == 10
assert x_or_y(1, 10, 20) == 20
assert x_or_y(0, 10, 20) == 20
assert x_or_y(4, 10, 20) == 20
assert x_or_y(5, 10, 20) == 10
assert x_or_y(6, 10, 20) == 20
assert x_or_y(8, 10, 20) == 20
assert x_or_y(9, 10, 20) == 20
assert x_or_y(10, 10, 20) == 20
assert x_or_y(11, 10, 20) == 10
assert x_or_y(12, 10, 20) == 20
assert x_or_y(13, 10, 20) == 10
assert x_or_y(14, 10, 20) == 20
assert x_or_y(16, 10, 20) == 20
assert x_or_y(17, 10, 20) == 10
assert x_or_y(18, 10, 20) == 20
assert x_or_y(19, 10, 20) == 10
assert x_or_y(20, 10, 20) == 20
assert x_or_y(21, 10, 20) == 20
assert x_or_y(22, 10, 20) == 20
assert x_or_y(23, 10, 20) == 10
assert x_or_y(24, 10, 20) == 20
assert x_or_y(25, 10, 20) == 20
assert x_or_y(26, 10, 20) == 20
assert x_or_y(27, 10, 20) == 20
assert x_or_y(28, 10, 20) == 20
assert x_or_y(29, 10, 20) == 10
assert x_or_y(30, 10, 20) == 20
assert x_or_y(31, 10, 20