"""
Write a python function to find the sum of an array.
assert _sum([1, 2, 3]) == 6
"""
def _sum(arr):
    """
    Write a python function to find the sum of an array.
    
    assert _sum([1, 2, 3]) == 6
    """
    return sum(arr)

# Test cases
assert _sum([1, 2, 3]) == 6
assert _sum([-1, -2, -3]) == -6
assert _sum([]) == 0
assert _sum([5]) == 5
assert _sum([10, 20, 30, 40, 50]) == 150