"""
Write a python function to find the sum of the largest and smallest value in a given array.
assert big_sum([1,2,3]) == 4
"""
def big_sum(arr):
    """
    Find the sum of the largest and smallest values in a given array.

    Args:
    arr (list): A list of integers.

    Returns:
    int: The sum of the largest and smallest values in the array.
    """
    return max(arr) + min(arr)

# Test cases
assert big_sum([1,2,3]) == 4
assert big_sum([-10, -5, 0, 5, 10]) == 0
assert big_sum([100, 200, 300, 400, 500]) == 600
assert big_sum([-1, -2, -3, -4, -5]) == -15
assert big_sum([0, 0, 0, 0, 0]) == 0