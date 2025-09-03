
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
# Define the function to check if a number is a simple power of another
def is_simple_power(x, n):
    # Check if x is less than or equal to 0 or n is less than 2
    if x <= 0 or n < 2:
        return False
    
    # Calculate the power of n to the base x
    power = n ** int(x)
    
    # Return True if the calculated power equals x, otherwise False
    return power == x

# Test cases to verify the correctness of the function
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(8, 2) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(3, 1) == False
assert is_simple_power(5, 3) == False