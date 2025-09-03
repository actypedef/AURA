
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
from fractions import Fraction

def simplify(x, n):
    # Convert the input strings to Fraction objects
    frac_x = Fraction(x)
    frac_n = Fraction(n)
    
    # Multiply the two fractions
    product = frac_x * frac_n
    
    # Check if the product is an integer (whole number)
    return product.denominator == 1

# Test cases
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False