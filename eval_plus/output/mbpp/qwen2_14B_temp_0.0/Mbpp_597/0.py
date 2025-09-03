"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    # Ensure arr1 is the smaller array
    if len(arr1) > len(arr2):
        return find_kth(arr2, arr1, k)
    
    # If arr1 is empty, return the k-th element from arr2
    if not arr1:
        return arr2[k - 1]
    
    # If k is 1, return the smallest element from both arrays
    if k == 1:
        return min(arr1[0], arr2[0])
    
    # Calculate the partition sizes
    partition1 = min(k // 2, len(arr1))
    partition2 = k - partition1
    
    # Compare elements at the partition positions
    if arr1[partition1 - 1] <= arr2[partition2 - 1]:
        # If the element in arr1 is smaller or equal, discard elements before partition1 in arr1
        return find_kth(arr1[partition1:], arr2, k - partition1)
    else:
        # Otherwise, discard elements before partition2 in arr2
        return find_kth(arr1, arr2[partition2:], k - partition2)

# Test the function with the provided test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6