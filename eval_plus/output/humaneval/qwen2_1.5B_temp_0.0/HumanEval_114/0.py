
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
def minSubArraySum(nums):
    if not nums: return 0

    # Initialize variables to keep track of the current sum and the minimum sum found so far
    current_sum = nums[0]
    min_sum = nums[0]

    # Iterate through each number in the list starting from the second element
    for num in nums[1:]:
        # Update the current sum to be the minimum of the current number or the sum of the current number and the previous current sum
        current_sum = min(num, current_sum + num)
        
        # Update the minimum sum to be the minimum of the current sum or the previous minimum sum
        min_sum = min(min_sum, current_sum)

    return min_sum

# Test cases to verify the correctness of the solution
assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
assert minSubArraySum([-1, -2, -3]) == -6