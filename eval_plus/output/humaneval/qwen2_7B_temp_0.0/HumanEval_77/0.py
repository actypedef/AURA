
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
    Determine if the given integer 'a' is a perfect cube.

    Args:
    a (int): The integer to check.

    Returns:
    bool: True if 'a' is a perfect cube, False otherwise.
    
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    # Calculate the cube root of 'a'
    cube_root = abs(a) ** (1/3)
    
    # Check if the cube root is an integer
    return cube_root.is_integer()

# Example usage: