"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    # Sort the array in ascending order
    arr.sort()
    
    # Return the k-th element (1-based index)
    return arr[k - 1]

# Test the function with the provided test case
assert kth_element([12, 3, 5, 7, 19], 2) == 3
