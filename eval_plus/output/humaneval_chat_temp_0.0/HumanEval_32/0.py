import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Ensure the list has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    # Find the largest non-zero coefficient to ensure a solution exists
    max_coeff = max(abs(coeff) for coeff in xs if coeff != 0)
    if max_coeff == 0:
        raise ValueError("All coefficients are zero, which does not guarantee a solution.")
    
    # Use Newton's method to find a root
    def newton_method(f, df, x0, tol=1e-7, max_iter=1000):
        x = x0
        for _ in range(max_iter):
            fx = f(xs, x)
            dfx = df(xs, x)
            if abs(dfx) < tol:
                break
            x -= fx / dfx
        return x
    
    # Derivative of the polynomial
    def dpoly(xs: list, x: float):
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])
    
    # Initial guess based on the coefficients
    x0 = -sum(xs[:-1]) / xs[-1]
    
    # Find the root using Newton's method
    root = newton_method(poly, dpoly, x0)
    
    return root

# Test cases