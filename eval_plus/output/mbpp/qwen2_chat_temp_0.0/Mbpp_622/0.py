"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(arr1, arr2, n):
    # Combine both arrays into one
    merged = arr1 + arr2
    
    # Sort the combined array
    merged.sort()
    
    # Calculate the median based on the length of the merged array
    if len(merged) % 2 == 0:
        return (merged[n - 1] + merged[n]) / 2.0
    else:
        return float(merged[n - 1])

# Test the function with the provided test case
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0