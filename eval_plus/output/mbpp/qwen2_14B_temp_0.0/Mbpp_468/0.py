"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(nums):
    # Initialize the dp list with the same values as nums
    dp = nums[:]
    
    # Iterate through the array to fill the dp table
    for i in range(len(nums)):
        for j in range(i):
            # Check if nums[j] is less than nums[i] to form an increasing subsequence
            if nums[j] < nums[i]:
                # Update dp[i] to be the maximum of its current value or the product of dp[j] and nums[i]
                dp[i] = max(dp[i], dp[j] * nums[i])
    
    # Return the maximum value in the dp list
    return max(dp)

# Test the function with the provided test case
assert max_product([3, 100, 4, 5, 150, 6]) == 3000