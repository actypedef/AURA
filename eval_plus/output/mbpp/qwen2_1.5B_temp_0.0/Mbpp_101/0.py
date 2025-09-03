"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    # Check if the index k is within the valid range of the array indices
    if k < 1 or k > len(arr):
        raise ValueError("Index out of bounds")
    
    # Return the k-th element of the array (1-based indexing)
    return arr[k-1]

# Test cases to verify the correctness of the function
assert kth_element([12,3,5,7,19], 2) == 3
assert kth_element([10,20,30,40,50], 4) == 40
assert kth_element([-1, -2, -3, -4, -5], 3) == -3