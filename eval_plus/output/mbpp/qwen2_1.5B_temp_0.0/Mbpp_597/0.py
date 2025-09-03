"""
Write a function to find kth element from the given two sorted arrays.
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
def find_kth(arr1, arr2, k):
    # Initialize pointers for both arrays
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            # If current element of arr1 is smaller or equal,
            # move pointer of arr1 forward
            i += 1
        else:
            # If current element of arr2 is smaller,
            # move pointer of arr2 forward
            j += 1
        
        # Decrement k as we have moved one step closer to the k-th element
        k -= 1
    
    # If there are remaining elements in arr1, return the next one
    if i < len(arr1):
        return arr1[i]
    
    # If there are remaining elements in arr2, return the next one
    return arr2[j]

# Test cases to verify the correctness of the function
assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
assert find_kth([1, 2, 3], [4, 5, 6], 4) == 3
assert find_kth([-1, -2, -3], [-4, -5, -6], 3) == -3
assert find_kth([], [], 1) == None