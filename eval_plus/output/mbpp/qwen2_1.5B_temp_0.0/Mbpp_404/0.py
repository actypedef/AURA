"""
Write a python function to find the minimum of two numbers.
assert minimum(1,2) == 1
"""
def minimum(a, b):
    """
    Write a python function to find the minimum of two numbers.
    
    assert minimum(1,2) == 1
    """
    return min(a, b)

# Test cases
assert minimum(1,2) == 1
assert minimum(-5, -3) == -5
assert minimum(0, 0) == 0
assert minimum(100, 200) == 100
assert minimum(-100, -200) == -200