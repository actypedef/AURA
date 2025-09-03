"""
Write a python function to count the number of equal numbers from three given integers.
assert test_three_equal(1,1,1) == 3
"""
def test_three_equal(a, b, c):
    """
    Write a python function to count the number of equal numbers from three given integers.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.
    
    Returns:
    int: The count of equal numbers among the three integers.
    """
    return sum([a == b, a == c, b == c])

# Test cases
assert test_three_equal(1,1,1) == 3
assert test_three_equal(2,2,3) == 2
assert test_three_equal(4,5,6) == 0
assert test_three_equal(-1,-1,-1) == 3
assert test_three_equal(0,0,0) == 3