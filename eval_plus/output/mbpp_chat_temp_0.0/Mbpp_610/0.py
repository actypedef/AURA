"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(test_list, K):
    # Using list slicing to exclude the K-th element (index K-1)
    res = test_list[:K] + test_list[K+1:]
    return res

# Test the function with the provided test case
assert remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3) == [1, 1, 3, 4, 4, 5, 1]
