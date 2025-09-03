"""
Write a function to find the common elements in given nested lists.
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
"""
def common_in_nested_lists(lists):
    # Initialize the intersection with the first list converted to a set
    intersection = set(lists[0])
    
    # Iterate over the remaining lists and update the intersection
    for lst in lists[1:]:
        intersection &= set(lst)
    
    return list(intersection)

# Test the function with the provided test case
assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]])) == set([18, 12])
