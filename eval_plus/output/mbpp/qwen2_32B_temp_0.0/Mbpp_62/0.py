"""
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
"""
def smallest_num(nums):
    """
    This function finds the smallest number in a list.
    """
    if not nums:
        return None
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest

# Test cases
assert smallest_num([10, 20, 1, 45, 99]) == 1
assert smallest_num([10, 20, 1, 45, 99, 0]) == 0
assert smallest_num([10, 20, 1, 45, 99, -1]) == -1
assert smallest_num([]) is None
assert smallest_num([1]) == 1