
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
import math

def is_simple_power(x, n):
    # Check if x is 1 and n is not 1, return True as 1 is a simple power of any number except 1
    if x == 1 and n != 1:
        return True
    # Check if n is 1 and x is not 1, return False as no number other than 1 can be a power of 1
    elif n == 1 and x != 1:
        return False
    else:
        # Calculate the logarithm of x to the base n and check if it's an integer
        log_result = math.log(x, n)
        return log_result.is_integer()

# Test cases to verify the correctness of the function