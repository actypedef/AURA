"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(a):
    # Initialize the dp array where dp[i] will store the size of the largest subset ending with a[i]
    dp = [0 for i in range(len(a))]
    
    # The last element is always a subset of size 1
    dp[-1] = 1
    
    # Iterate from the second last element to the first element
    for i in range(len(a) - 2, -1, -1):
        mxm = 0
        # Check all elements after the current element
        for j in range(i + 1, len(a)):
            # If a[j] is divisible by a[i] or vice versa, update the maximum subset size
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                mxm = max(mxm, dp[j])
        # Update dp[i] with the size of the largest subset ending with a[i]
        dp[i] = 1 + mxm
    
    # Return the maximum value in dp array which represents the largest subset size
    return max(dp)

# Test the function with the provided test case
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4
