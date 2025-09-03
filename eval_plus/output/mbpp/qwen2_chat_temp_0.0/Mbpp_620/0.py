"""
Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
"""
def largest_subset(arr):
    n = len(arr)
    
    # Initialize dp array where dp[i] will store the size of the largest subset ending at index i
    dp = [1] * n
    
    # Iterate over each element in the array
    for i in range(n):
        # Check all previous elements to see if they form a valid subset with arr[i]
        for j in range(i):
            # If arr[j] divides arr[i], update dp[i]
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The result is the maximum value in the dp array
    return max(dp)

# Test the function with the provided test case
assert largest_subset([1, 3, 6, 13, 17, 18]) == 4