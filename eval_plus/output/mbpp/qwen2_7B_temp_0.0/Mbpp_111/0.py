"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(lists):
    # Initialize an empty list to store common elements
    common_elements = []
    
    # Iterate over each element in the first list
    for i in lists[0]:
        # Check if the element is present in all other lists
        if all(i in sublist for sublist in lists):
            # If present, add it to the common_elements list
            common_elements.append(i)
    
    # Convert the list of common elements to a set and return
    return set(common_elements)

# Test the function with the provided test case
assert common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == {18, 12}
