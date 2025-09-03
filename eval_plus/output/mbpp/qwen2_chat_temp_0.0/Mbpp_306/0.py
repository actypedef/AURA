"""
Write a function to find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i .
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
"""
def max_sum_increasing_subseq(arr, n, i, k):
    # If the current index exceeds the array length or if k is not greater than i, return 0
    if (i >= n or k <= i):
        return 0
    
    # Initialize result as the maximum between the current element and the next element
    res = max(arr[i], arr[k])
    
    # Iterate through the array starting from the next element after k
    for j in range(k + 1, n):
        # Check if the current element is greater than the previous element and if it's less than the current result
        if ((arr[j] > arr[j - 1]) and (arr[j] < res)):
            # Recursively call the function with updated parameters and update the result
            res = max(res, max_sum_increasing_subseq(arr, n, j, k))
    
    # Return the final result
    return res

# Test the function with the provided test case
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11