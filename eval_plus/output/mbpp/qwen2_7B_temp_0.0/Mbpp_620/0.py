"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(nums):
    # Sort the input array to facilitate finding pairs
    nums.sort()
    
    # Initialize an array to store the maximum subset size ending at each index
    dp = [1] * len(nums)
    
    # Iterate through the sorted array to fill the dp array
    for i in range(1, len(nums)):
        for j in range(i):
            # Check if the current number is divisible by the previous number
            if nums[i] % nums[j] == 0:
                # Update the dp value for the current index
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the size of the largest subset found
    return max(dp)

# Test the function with the provided test case
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4