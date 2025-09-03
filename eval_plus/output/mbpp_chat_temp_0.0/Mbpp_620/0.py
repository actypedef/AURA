"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(arr):
    # Sort the array to facilitate finding divisible pairs
    arr.sort()
    
    # Initialize an array to store the maximum subset size ending at each index
    dp = [1] * len(arr)
    
    # Iterate through the array to fill the dp array
    for i in range(1, len(arr)):
        for j in range(i):
            # Check if the current element is divisible by the previous element
            if arr[i] % arr[j] == 0:
                # Update the dp value for the current index
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum value from the dp array, which represents the size of the largest subset
    return max(dp)

# Test the function with the provided test case
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4