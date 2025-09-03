"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(nested_lists):
    # Initialize an empty set to store common elements
    common_elements = set()
    
    # Iterate over each sublist in the list of nested lists
    for sublist in nested_lists:
        # Update the common_elements set with elements from the current sublist
        common_elements.update(sublist)
    
    return common_elements

# Test the function with the provided test case
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) == set([18, 12])