"""
Write a function to append the given list to the given tuples.
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
"""
def add_lists(test_list, test_tup):
    # Convert the tuple to a list, extend it with the original list, and convert back to a tuple
    res = tuple(list(test_tup) + test_list)
    return res

# Test the function with the provided test case
assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
