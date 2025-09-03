"""
We say that an element is common for lists l1, l2, l3 if it appears in all three lists under the same index. Write a function to find common elements from three lists. The function should return a list.
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
"""
def extract_index_list(list1, list2, list3):
    # Initialize an empty list to store the common elements
    common_elements = []
    
    # Iterate over the indices of the lists
    for i in range(len(list1)):
        # Check if the elements at the current index are the same across all three lists
        if list1[i] == list2[i] == list3[i]:
            # If they are the same, append the element to the common_elements list
            common_elements.append(list1[i])
    
    # Return the list of common elements
    return common_elements

# Test the function with the provided test case
assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 7]
