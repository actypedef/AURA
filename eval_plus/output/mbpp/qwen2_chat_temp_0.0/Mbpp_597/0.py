"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    # Initialize pointers for both arrays
    i = j = 0
    
    # Iterate until we reach the k-th element
    while (i + j < k):
        if i == len(arr1): 
            return arr2[j]
        elif j == len(arr2): 
            return arr1[i]
        elif arr1[i] <= arr2[j]: 
            i += 1
        else: 
            j += 1
    
    # Return the k-th element
    return min(arr1[i], arr2[j])

# Test the function with the provided test case
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6