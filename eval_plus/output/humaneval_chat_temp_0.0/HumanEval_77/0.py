
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
import math

def iscube(a):
    """
    Check if the given integer 'a' is a perfect cube.

    Args:
    a (int): The integer to check.

    Returns:
    bool: True if 'a' is a perfect cube, False otherwise.
    """
    # Handle negative numbers by converting them to positive
    abs_a = abs(a)
    
    # Calculate the cube root of the absolute value of 'a'
    cube_root = round(abs_a ** (1/3))
    
    # Check if the cube of the calculated cube root equals the original number
    return cube_root ** 3 == abs_a

# Test cases to verify the correctness of the function