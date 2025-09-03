"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
def max_length(lst):
    # Find the maximum length among all sublists
    max_len = max(len(x) for x in lst)
    
    # Filter out the sublist(s) with the maximum length
    result = [x for x in lst if len(x) == max_len]
    
    return (max_len, result[0])

# Test the function with the provided test case
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])