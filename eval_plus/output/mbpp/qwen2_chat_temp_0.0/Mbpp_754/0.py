"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""
def extract_index_list(l1, l2, l3):
    # Initialize an empty list to store common elements
    res = []
    
    # Iterate over the indices of the lists using zip
    for i, j, k in zip(l1, l2, l3):
        # Check if the current elements at the same index are equal
        if i == j == k:
            # If they are equal, append the element to the result list
            res.append(i)
    
    # Return the list of common elements
    return res

# Test the function with the provided test case
assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 7]
