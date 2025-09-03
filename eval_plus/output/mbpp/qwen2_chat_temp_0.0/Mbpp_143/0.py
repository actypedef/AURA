"""
Write a function to find number of lists present in the given tuple.
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2
"""
def find_lists(test_tup):
    # Count the number of list elements in the tuple
    res = sum(isinstance(ele, list) for ele in test_tup)
    return res

# Test the function with the provided test case
assert find_lists(([1, 2, 3, 4], [5, 6, 7, 8])) == 2