"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(arr):
    n = len(arr)
    
    # Initialize arrays to store the maximum sum increasing subsequence ending at each index
    inc = [arr[i] for i in range(n)]
    
    # Calculate the maximum sum increasing subsequence for each element
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
    
    # Initialize arrays to store the maximum sum decreasing subsequence starting at each index
    dec = [arr[i] for i in range(n)]
    
    # Calculate the maximum sum decreasing subsequence for each element
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]
    
    # Find the maximum sum of bitonic subsequence
    max_bitonic_sum = 0
    for i in range(n):
        max_bitonic_sum = max(max_bitonic_sum, inc[i] + dec[i] - arr[i])
    
    return max_bitonic_sum

# Test the function with the provided test case
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194