
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    for digit in str(n):
        d = int(digit)
        if d % 2 == 1:
            product *= d
            has_odd = True
    return product if has_odd else 0

# Test cases to verify the correctness of the function
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(2222222) == 0
assert digits(13579) == 945