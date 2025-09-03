
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
def minSubArraySum(nums):
    # Initialize the minimum sum to a very large positive value
    min_sum = float('inf')
    # Initialize the current sum to zero
    current_sum = 0
    
    for num in nums:
        # Update the current sum to be the minimum of the current number alone or adding the current number to the current sum
        current_sum = min(num, current_sum + num)
        # Update the minimum sum found so far
        min_sum = min(min_sum, current_sum)
    
    return min_sum

# Test cases
assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
assert minSubArraySum([-1, -2, -3]) == -6