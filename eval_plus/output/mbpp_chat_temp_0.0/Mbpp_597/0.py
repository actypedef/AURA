"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    # Initialize pointers for both arrays
    i = j = 0
    
    # Loop until we reach the k-th element
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            i += 1
        else:
            j += 1
        
        # If we have reached the k-th element, return it
        if i + j == k:
            if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
                return arr1[i]
            else:
                return arr2[j]

# Test the function with the provided test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6