"""
Write a function that takes an array and finds the maximum sum of a bitonic subsequence for the given array, where a sequence is bitonic if it is first increasing and then decreasing.
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
"""
def max_sum(A):
    n = len(A)
    
    # Initialize lists to store the maximum sum of increasing subsequences up to each element
    inc = [0] * n
    dec = [0] * n
    
    # Fill the 'inc' array
    for i in range(n):
        inc[i] = A[i]
        for j in range(i):
            if (A[i] > A[j] and inc[i] < inc[j] + A[i]):
                inc[i] = inc[j] + A[i]
    
    # Fill the 'dec' array
    for i in range(n - 1, -1, -1):
        dec[i] = A[i]
        for j in range(i + 1, n):
            if (A[i] > A[j] and dec[i] < dec[j] + A[i]):
                dec[i] = dec[j] + A[i]
    
    # Find the maximum sum of a bitonic subsequence
    mx = 0
    for i in range(n):
        mx = max(mx, inc[i] + dec[i] - A[i])
    
    return mx

# Test the function with the provided test case
assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
