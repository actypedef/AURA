"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(nums1, nums2, n):
    # Merge the two sorted arrays into one
    merged = sorted(nums1 + nums2)
    
    # Calculate the median based on the length of the merged array
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2.0
    else:
        return merged[n//2]

# Test cases to verify the correctness of the solution
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
assert get_median([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5) == 5.5
assert get_median([-10, -5, 0, 5, 10], [-20, -15, 0, 15, 20], 5) == 0.0