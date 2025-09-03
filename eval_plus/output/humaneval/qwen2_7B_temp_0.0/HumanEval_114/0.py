
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
    # Initialize variables to store the minimum sum found so far and the current sum
    min_sum = float('inf')
    current_sum = 0
    
    # Iterate through each number in the array
    for num in nums:
        # Update the current sum to be the minimum of the current number alone or adding the current number to the previous current sum
        current_sum = min(num, current_sum + num)
        # Update the minimum sum found so far if the current sum is less than it
        min_sum = min(min_sum, current_sum)
    
    return min_sum

# Test cases