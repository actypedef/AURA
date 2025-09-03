"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    # Return the k-th element of the array using 1-based indexing
    return arr[k - 1]

# Test cases to validate the solution
assert kth_element([12, 3, 5, 7, 19], 2) == 3
