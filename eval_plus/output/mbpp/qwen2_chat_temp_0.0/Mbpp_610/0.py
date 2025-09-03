"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(nums, k):
    # Remove the k-th element from the list (index k-1)
    nums.pop(k - 1)
    return nums

# Test the function with the provided test case
assert remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3) == [1, 1, 3, 4, 4, 5, 1]