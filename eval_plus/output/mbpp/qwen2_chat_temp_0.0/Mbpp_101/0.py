"""
Write a function to find the kth element in the given array using 1-based indexing.
assert kth_element([12,3,5,7,19], 2) == 3
"""
def kth_element(arr, k):
    # Return the k-1 index element from the array (since list indices start at 0)
    return arr[k - 1]

# Test the function with the provided test case
assert kth_element([12, 3, 5, 7, 19], 2) == 3
