
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
def any_int(x, y, z):
    # Check if all inputs are integers
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    
    # Check if any number is equal to the sum of the other two
    if x + y == z or x + z == y or y + z == x:
        return True
    
    return False

# Test cases