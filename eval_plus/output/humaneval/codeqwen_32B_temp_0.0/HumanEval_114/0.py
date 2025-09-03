
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum

# Test cases
assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
assert minSubArraySum([-1, -2, -3]) == -6
assert minSubArraySum([1, 2, 3, 4, 5]) == 1
assert minSubArraySum([-1, -2, -3, -4, -5]) == -15
assert minSubArraySum([1, -2, 3, -4, 5, -6]) == -6
assert minSubArraySum([1, 2, 3, -6, 4, 5, -3, 2]) == -6
assert minSubArraySum([1, 2, 3, -4, 5, 6]) == -4
assert minSubArraySum([-1, -2, -3, -4, -5, -6]) == -21
assert minSubArraySum([1, 2, 3, 4, 5, -6]) == -6
assert minSubArraySum([1, -2, 3, 4, -5, 6]) == -5
assert minSubArraySum([1, 2, 3, 4, 5, 6]) == 1
assert minSubArraySum([-1, -2, -3, -4, -5, -6]) == -21
assert minSubArraySum([1, 2, 3, 4, 5, 6, -7]) == -7
assert minSubArraySum([1, -2, 3, 4, 5, 6, -7]) == -7
assert minSubArraySum([1, 2, 3, 4, 5, 6, -7, 8]) == -7
assert minSubArraySum([1, -2, 3, 4, 5, 6, -7, 8, -9]) == -9
assert minSubArraySum([1, 2, 3, 4, 5, 6, -7, 8, -9, 10]) == -9
assert minSubArraySum([1, -2, 3, 4, 5, 6, -7, 8, -9, 10, -11]) == -11
assert minSubArraySum([1, 2, 3, 4, 5, 6, -7, 8, -9, 10, -11, 12]) == -11
assert minSubArraySum([1, -2, 3, 4, 5, 6, -7, 8, -9, 10, -11, 12, -13]) == -13