"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(arr1, arr2, n):
    # Initialize variables for binary search
    i = 0
    j = 0
    
    # Find the partition point where both halves have equal elements
    while (i < n and j < n):
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            j += 1
    
    # If one array is exhausted, use the other array's remaining elements
    if i >= n:
        return float(arr2[j + (n - i)])
    elif j >= n:
        return float(arr1[i + (n - j)])
    
    # Calculate the median using the partition points
    return float((max(arr1[i-1], arr2[j-1]) + min(arr1[i], arr2[j])) / 2)

# Test the function with the provided test case
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
