"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(list1, L):
    # Create a new list excluding the k'th element (0-based index)
    return list1[:L-1] + list1[L:]

# Test the function with the provided test case
assert remove_kth_element([1,1,2,3,4,4,5,1], 3) == [1, 1, 2, 4, 4, 5, 1]
