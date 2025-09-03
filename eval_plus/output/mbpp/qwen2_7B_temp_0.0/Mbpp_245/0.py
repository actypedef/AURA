"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(arr):
    n = len(arr)
    
    # Initialize arrays to store maximum sums
    inc = [0] * n
    dec = [0] * n
    
    # Calculate maximum sum of increasing subsequences
    for i in range(n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                inc[i] = max(inc[i], inc[j] + arr[i])
    
    # Calculate maximum sum of decreasing subsequences
    for i in range(n-1, -1, -1):
        dec[i] = arr[i]
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                dec[i] = max(dec[i], dec[j] + arr[i])
    
    # Find the maximum sum of bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, inc[i] + dec[i] - arr[i])
    
    return max_bitonic_sum

# Test the function with the provided test case
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194