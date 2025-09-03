
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
    # Check if n is 1, which is only a simple power of itself (1^k = 1 for any k)
    if n == 1:
        return x == 1
    
    # Calculate the logarithm of x to the base n
    log_result = math.log(x, n)
    
    # Check if the logarithm result is an integer
    return log_result.is_integer()

# Test cases