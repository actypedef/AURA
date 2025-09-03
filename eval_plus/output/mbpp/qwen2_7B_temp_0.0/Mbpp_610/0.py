"""
Write a python function which takes a list and returns a list with the same elements, but the k'th element removed.
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
"""
def remove_kth_element(test_list, K):
    # Initialize an empty list to store the result
    res = []
    # Iterate over the test_list using enumerate to get both index and value
    for idx, ele in enumerate(test_list):
        # Check if the current index is not equal to K (0-based index)
        if idx != K:
            # Append the element to the result list if it's not at position K
            res.append(ele)
    return res

# Test the function with the provided test case
assert remove_kth_element([1, 1, 2, 3, 4, 4, 5, 1], 3) == [1, 1, 3, 4, 4, 5, 1]
