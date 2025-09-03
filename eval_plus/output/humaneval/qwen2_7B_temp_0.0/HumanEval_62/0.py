

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
def derivative(xs: list):
    # Calculate the derivative by multiplying each coefficient by its respective power of x
    # and then reducing the power by one for each term.
    return [i * coeff for i, coeff in enumerate(xs) if i > 0]

# Test cases to verify the correctness of the function
assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20], "Test case 1 failed"
assert derivative([1, 2, 3]) == [2, 6], "Test case 2 failed"
