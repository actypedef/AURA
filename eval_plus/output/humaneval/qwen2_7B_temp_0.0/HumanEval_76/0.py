
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
    # Check if n is 1 and x is not 1, which should return False
    if n == 1 and x != 1:
        return False
    
    # Calculate the logarithm of x to the base n
    log_result = math.log(x, n)
    
    # Check if the result is an integer (simple power condition)
    return log_result.is_integer()

# Test cases