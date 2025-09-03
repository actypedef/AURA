"""
Write a python function to find the difference between largest and smallest value in a given list.
assert big_diff([1,2,3,4]) == 3
"""
def big_diff(nums):
    """
    Find the difference between the largest and smallest values in a given list.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The difference between the largest and smallest values in the list.
    """
    return max(nums) - min(nums)

# Test cases
assert big_diff([1,2,3,4]) == 3
assert big_diff([-10, 0, 5, 10, 20]) == 20
assert big_diff([100, 99, 88, 77, 66]) == 33
assert big_diff([]) == None
assert big_diff([1]) == 0