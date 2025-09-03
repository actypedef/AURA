"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    # Initialize pointers for both arrays
    i = j = 0
    
    # Traverse through both arrays
    while i < len(arr1) and j < len(arr2):
        if i + j == k - 1:  # Check if we have reached the k-th position
            return min(arr1[i], arr2[j])  # Return the minimum of the current elements
        elif arr1[i] < arr2[j]:
            i += 1  # Move pointer in arr1
        else:
            j += 1  # Move pointer in arr2
    
    # If one array is exhausted, continue with the other
    if i == len(arr1):
        return arr2[k - i - 1]
    else:
        return arr1[k - j - 1]

# Test the function with the provided test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6