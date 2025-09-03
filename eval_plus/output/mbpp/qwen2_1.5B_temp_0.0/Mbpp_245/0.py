"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(arr):
    n = len(arr)
    # Initialize dp arrays for increasing and decreasing subsequences
    inc = [1] * n
    dec = [1] * n
    
    # Fill up the increasing dp array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + 1)
    
    # Fill up the decreasing dp array
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    # Calculate the maximum sum of bitonic subsequences
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - 1)  # Subtract 1 to exclude the element itself
    
    return max_sum

# Test the function with the provided data point
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194