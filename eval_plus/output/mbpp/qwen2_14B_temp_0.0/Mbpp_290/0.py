"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
def max_length(lists):
    # Find the maximum length among all sublists
    max_len = max(len(x) for x in lists)
    
    # Find the sublist with the maximum length
    max_list = max(lists, key=lambda i: len(i))
    
    return (max_len, max_list)

# Test the function with the provided test case
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
