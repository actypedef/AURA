"""
Write a function to find the maximum product formed by multiplying numbers of an increasing subsequence of that array.
assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
def max_product(arr):
    n = len(arr)
    
    # Initialize the list to store the maximum product subsequence ending at each index
    dp = [0] * n
    
    # The maximum product subsequence for any single element is the element itself
    for i in range(n):
        dp[i] = arr[i]
    
    # Iterate through the array to fill the dp array
    for i in range(1, n):
        for j in range(i):
            # Check if the current element forms an increasing subsequence with the previous elements
            if arr[i] > arr[j]:
                # Update the dp value to be the maximum product found so far
                dp[i] = max(dp[i], dp[j] * arr[i])
    
    # Return the maximum value from the dp array, which represents the maximum product subsequence
    return max(dp)

# Test the function with the provided test case
assert max_product([3, 100, 4, 5, 150, 6]) == 3000