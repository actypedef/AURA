
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
    # Check if the absolute value of 'a' is a perfect cube
    return round(abs(a) ** (1/3)) ** 3 == abs(a)

# Test cases to verify the correctness of the function